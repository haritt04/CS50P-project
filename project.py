"""
File Missing Alert System
-----------------------------------
Checks a local directory for files matching a pattern.
Sends an email alert if files are missing or empty.
Logs all results to a timestamped log file.
"""

import os
import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Configuration
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "mediationalert@@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
RECEIVER_EMAILS = os.getenv("RECEIVER_EMAILS", "harrynyinyi183@gmail.com,harrynyinyi184@gmail.com").split(",")
LOCAL_PATH = os.getenv("LOCAL_PATH", "./files_to_check/")
FILENAME_PATTERN = os.getenv("FILENAME_PATTERN", "filename_pattern")
LOG_FILE = f"{datetime.datetime.now().strftime('%Y%m%d')}.log"
ALLOWED_START = datetime.datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
ALLOWED_END = datetime.datetime.now().replace(hour=16, minute=30, second=0, microsecond=0)


# Function 1
def check_file(local_path=None):
    """
    Check if today's file exists in LOCAL_PATH and is non-empty.
    Optional: pass local_path to override module-level LOCAL_PATH (for testing)
    Returns: (bool, str) -> success, message
    """
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
def send_email_alert(subject: str, body: str, attachment: str = None):
    """Send email alert with optional log attachment."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(RECEIVER_EMAILS)
    msg.set_content(body)
    msg.add_alternative(f"<html><body><h2>File Alert</h2><p>{body}</p></body></html>", subtype="html")

    if attachment and os.path.exists(attachment):
        with open(attachment, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment)
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


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
        send_email_alert("File Missing or Empty", message, LOG_FILE)
    else:
        send_email_alert("File Successfully Received", message, LOG_FILE)


if __name__ == "__main__":
    main()
