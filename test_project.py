import os
import pytest
from project import check_file, log_result, send_email_alert

from datetime import datetime

def test_check_file(tmp_path):
    from project import check_file, FILENAME_PATTERN
    today_str = datetime.now().strftime("%Y%m%d")
    dummy_file = tmp_path / f"{FILENAME_PATTERN}{today_str}_test.txt"
    dummy_file.write_text("data")

    success, msg = check_file(local_path=str(tmp_path))
    assert success is True


def test_log_result(tmp_path):
    from project import log_result
    test_log_file = tmp_path / "test.log"

    log_result("Test message", log_file=str(test_log_file))

    assert test_log_file.exists()
    content = test_log_file.read_text()
    assert "Test message" in content


def test_send_email_alert(monkeypatch):
    class MockSMTP:
        def __init__(self, *args, **kwargs): pass
        def starttls(self): pass
        def login(self, user, pwd): pass
        def send_message(self, msg): pass
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_value, traceback): pass

    monkeypatch.setattr("smtplib.SMTP", MockSMTP)
    success = send_email_alert("Test", "Body", None)
    assert success is True
