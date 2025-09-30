# File Missing Alert System

#### Video Demo: <URL HERE>

#### Description:

The File Missing Alert System is a python project that will be used to track files in a local directory that match a given pattern. Where there is a missing file or an empty file, an alert is raised by the system. Timestamps are added to all results, both successes, and failures.

The project shows Python programming, such as functions, logging, environment setup, and pytest testing. It is organized according to CS50P final project requirements.

---

#### Author

**Nyi Nyi Phyo**

* CS50P Final Project Submission
* City, Country: <Yangon, Myanmar>
* Date: <September 30, 2025>

## Features

1. **File Monitoring:**  
   Checks if files with a specific naming pattern exist in a local directory and verifies that they are not empty.

2. **Logging:**  
   Writes all events to a timestamped log file in the project folder for tracking file status.

3. **Alert System:**  
   Instead of sending email (SMTP), which can be blocked in restricted environments, this project:
   - Prints alerts to the console.
   - Saves alerts to a structured JSON file (`alerts.json`) for easy review.

4. **Configuration via Environment Variables:**  
   Supports `.env` configuration for the following variables:
   - `LOCAL_PATH` – Path to the directory to monitor.
   - `FILENAME_PATTERN` – Base pattern to check in filenames.
   - Optional email credentials placeholders (not required for local testing).

5. **Testable Functions:**  
   The project includes four main functions:
   - `check_file()` – Verifies file existence and size.
   - `log_result()` – Logs results to the log file.
   - `send_alert()` – Simulates alerts via console and JSON.
   - `main()` – Runs the complete workflow.

---

## Project Structure

```

CS50P-project/
├── project.py            # Main project code
├── test\_project.py       # Pytest tests for main functions
├── README.md             # Project documentation
├── .env.example          # Example environment variables file
├── files\_to\_check/       # Directory to place test files
└── alerts.json           # JSON file storing alerts 

```

---

## Design Decisions

1. **Configurable Paths and Patterns:**
    Environment variables can also be customized to enable all paths and pattern of files to be tested flexibly.

2. **Testable Functions:**
   Functions are also testable and modular with `pytest`. This has optional overrides in paths and log files.

3. **Logging and Alerts:**
    Uses human-readable logs and well-structured JSON alerts to show that there is a professionally-written software engineering process.
---

## Future Enhancements

* Optionally integrate actual SMTP or SMS alerts for production deployment.
* Extend monitoring to multiple directories or recursive checks.
* Add more complex filename patterns and advanced alert logic.
* Include a web interface/dashboard for alerts.

---


