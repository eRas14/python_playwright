from playwright.sync_api import Playwright, sync_playwright, expect

def sausedemo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=900)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("problem_use2r")  # лучше использовать fill вместо press_sequentially
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()  # добавлены скобки!

    # Правильная проверка видимости
    if page.locator(".error-message-container").is_visible():
        print("Неверный пароль")
    else:
        print("Успешный вход!")

    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        sausedemo(playwright)