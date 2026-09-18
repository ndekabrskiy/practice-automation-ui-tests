import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def is_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        return bool(elements and elements[0].is_displayed())
