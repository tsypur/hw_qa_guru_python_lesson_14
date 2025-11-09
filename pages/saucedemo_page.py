from selene import browser, have

class LoginPage:
    def open(self):
        browser.open('/')
        return self

    def login(self, username, password):
        browser.element('#user-name').type(username)
        browser.element('#password').type(password)
        browser.element('#login-button').click()
        return self



    def should_have_error(self, text):
        browser.element('[data-test="error"]').should(have.text(text))
        return self

class MainPage:
    def should_be_loaded(self):
        browser.element('.title').should(have.text('Products'))
        return self

    def add_item_to_cart(self, item_id):
        browser.element(f'#{item_id}').click()
        return self

    def open_about_page(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#about_sidebar_link').click()
        return self

    def logout(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#logout_sidebar_link').click()
        return self

class CartPage:

    def open_cart(self):
        browser.element('#shopping_cart_container').click()
        return self


    def should_contain_item(self, item_name):
        browser.element('.cart_item').should(have.text(item_name))
        return self

    def should_have_items_count(self, count):
        items = browser.all('.cart_item')
        items.should(have.size(count))
        return self