
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    #Следующие три строки отвечают за запуск браузера и создание в нем контекста
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #запуск браузера chromium
    #headless=False - дает команду, чтобы браузер chromium отображался и был видимым при запуске кода. Ели вы установите True, то браузер не будет отображаться. Но при этом все записанные в коде действия сценария будут выполнены.

    context = browser.new_context()# Создает изолированный сеанс браузера.
    page = context.new_page()# Открывает новую страницу(tab) в браузере
    page.goto("https://demo.playwright.dev/todomvc/#/")# Метод чтобы открыть сайт
    page.get_by_role("textbox", name="What needs to be done?").click()# Находим атрибут в DOM дереве с тегом textbo и именем What needs to be done?" и кликаем
    page.get_by_role("textbox", name="What needs to be done?").fill("Создать первый сценарий playwright") #Этот метод вводит значения, переданные ему в качестве аргумента в веб-элемент. В нашем случае это текст  - "Создать первый сценарий playwright"
    page.get_by_role("textbox", name="What needs to be done?").press("ControlOrMeta+a")#Нажатие кнопки ENTER
  

    # ---------------------
    context.close()
    browser.close()

    #playwright codegen demo.playwright.dev/todomvc


with sync_playwright() as playwright:
    run(playwright)
