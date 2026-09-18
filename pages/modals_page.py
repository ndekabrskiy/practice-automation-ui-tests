import allure
from selenium.webdriver.common.by import By
from config import MODALS_URL
from pages.base_page import BasePage


class ModalsPage(BasePage):
    SIMPLE_BUTTON = (By.ID, "simpleModal")
    FORM_BUTTON = (By.ID, "formModal")
    SIMPLE = (By.ID, "pum-1318")
    FORM = (By.ID, "pum-674")
    NAME = (By.CSS_SELECTOR, "#pum-674 input[name$='-name']")
    EMAIL = (By.CSS_SELECTOR, "#pum-674 input[name$='-email']")
    MESSAGE = (By.CSS_SELECTOR, "#pum-674 textarea[name$='-message']")

    def open_page(self):
        self.open(MODALS_URL)

    @allure.step("Открыть простое модальное окно")
    def open_simple(self):
        self.clickable(self.SIMPLE_BUTTON).click(); return self.visible(self.SIMPLE)

    @allure.step("Открыть модальное окно с формой")
    def open_form(self):
        self.clickable(self.FORM_BUTTON).click(); return self.visible(self.FORM)

    def fill(self, name="Automation User", email="automation@example.com", message="message"):
        self.visible(self.NAME).send_keys(name)
        self.visible(self.EMAIL).send_keys(email)
        self.visible(self.MESSAGE).send_keys(message)

    def valid(self, locator):
        return bool(self.driver.execute_script("return arguments[0].validity.valid", self.present(locator)))

    def message_value(self):
        return self.present(self.MESSAGE).get_attribute("value") or ""
