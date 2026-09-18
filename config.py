import os

BASE_URL = os.getenv("BASE_URL", "https://practice-automation.com")
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "true").lower() not in {"0", "false", "no"}
TIMEOUT = int(os.getenv("TIMEOUT", "15"))
CALENDARS_URL = f"{BASE_URL}/calendars/"
MODALS_URL = f"{BASE_URL}/modals/"
ADS_URL = f"{BASE_URL}/ads/"
HOME_URL = f"{BASE_URL}/"
