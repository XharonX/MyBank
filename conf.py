from datetime import datetime

def get_rtc():
    today = datetime.now()
    return datetime.strftime(today, "%Y-%m-%d")
