import os
import json
import pytest
from project import check_file, log_result, send_alert
from datetime import datetime

def test_check_file(tmp_path):
    today_str = datetime.now().strftime("%Y%m%d")
    dummy_file = tmp_path / f"filename_pattern_{today_str}_test.txt"
    dummy_file.write_text("data")

    # temporarily override LOCAL_PATH
    from project import LOCAL_PATH
    old_path = LOCAL_PATH
    try:
        import project
        project.LOCAL_PATH = str(tmp_path)
        success, msg = check_file()
        assert success is True
        assert "found" in msg
    finally:
        project.LOCAL_PATH = old_path


def test_log_result(tmp_path):
    # temporarily override LOG_FILE
    from project import LOG_FILE
    old_log = LOG_FILE
    test_log_file = tmp_path / "test.log"

    try:
        import project
        project.LOG_FILE = str(test_log_file)
        log_result("Test message")
        assert test_log_file.exists()
        with open(test_log_file, "r") as f:
            contents = f.read()
        assert "Test message" in contents
    finally:
        project.LOG_FILE = old_log


def test_send_alert(tmp_path):
    # redirect alerts.json to tmp_path
    test_alerts = tmp_path / "alerts.json"
    import project

    old_alert_file = getattr(project, "ALERT_FILE", None)
    project.ALERT_FILE = str(test_alerts)

    try:
        send_alert("Test Subject", "Test Body")
        assert test_alerts.exists()
        with open(test_alerts, "r") as f:
            data = f.read().strip().splitlines()
        assert len(data) > 0
        alert_obj = json.loads(data[-1])
        assert alert_obj["subject"] == "Test Subject"
        assert alert_obj["body"] == "Test Body"
    finally:
        if old_alert_file:
            project.ALERT_FILE = old_alert_file
