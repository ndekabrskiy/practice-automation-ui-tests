import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import ADS_URL, TIMEOUT
from pages.base_page import BasePage


class AdsPage(BasePage):
    AD = (By.ID, "pum-1272")
    CLOSE = (By.CSS_SELECTOR, "#pum-1272 .pum-close")

    def open_page(self):
        self.open(ADS_URL)

    def wait_for_ad(self):
        WebDriverWait(self.driver, TIMEOUT + 5).until(lambda _: self.is_visible(self.AD))

    def close_ad(self):
        self.visible(self.CLOSE).click()
        WebDriverWait(self.driver, TIMEOUT).until(lambda _: not self.is_visible(self.AD))

    def text(self):
        return self.visible((By.CSS_SELECTOR, "#pum-1272 .pum-content")).text
