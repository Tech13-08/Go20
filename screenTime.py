import time
import datetime
import logging

logging.basicConfig(filename='script_log.txt', level=logging.DEBUG)


def process_lid_status_log():
    # Read the number of lines in "lid_status.log"
    with open("lid_status.log", "r") as log_file:
        lines = log_file.readlines()

    # Calculate total minutes and convert to hours
    total_minutes = len(lines)
    total_hours = total_minutes / 60

    # Save the number of hours
    with open("daily_screen_time.txt", "a") as result_file:
        result_file.write(f"{total_hours:.1f}\n")

    # Clear the "lid_status.log" file
    open("lid_status.log", "w").close()

if __name__ == "__main__":
    try:
        # Process lid status log and save data
        process_lid_status_log()
    except Exception as e:
        logging.exception(f"An error occurred: {str(e)}")
        # Delay before restarting
        time.sleep(10)  # Adjust the delay as needed
