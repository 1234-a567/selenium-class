# import pytest
# from time import sleep
# from selenium.webdriver.chrome.webdriver import WebDriver
#
#
# @pytest.fixture()
# def setup_and_teardown():
#     global driver
#     driver = WebDriver()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get("https://demowebshop.tricentis.com/")
#     login_link = driver.find_element("link text", "Log in")
#     login_link.click()
#     yield
#     driver.quit()
# #
# def test_login_with_valid_creds(setup_and_teardown):
#     email_textbox = driver.find_element("id", "Email")
#     email_textbox.send_keys("reddyvinuth27@gmail.com")
#     password_textbox = driver.find_element("id", "Password")
#     password_textbox.send_keys("selenium")
#     login_btn = driver.find_element("css selector", "input[value='Log in']")
#     login_btn.click()
#     assert driver.find_element("xpath", "//span[contains(text(),'Login was unsuccessful')]").is_displayed()
#     # assert driver.find_element("xpath", "//a[text()='reddyvinuth27@gmail.com']").is_displayed()
# #
# # @pytest.mark.another
# # @pytest.mark.negative
# def test_login_with_invalid_cred(setup_and_teardown):
#     email_textbox = driver.find_element("id", "Email")
#     email_textbox.send_keys("reddyvinuth2777@gmail.com")
#     password_textbox = driver.find_element("id", "Password")
#     password_textbox.send_keys("selenium123")
#     login_btn = driver.find_element("css selector", "input[value='Log in']")
#     login_btn.click()
#     assert driver.find_element("xpath", "//span[contains(text(),'Login was unsuccessful')]").is_displayed()
#
# #
# passwords = ["123", "231", "213", "312", "321", "132", "111"]
# @pytest.mark.demo
# @pytest.mark.parametrize('password' ,passwords)
# def test_login_without_username(setup_and_teardown, password):
#     email_textbox = driver.find_element("id", "Email")
#     email_textbox.send_keys("")
#     password_textbox = driver.find_element("id", "Password")
#     password_textbox.send_keys(password)
#     login_btn = driver.find_element("css selector", "input[value='Log in']")
#     login_btn.click()
#
# #
# # @pytest.mark.negative
# # def test_login_without_password(setup_and_teardown, password):
# #     email_textbox = driver.find_element("id", "Email")
# #     email_textbox.send_keys("reddyvinuth27@gmail.com")
# #     password_textbox = driver.find_element("id", "Password")
# #     password_textbox.send_keys(password)
# #     login_btn = driver.find_element("css selector", "input[value='Log in']")
# #     login_btn.click()
# #
# # @pytest.mark.negative
# # def test_login_without_creds(setup_and_teardown, password):
# #     email_textbox = driver.find_element("id", "Email")
# #     email_textbox.send_keys("reddyvinuth27@gmail.com")
# #     password_textbox = driver.find_element("id", "Password")
# #     password_textbox.send_keys(password)
# #     login_btn = driver.find_element("css selector", "input[value='Log in']")
# #     login_btn.click()