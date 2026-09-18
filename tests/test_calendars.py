from datetime import date
import re
import pytest
import allure
from pages.calendar_page import CalendarPage


@pytest.mark.positive
@allure.feature("Calendars")
class TestCalendarsPositive:
    def test_page_title(self, driver):
        p = CalendarPage(driver); p.open_page(); assert "Calendars" in driver.title

    def test_date_input_visible(self, driver):
        p = CalendarPage(driver); p.open_page(); assert p.visible(p.DATE).is_displayed()

    def test_picker_opens(self, driver):
        p = CalendarPage(driver); p.open_page(); assert p.open_picker().is_displayed()

    def test_month_is_displayed(self, driver):
        p = CalendarPage(driver); p.open_page(); p.open_picker(); assert p.month()

    def test_next_month_navigation(self, driver):
        p = CalendarPage(driver); p.open_page(); p.open_picker(); before = p.month(); p.clickable(p.NEXT).click(); assert p.month() != before

    def test_previous_month_navigation(self, driver):
        p = CalendarPage(driver); p.open_page(); p.open_picker(); before = p.month(); p.clickable(p.NEXT).click(); p.clickable(p.PREVIOUS).click(); assert p.month() == before

    def test_date_selected_through_calendar_ui(self, driver):
        p = CalendarPage(driver); p.open_page(); expected = p.select_today(); assert p.value() == expected

    def test_date_input_accepts_iso_value(self, driver):
        p = CalendarPage(driver); p.open_page(); p.enter(date.today().isoformat()); assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.value())


@pytest.mark.negative
@allure.feature("Calendars")
class TestCalendarsNegative:
    def test_non_iso_date_is_detected(self, driver):
        p = CalendarPage(driver); p.open_page(); p.enter("18/09/2026"); assert not re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.value())

    def test_impossible_date_is_not_a_real_date(self, driver):
        p = CalendarPage(driver); p.open_page(); p.enter("2026-02-30")
        with pytest.raises(ValueError): date.fromisoformat(p.value())

    def test_empty_date_is_empty_before_submit(self, driver):
        p = CalendarPage(driver); p.open_page(); assert p.value() == ""
