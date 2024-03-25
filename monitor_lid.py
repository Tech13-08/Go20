import time
from datetime import datetime
import psutil
import logging

logging.basicConfig(filename='script_log.txt', level=logging.DEBUG)

def monitor_lid_status():
    try:
        # Get the current power status
        power_status = psutil.sensors_battery().power_plugged


        with open("userActive.txt", "r") as user_active:
            if len(user_active.read()) > 0:  
                # Log the event with timestamp
                log_event(power_status)

    except Exception as e:
        logging.exception(f"An error occurred: {str(e)}")
        # Delay before restarting
        time.sleep(1)  # Adjust the delay as needed

def log_event(power_status):
    event_type = "AC Power Connected" if power_status else "On Battery"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - Power Status: {event_type}"

    # Append the log message to a file
    with open("lid_status.log", "a") as log_file:
        log_file.write(log_message + "\n")

if __name__ == "__main__":
    monitor_lid_status()
