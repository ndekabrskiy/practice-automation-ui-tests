# Practice Automation UI Tests

Проект по ТЗ дисциплины «Автоматизация тестирования (Java, Python)».
Стек: Python 3.12+, Selenium, PyTest, Allure. Используется Page Object Model.

## Покрытие

Автоматизированы страницы Calendars, Modals и Ads. На каждой странице предусмотрены позитивные и негативные сценарии. Сценарий формы получает через Selenium список ссылок из Automation Tools и заполняет им поле Message.

## Запуск локально

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --alluredir=allure-results
```

Selenium Manager автоматически подберёт ChromeDriver. Переменные `BROWSER=firefox` и `HEADLESS=false` позволяют сменить браузер и режим.

## Allure

```bash
allure serve allure-results
```

При падении теста сохраняются screenshot и HTML страницы. GitHub Actions запускает тесты на push и pull request и сохраняет `allure-results` как artifact.
