from POM.homepage import HomePage


class RegisterPage(HomePage):
    fname_textbox_locator = ("id", "FirstName")
    lname_textbox_locator = ("id", "LastName")
    email_textbox_locator = ("id", "Email")
    password_textbox_locator = ("id", "Password")
    confirm_textbox_locator = ("id", "ConfirmPassword")
    register_btn_locator = ("id", "register-button")
    register_success_locator = ("css selector", "input[value='Continue']")


    def enter_first_name(self, fname):
        fname_textbox = self.driver.find_element(*self.fname_textbox_locator)
        fname_textbox.send_keys(fname)

    def enter_last_name(self, lname):
        lname_textbox = self.driver.find_element(*self.lname_textbox_locator)
        lname_textbox.send_keys(lname)

    def enter_email(self, email):
        email_textbox = self.driver.find_element(*self.email_textbox_locator)
        email_textbox.send_keys(email)

    def enter_password(self, password):
        password_textbox = self.driver.find_element(*self.password_textbox_locator)
        password_textbox.send_keys(password)

    def enter_confirm_password(self, cpassword):
        confirm_textbox = self.driver.find_element(*self.confirm_textbox_locator)
        confirm_textbox.send_keys(cpassword)

    def click_on_register_btn(self):
        register_btn = self.driver.find_element(*self.register_btn_locator)
        register_btn.click()

    def check_register_success(self):
        try:
            continue_btn = self.driver.find_element(*self.register_success_locator)
            result = continue_btn.is_displayed()
        except:
            return False
        else:
            return result