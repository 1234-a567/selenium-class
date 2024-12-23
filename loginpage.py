from csv import excel
from sys import excepthook

from homepage import HomePage

class LoginPage(HomePage):
    email_textbox_locator = ("id", "Email")
    password_textbox_loactor = ("id", "Password")
    login_btn_locator = ("css selector", "input[value='Log in']")
    error_locator = ("xpath", "//span[contains(text(), 'unsuccessful')]")

    def enter_email(self, email):
        email_textbox = self.driver.find_element(*self.email_textbox_locator)
        email_textbox.send_keys(email)

    def enter_password(self, password):
        password_textbox = self.driver.find_element(*self.password_textbox_loactor)
        password_textbox.send_keys(password)

    def click_on_login_btn(self):
        login_btn = self.driver.find_element(*self.login_btn_locator)
        login_btn.click()

    def check_error_message(self):
        try:
            error = self.driver.find_element(*self.error_locator)
        except:
            return False
        else:
            return error.is_displayed()


