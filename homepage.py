from selenium.webdriver import ActionChains

from lib.library import Library


class HomePage(Library):
    register_link_locator = ("link text", "Register")
    login_link_locator = ("link text", "Log in")

    def click_on_register_link(self):
        register_link = self.driver.find_element(*self.register_link_locator)
        register_link.click()

    def click_on_login_link(self):
        login_link = self.driver.find_element(*self.login_link_locator)
        login_link.click()

    def hover_on_electronics(self):
        electronics = self.driver.find_element("xpath", "(//a[contains(text(),'Electronics')])[1]")
        actions = ActionChains(self.driver)
        actions.move_to_element(electronics).perform()

    def click_on_camera_photo_link(self):
        camera_photo = self.driver.find_element("xpath", "//ul[@class='sublist firstLevel active']/li/a[@href='/camera-photo']")
        camera_photo.click()

