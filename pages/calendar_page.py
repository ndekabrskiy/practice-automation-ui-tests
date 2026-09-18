import allure
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import CALENDARS_URL
from pages.base_page import BasePage


class CalendarPage(BasePage):
    DATE = (By.CSS_SELECTOR, "input.jp-contact-form-date")
    PICKER = (By.CSS_SELECTOR, "div.dp-cal")
    MONTH = (By.CSS_SELECTOR, "div.dp-cal button.dp-cal-month")
    NEXT = (By.CSS_SELECTOR, "div.dp-cal button.dp-next")
    PREVIOUS = (By.CSS_SELECTOR, "div.dp-cal button.dp-prev")
    SUBMIT = (By.CSS_SELECTOR, "form[aria-label='Calendars'] button[type='submit']")

    def open_page(self):
        self.open(CALENDARS_URL)

    @allure.step("Открыть календарь")
    def open_picker(self):
        self.clickable(self.DATE).click()
        return self.visible(self.PICKER)

    def month(self):
        return self.visible(self.MONTH).text

    def select_today(self):
        self.open_picker()
        target_date = date.today()
        target = target_date.strftime("%Y-%m-%d")
        aria_target = target_date.strftime("%a %b %d %Y")
        for _ in range(24):
            for item in self.driver.find_elements(By.CSS_SELECTOR, "div.dp-cal button.dp-day"):
                if aria_target in item.get_attribute("aria-label"):
                    item.click()
                    return target
            self.clickable(self.NEXT).click()
        raise AssertionError(f"Date {target} was not found")

    def enter(self, value):
        field = self.visible(self.DATE)
        field.clear(); field.send_keys(value); field.send_keys(Keys.TAB)

    def value(self):
        return self.present(self.DATE).get_attribute("value") or ""
