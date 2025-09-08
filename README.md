# File Missing Alert System

#### Video Demo: <URL HERE>

#### Description:

The File Missing Alert System is a python project that will be used to track files in a local directory that match a given pattern. Where there is a missing file or an empty file, an alert is raised by the system. Timestamps are added to all results, both successes, and failures.

The project shows Python programming, such as functions, logging, environment setup, and pytest testing. It is organized according to CS50P final project requirements.

---

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

````

---

## Getting Started

1. **Clone or download** the repository.
2. **Install dependencies** (if any are added; currently standard library used):
   ```bash
   pip install -r requirements.txt
````

3. **Create a `.env` file** in the root directory based on `.env.example`:

   ```env
   LOCAL_PATH=./files_to_check/
   FILENAME_PATTERN=filename_pattern_
   ```
4. **Add test files** in the `files_to_check/` directory to simulate missing or existing files.
5. **Run the project**:

   ```bash
   python project.py
   ```
6. **Check logs**:

   * Console output will show alerts.
   * `alerts.json` will contain structured JSON records for each alert.
   * Timestamped log file (`YYYYMMDD.log`) will record all checks.

---

## Testing

The project includes `pytest` test cases for all main functions.

Run tests with:

```bash
pytest test_project.py
```

Test coverage:

* File existence and size verification.
* Logging function writes correctly.
* Alert simulation writes to console and JSON.

---

## Example `.env.example`

```
# Directory to monitor
LOCAL_PATH=./files_to_check/

# Filename base pattern
FILENAME_PATTERN=filename_pattern_


**Note:** Alerts are handled via console output and `alerts.json`.

---

## Design Decisions

1. **No SMTP for Alerts:**
    SMTP could not work in limited networks. The project records notifications to JSON and displays them on the console so that they can be reviewable. 

2. **Configurable Paths and Patterns:**
    Environment variables can also be customized to enable all paths and pattern of files to be tested flexibly.

3. **Testable Functions:**
   Functions are also testable and modular with `pytest`. This has optional overrides in paths and log files.

4. **Logging and Alerts:**
    Uses human-readable logs and well-structured JSON alerts to show that there is a professionally-written software engineering process.
---

## Future Enhancements

* Optionally integrate actual SMTP or SMS alerts for production deployment.
* Extend monitoring to multiple directories or recursive checks.
* Add more complex filename patterns and advanced alert logic.
* Include a web interface/dashboard for alerts.

---

#### Author

**Nyi Nyi Phyo**
CS50P Final Project Submission
City, Country: \<Yangon, Myanmar>
Date: <Submission Date>

