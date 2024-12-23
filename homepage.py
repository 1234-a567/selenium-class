from selenium.webdriver.chrome.webdriver import WebDriver


class HomePage:
    register_link_locator = ("link text", "Register")
    login_link_locator = ("link text", "Log in")

    def __init__(self):
        self.driver = WebDriver()
        self.driver.maximize_window()
        self.driver.get("https://demowebshop.tricentis.com/")

    def click_on_register_link(self):
        register_link = self.driver.find_element(*self.register_link_locator)
        register_link.click()

    def click_on_login_link(self):
        login_link = self.driver.find_element(*self.login_link_locator)
        login_link.click()
