from selenium.webdriver.support.select import Select

from POM.homepage import HomePage


class CameraPhotoPage(HomePage):
    def sort_by_listbox(self, text):
        select_obj1 = Select(self.driver)
        select_obj1.select_by_visible_text(text)

    def display_listbox(self, text):
        select_obj2 = Select(self.driver)
        select_obj2.select_by_visible_text(text)

    def view_as_listbox(self, text):
        select_obj2 = Select(self.driver)
        select_obj2.select_by_visible_text(text)

    def click_on_1MP_60GB_HD(self):
        product_link = self.driver.find_element("xpath", "//h2/a[@href='/hard-drive-handycam-camcorder']")
        product_link.click()

    def click_on_camcorder(self):
        camcorder_link = self.driver.find_element("xpath", "//h2/a[@href='/camcorder']")
        camcorder_link.click()

