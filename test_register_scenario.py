import pytest

from POM.loginpage import LoginPage
from POM.registerpage import RegisterPage

def test_register_and_login(register_driver):
    register = RegisterPage(register_driver)
    register.enter_first_name("paine12")
    register.enter_last_name("johnson")
    register.enter_email("paper@scissor12.com")
    register.enter_password("pebble")
    register.enter_confirm_password("pebble")
    register.click_on_register_btn()
    # if register.check_register_success() == True:
    #     assert True
    # else:
    #     assert False
    l1 = LoginPage(register_driver)
    l1.click_on_login_link()
    l1.enter_email("paper@scissor12.com")
    l1.enter_password("pebble")
    l1.click_on_login_btn()
    if l1.check_error_message() == False:
        assert True
    else:
        assert False


