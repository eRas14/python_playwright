from playwright.sync_api import Playwright, sync_playwright, expect
import time

def sausedemo_buy_something(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=900)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("problem_user")  # лучше использовать fill вместо press_sequentially
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()  # добавлены скобки!

    # Правильная проверка видимости
    if page.locator(".error-message-container").is_visible():
        print("Неверный пароль")
    else:
        print("Успешный вход!")

    #Собираем все заказы в список и преобразуем сразу в строку с маленькой буквы и заменяем пробелы -
    items_name = [item.replace(' ', '-').lower() for item in page.locator(".inventory_item_name").all_text_contents()]

    print(f"Всего заказов: {len(items_name)}")
    print(f"Последний заказ на странице: {items_name[-1]}")
    print(f"Список товаров: {items_name}")

    #Добавляем все заказы в корзину
    for item in range(len(items_name)-1):
        page.locator(f"#add-to-cart-{items_name[item]}").click()
        print (page.locator(f"#add-to-cart-{items_name[item]}"))
    
    page.locator(".shopping_cart_link").click()

    time.sleep(10)



    

    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        sausedemo_buy_something(playwright)