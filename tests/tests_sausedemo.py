import allure
from selene import browser, have, be

from pages.saucedemo_page import LoginPage, MainPage, CartPage

login = LoginPage()
main = MainPage()
cart = CartPage()

@allure.title("Successful Login")
def test_successful_login(browser_setup):
    with allure.step("Открыть страницу сайта saucedemo"):
        login.open()
    with allure.step("Ввести данные для авторизации"):
        login.login('standard_user', 'secret_sauce')
    with allure.step("Убедимся, что пользователь вошёл в систему"):
        main.should_be_loaded()

@allure.title("Add Item to Cart")
def test_add_item_to_cart():
    with allure.step("Войти в приложение"):
        login.open().login('standard_user', 'secret_sauce')
    with allure.step("Добавить товар в корзину"):
        main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
    with allure.step("Подтвердить наличие товара в корзине"):
        cart.open_cart()
        browser.element('.title').should(have.text('Your Cart'))
        cart.should_contain_item('Sauce Labs Backpack')
    with allure.step("Проверить количество товара в корзине"):
        cart.should_have_items_count(1)


@allure.title("Navigation")
def test_navigation():
    with allure.step("Войти в приложение"):
        login.open().login('standard_user', 'secret_sauce')
    with allure.step("Открыть страницу «О нас» через меню"):
        main.open_about_page()
    with allure.step("Подтвердить открытие страницы"):
        browser.should(have.url_containing('saucelabs.com'))

@allure.title("Logout")
def test_logout():
    with allure.step("Войти в приложение"):
        login.open().login('standard_user', 'secret_sauce')
    with allure.step("Выполнить выход"):
        main.logout()
    with allure.step("Убедиться, что пользователь вышел из системы"):
        browser.element('#login-button').should(be.visible)

@allure.title("Failed Login")
def test_failed_login():
    with allure.step("Открыть страницу сайта saucedemo"):
        login.open()
    with allure.step("Ввести невалидные данные пользователя"):
        login.login('invalid_user', 'invalid_password')
    with allure.step("Убедиться, что отображается сообщение об ошибке"):
        login.should_have_error('Username and password do not match')

