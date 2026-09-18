import re
from pathlib import Path
import allure
import pytest
from utils.driver_factory import create_driver

@pytest.fixture()
def driver():
    browser = create_driver()
    browser.set_page_load_timeout(45)
    yield browser
    browser.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and "driver" in item.funcargs:
        folder = Path("screenshots"); folder.mkdir(exist_ok=True)
        filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid) + ".png"
        path = folder / filename
        item.funcargs["driver"].save_screenshot(str(path))
        allure.attach.file(str(path), name="Скриншот ошибки", attachment_type=allure.attachment_type.PNG)
        allure.attach(item.funcargs["driver"].page_source, name="HTML страницы", attachment_type=allure.attachment_type.HTML)
