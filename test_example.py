import re
from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.soccer.ru/news/1419705/vinisius-zhunior-real")
#     text = page.get_attribute("class", "examaple")
#     page.close()
#     print(text)
#     # ---------------------
#     context.close()
#     browser.close()

#flash 
# with sync_playwright() as playwright:
#     run(playwright)


def test_run(playwright: Playwright) -> None:
    clear = []
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    username = page.locator("#username").fill("tomsmith")
    password = page.locator("#password").fill("SuperSecretPassword!")
    page.locator(".fa-sign-in").click()
    text = page.locator("#flash").text_content().replace("×", "").strip()
    
    assert text == "Your username is invalid!"
    page.close()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
