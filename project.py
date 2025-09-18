import os
import datetime
import json
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv() 

LOCAL_PATH = os.getenv("LOCAL_PATH", "./files_to_check/")
FILENAME_PATTERN = os.getenv("FILENAME_PATTERN", "filename_pattern")
LOG_FILE = f"{datetime.datetime.now().strftime('%Y%m%d')}.log"
ALLOWED_START = datetime.datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
ALLOWED_END = datetime.datetime.now().replace(hour=14, minute=30, second=0, microsecond=0)
ALERT_FILE = "alerts.json"   

# Function 1
def check_file(local_path=None):
    try:
        path_to_check = local_path or LOCAL_PATH
        files = os.listdir(path_to_check)
        today_str = datetime.datetime.now().strftime("%Y%m%d")
        pattern = f"{FILENAME_PATTERN}"
        matched_files = [f for f in files if pattern in f]

        if not matched_files:
            return False, f"No file found with pattern {pattern}*"

        for filename in matched_files:
            filepath = os.path.join(path_to_check, filename)
            size = os.path.getsize(filepath)
            if size == 0:
                return False, f"File {filename} exists but size is 0 bytes."
            else:
                return True, f"File {filename} found with size {size} bytes."
    except Exception as e:
        return False, f"Exception during file check: {str(e)}"


# Function 2
def log_result(message: str, log_file: str = None):
    """
    Log message to log_file with timestamp.
    If log_file is None, uses default LOG_FILE.
    """
    log_file_to_use = log_file or LOG_FILE
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_to_use, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


# Function 3
def send_alert(subject, body, alert_file=None):
    """
    Simulates sending an alert by logging to a file and printing to console.
    """
    print(f"ALERT: {subject}\n{body}")

    alert = {
        "time": datetime.datetime.now().isoformat(),
        "subject": subject,
        "body": body
    }

    alert_file_to_use = alert_file or ALERT_FILE
    with open(alert_file_to_use, "a", encoding="utf-8") as f:
        f.write(json.dumps(alert) + "\n")


# Function 4 (main)
def main():
    """Main function to execute file alert workflow."""
    now = datetime.datetime.now()
    if not ALLOWED_START <= now <= ALLOWED_END:
        print(f"Script run at {now.strftime('%H:%M:%S')} — outside allowed time window. Exiting.")
        return

    success, message = check_file()
    log_result(message)
    print(message)

    if not success:
        send_alert("File Missing or Empty", message)
    else:
        send_alert("File Successfully Received", message)


if __name__ == "__main__":
    main()

