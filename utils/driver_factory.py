from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import BROWSER, HEADLESS


def create_driver():
    if BROWSER == "firefox":
        options = FirefoxOptions()
        if HEADLESS:
            options.add_argument("-headless")
        options.add_argument("--width=1440")
        options.add_argument("--height=1200")
        return webdriver.Firefox(options=options)
    options = ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1440,1200")
    return webdriver.Chrome(options=options)
