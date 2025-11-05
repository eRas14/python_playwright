
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.only_browser("firefox")
def test_add_todo(page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("Создать первый сценарий playwright") 
    page.get_by_role("textbox", name="What needs to be done?").press("ControlOrMeta+a")



# def test_add_todo(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demo.playwright.dev/todomvc/#/")
#     page.get_by_role("textbox", name="What needs to be done?").click()
#     page.get_by_role("textbox", name="What needs to be done?").fill("Создать первый сценарий playwright") 
#     page.get_by_role("textbox", name="What needs to be done?").press("ControlOrMeta+a")

#     context.close()
#     browser.close()

    #playwright codegen demo.playwright.dev/todomvc


# with sync_playwright() as playwright:
#     run(playwright)


# Проще говоря:

# •  Browser: Какой браузер использовать (Chrome, Firefox, etc.)
# •  Browser Context: Как "настроить" этот браузер (режим инкогнито, профиль с куками, etc.)
# •  Page: Что именно ты делаешь на конкретной странице сайта.