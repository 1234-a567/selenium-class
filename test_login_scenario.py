from loginpage import LoginPage


def test_login_with_valid_creds():
    l1 = LoginPage()
    l1.click_on_login_link()
    l1.enter_email("reddyvinuth27@gmail.com")
    l1.enter_password("selenium")
    l1.click_on_login_btn()
    if l1.check_error_message() == False:
        assert True
    else:
        assert False


def test_login_without_email():
    l1 = LoginPage()
    l1.click_on_login_link()
    l1.enter_email("")
    l1.enter_password("selenium")
    l1.click_on_login_btn()
    if l1.check_error_message() == True:
        assert True
    else:
        assert False

def test_login_without_password():
    l1 = LoginPage()
    l1.click_on_login_link()
    l1.enter_email("reddyvinuth27@gmail.com")
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


def test_login_with_invalid_creds():
    l1 = LoginPage()
    l1.click_on_login_link()
    l1.enter_email("reddyvinuth@gmail.com")
    l1.enter_password("selenium1234")
    l1.click_on_login_btn()
    if l1.check_error_message() == True:
        assert True
    else:
        assert False
