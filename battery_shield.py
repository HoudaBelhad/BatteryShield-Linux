import os
import time
import json
import tkinter as tk
from datetime import datetime

# CONFIGURATION
PATH = "/sys/class/power_supply/BAT0/"
LOG_FILE = os.path.expanduser("~/battery_logs.json")
CHECK_INTERVAL = 10 
CRITICAL_THRESHOLD = 20

def get_battery_stats():
    try:
        # percentage reading
        with open(PATH + "capacity", "r") as f:
            percent = int(f.read().strip())
        
        # status reading
        with open(PATH + "status", "r") as f:
            status = f.read().strip().capitalize()
        
        # health
        full_file = "energy_full" if os.path.exists(PATH + "energy_full") else "charge_full"
        design_file = "energy_full_design" if os.path.exists(PATH + "energy_full_design") else "charge_full_design"
        
        with open(PATH + full_file, "r") as f:
            full = int(f.read().strip())
        with open(PATH + design_file, "r") as f:
            design = int(f.read().strip())
        
        health = round((full / design) * 100, 2)
        return percent, status, health
    except Exception as e:
        try:
            with open(PATH + "capacity", "r") as f:
                p = int(f.read().strip())
            with open(PATH + "status", "r") as f:
                s = f.read().strip().capitalize()
            return p, s, 100
        except:
            return 100, "Unknown", 100
        
def log_data(percent, status, health):
    # Gamification
    points = 10 if (percent > 20 and status == "Charging") else 0
    
    entry = {
        "timestamp": datetime.now().isoformat(),
        "percent": percent,
        "status": status,
        "health": health,
        "points_earned": points
    }
    
    data = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                data = json.load(f)
        except: data = []
    
    data.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(data[-5000:], f, indent=4)

def show_alert():
    root = tk.Tk()
    root.title("ALERTE CRITIQUE")
    root.attributes("-fullscreen", True, "-topmost", True)
    root.configure(bg='red')
    
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tk.Label(root, text="⚡ BRANCHE TON PC ! ⚡", 
                     fg="white", bg="red", font=("Helvetica", 50, "bold"))
    label.pack(expand=True)
    
    sub_label = tk.Label(root, text="Le système est bloqué jusqu'à la mise en charge", 
                         fg="white", bg="red", font=("Helvetica", 15))
    sub_label.pack(pady=20)

    def monitor_charge():
        try:
            with open(PATH + "status", "r") as f:
                current_status = f.read().strip().capitalize()
            
            if current_status == "Charging":
                root.destroy()
            else:
                # Effet clignotant agressif
                curr_bg = root.cget("bg")
                new_bg = "black" if curr_bg == "red" else "red"
                root.configure(bg=new_bg)
                label.configure(bg=new_bg)
                sub_label.configure(bg=new_bg)
                root.after(500, monitor_charge)
        except:
            root.after(500, monitor_charge)

    os.system('canberra-gtk-play --id="suspend-error" &')
    
    monitor_charge()
    root.mainloop()

def main():
    print(f"--- BatteryShield lancé à {datetime.now().strftime('%H:%M')} ---")
    print(f"Seuil critique : {CRITICAL_THRESHOLD}%")
    
    while True:
        p, s, h = get_battery_stats()
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {p}% | {s} | Santé: {h}%")
        
        log_data(p, s, h)
        
        if p <= CRITICAL_THRESHOLD and s != "Charging":
            print(">> DECLENCHEMENT FENETRE ROUGE <<")
            show_alert()
            
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
