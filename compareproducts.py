from csv import excel
from sys import excepthook

from POM.homepage import HomePage


class CompareProductsPage(HomePage):
    def click_on_remove_of_camcorder(self):
        remove_btn = self.driver.find_element("xpath", "(//input[@value='Remove'])[1]")
        remove_btn.click()

    def click_on_remove_of_handycam(self):
        remove_btn = self.driver.find_element("xpath", "//input[@value='Remove']")
        remove_btn.click()

    def check_empty_status(self):
        try:
            empty_success = self.driver.find_element("xpath", "//div[contains(text(), 'no items to compare')]")
        except:
            return False
        else:
            return empty_success.is_displayed()
        

