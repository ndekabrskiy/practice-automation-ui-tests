import allure
import pytest
from selenium.webdriver.common.by import By
from pages.ads_page import AdsPage


@pytest.mark.positive
@allure.feature("Ads")
class TestAdsPositive:
    def test_page_title(self, driver):
        p = AdsPage(driver); p.open_page(); assert "Ads" in driver.title

    def test_countdown_text_visible(self, driver):
        p = AdsPage(driver); p.open_page(); assert "5" in driver.find_element(By.TAG_NAME, "body").text

    def test_ad_appears_after_countdown(self, driver):
        p = AdsPage(driver); p.open_page(); p.wait_for_ad(); assert p.is_visible(p.AD)

    def test_ad_has_expected_text(self, driver):
        p = AdsPage(driver); p.open_page(); p.wait_for_ad(); assert "ad" in p.text().lower()

    def test_ad_is_dialog(self, driver):
        p = AdsPage(driver); p.open_page(); p.wait_for_ad(); assert p.present(p.AD).get_attribute("role") == "dialog"

    def test_close_control_visible(self, driver):
        p = AdsPage(driver); p.open_page(); p.wait_for_ad(); assert p.visible(p.CLOSE).is_displayed()

    def test_ad_can_be_closed(self, driver):
        p = AdsPage(driver); p.open_page(); p.wait_for_ad(); p.close_ad(); assert not p.is_visible(p.AD)

    def test_url_remains_ads_page(self, driver):
        p = AdsPage(driver); p.open_page(); p.wait_for_ad(); p.close_ad(); assert driver.current_url.rstrip("/").endswith("/ads")


@pytest.mark.negative
@allure.feature("Ads")
class TestAdsNegative:
    def test_ad_hidden_before_countdown(self, driver):
        p = AdsPage(driver); p.open_page(); assert not p.is_visible(p.AD)

    def test_closed_ad_is_hidden(self, driver):
        p = AdsPage(driver); p.open_page(); p.wait_for_ad(); p.close_ad(); assert not p.is_visible(p.AD)

    def test_close_control_hidden_after_close(self, driver):
        p = AdsPage(driver); p.open_page(); p.wait_for_ad(); p.close_ad(); assert not p.is_visible(p.CLOSE)
