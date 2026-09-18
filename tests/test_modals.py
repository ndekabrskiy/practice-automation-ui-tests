import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.modals_page import ModalsPage


@pytest.mark.positive
@allure.feature("Modals")
class TestModalsPositive:
    def test_page_title(self, driver):
        p = ModalsPage(driver); p.open_page(); assert "Modals" in driver.title

    def test_simple_modal_opens(self, driver):
        p = ModalsPage(driver); p.open_page(); assert p.open_simple().is_displayed()

    def test_simple_modal_has_text(self, driver):
        p = ModalsPage(driver); p.open_page(); p.open_simple(); assert "simple modal" in p.visible((By.CSS_SELECTOR, "#pum-1318 .pum-content")).text.lower()

    def test_simple_modal_closes(self, driver):
        p = ModalsPage(driver); p.open_page(); p.open_simple(); driver.find_element(By.CSS_SELECTOR, "#pum-1318 .pum-close").click(); p.wait.until(EC.invisibility_of_element_located(p.SIMPLE)); assert not driver.find_element(*p.SIMPLE).is_displayed()

    def test_form_modal_opens(self, driver):
        p = ModalsPage(driver); p.open_page(); assert p.open_form().is_displayed()

    def test_form_name_field_visible(self, driver):
        p = ModalsPage(driver); p.open_page(); p.open_form(); assert p.visible(p.NAME).is_displayed()

    def test_form_email_field_visible(self, driver):
        p = ModalsPage(driver); p.open_page(); p.open_form(); assert p.visible(p.EMAIL).is_displayed()

    def test_form_accepts_valid_data(self, driver):
        p = ModalsPage(driver); p.open_page(); p.open_form(); p.fill(); assert p.valid(p.NAME) and p.valid(p.EMAIL)

    def test_message_uses_automation_tools(self, driver):
        tools = HomePage(driver).automation_tools_text(); p = ModalsPage(driver); p.open_page(); p.open_form(); p.fill(message=tools); assert p.message_value() and "," in tools


@pytest.mark.negative
@allure.feature("Modals")
class TestModalsNegative:
    def test_name_required(self, driver):
        p = ModalsPage(driver); p.open_page(); p.open_form(); p.fill(name="", email="valid@example.com"); assert not p.valid(p.NAME)

    def test_invalid_email_rejected(self, driver):
        p = ModalsPage(driver); p.open_page(); p.open_form(); p.fill(email="not-an-email"); assert not p.valid(p.EMAIL)

    def test_blank_form_is_invalid(self, driver):
        p = ModalsPage(driver); p.open_page(); p.open_form(); assert not p.valid(p.NAME)
