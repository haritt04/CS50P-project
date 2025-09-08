# Missing File Alert System

#### Video Demo:  <URL HERE>

#### Description: 
File Missing Alert System is a Python program that will work to track a local folder, where it is assumed that the files fit a specific template. It checks that these files are not empty. When a file is deleted, or it contains zero bytes, an email notification is issued to the specified recipients and a record is made in a inserted time-stamped log file.

The project is coded fully with one main and other functions: `checkfile()`, `log_result()`, `send_email_alert()` and `main()`. The program is writeable and maintainable as each functionality is modular. 

`check_file()` scans files that meet the desired pattern and validates their sizes. `log_result()` writes detailed logs with timestamps of every check that has been completed. 
`send_email_alert()` sends emails to recipients and logs may be attached to their email. `main()` coordinates all the workflow, so that only checks within a specified time range are run.

To test, `test_project.py` contains pytest functions `check_file()`, `log_result()` and `send_email_alert()` to make sure it will work without actually sending real emails. Environment variables are configuration values defined as email credentials, file paths, and filename patterns, and can be easily modified using `.env.example`.

This project illustrates file monitoring, logging, email notification and simple testing principles. It may be expanded to several directories, dynamic pattern of files, or to interoperability with web dashboards. The modular architecture makes the program maintainable and scalable in real world.

---

## Features
- Checks a local folder for files matching a defined pattern.
- Validates that the file is non-empty.
- Sends an email alert if the file is missing or empty.
- Attaches the log file to email alerts for review.
- Logs results with timestamps for record keeping.
- Configurable file pattern, directory, and email recipients.

---

## Requirements
- Python 3.8+
- Gmail account for SMTP (use App Password for authentication)
- Standard Python libraries (`os`, `datetime`, `smtplib`, `email`)  
---

## Setup Instructions

1. **Clone the repository**
```bash
git clone <repository_url>
cd file-alert
````

2. **Create and activate a virtual environment** (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. **Install dependencies** (if using `.env` and `python-dotenv`)

```bash
pip install -r requirements.txt
```

4. **Configuration**

* Copy `.env.example` to `.env` or edit the script directly.
* Provide your own **test Gmail account** for sending emails (do not use personal/company email).
* Update the following values:

  * `SENDER_EMAIL` → Gmail sender
  * `EMAIL_PASSWORD` → App Password
  * `RECEIVER_EMAILS` → comma-separated list of recipients
  * `LOCAL_PATH` → directory to monitor
  * `FILENAME_PATTERN` → pattern to match filenames (e.g., `filename_pattern_YYYYMMDD_`)

---

## Running the Script

```bash
python file_alert.py
```

* The script only runs during the allowed time window (default 01:00–01:30).
* If the file is missing or empty, an email alert is sent and a log is saved.
* If the file exists and is valid, a success email is sent with the log attached.

---

## Sample Files

Include a sample file in `files_to_check/` to demonstrate functionality.

---

## Notes

* For security, **do not commit real email credentials**.
* The system can be extended to check multiple files, different directories, or even send SMS using APIs like Twilio.
* Logs are created daily with the date in the filename (`YYYYMMDD.log`) for easy tracking.

---

## Example Log Entry

```
[2025-09-08 01:15:03] File filename_pattern_20250908_test.csv found with size 1024 bytes.
```

* Shows timestamped results of file check and alerts sent.

---

## Author

Nyi Nyi Phyo

