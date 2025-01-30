import pytest
from POM.loginpage import LoginPage
from Tests.conftest import login_driver
from Utils.excelReader import get_data_from_excel, get_passwords_from_excel, get_emails_from_excel, get_invalid_data_from_excel

data = get_data_from_excel(r"C:\Users\shash\PycharmProjects\pytest_\Utils\demowebshopdata.xlsx", "valid_creds")
@pytest.mark.parametrize('username,password', data)
def test_login_with_valid_creds(login_driver,username,password):
    l1 = LoginPage(login_driver)
    l1.enter_email(username)
    l1.enter_password(password)
    l1.click_on_login_btn()
    if l1.check_error_message() == False:
        assert True
    else:
        assert False


passwords = get_passwords_from_excel(r"C:\Users\shash\PycharmProjects\pytest_\Utils\demowebshopdata.xlsx", "passwords")
@pytest.mark.parametrize("password", passwords)
def test_login_without_email(login_driver, password):
    l1 = LoginPage(login_driver)
    l1.click_on_login_link()
    l1.enter_email("")
    l1.enter_password(password)
    l1.click_on_login_btn()
    if l1.check_error_message() == False:
        assert True
    else:
        l1.grab_screenshot(password)
        assert False

emails = get_emails_from_excel(r"C:\Users\shash\PycharmProjects\pytest_\Utils\demowebshopdata.xlsx", "emails")
@pytest.mark.parametrize("email", emails)
def test_login_without_password(login_driver, email):
    l1 = LoginPage(login_driver)
    l1.click_on_login_link()
    l1.enter_email(email)
    l1.enter_password("")
    l1.click_on_login_btn()
    if l1.check_error_message() == True:
        assert True
    else:
        assert False


def test_login_without_creds():
    l1 = LoginPage()
    l1.click_on_login_link()
    l1.enter_email("")
    l1.enter_password("")
    l1.click_on_login_btn()
    if l1.check_error_message() == True:
        assert True
    else:
        assert False

invalid_creds = get_invalid_data_from_excel(r"C:\Users\shash\PycharmProjects\pytest_\Utils\demowebshopdata.xlsx", "invalid_creds")
@pytest.mark.parametrize("email,password", invalid_creds)
def test_login_with_invalid_creds(login_driver, email, password):
    l1 = LoginPage(login_driver)
    l1.click_on_login_link()
    l1.enter_email(email)
    l1.enter_password(password)
    l1.click_on_login_btn()
    if l1.check_error_message() == True:
        assert True
    else:
        assert False
