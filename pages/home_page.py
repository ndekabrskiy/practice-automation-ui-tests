import allure
from selenium.webdriver.common.by import By
from config import HOME_URL
from pages.base_page import BasePage


class HomePage(BasePage):
    TOOLS = (By.CSS_SELECTOR, "main a.wp-block-button__link")

    @allure.step("Получить Automation Tools через Selenium")
    def automation_tools_text(self):
        self.open(HOME_URL)
        values = [e.text.strip() for e in self.driver.find_elements(*self.TOOLS)]
        values = [v for v in values if v]
        assert values, "Automation Tools is empty"
        return ", ".join(values)
