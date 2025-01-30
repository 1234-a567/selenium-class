from POM.homepage import HomePage


class ProductPage(HomePage):
    def click_on_email_friend(self):
        email_friend_btn = self.driver.find_element("css selector", "input[value='Email a friend']")
        email_friend_btn.click()

    def click_on_add_to_compare(self):
        add_to_compare_btn = self.driver.find_element("css selector", "input[value='Add to compare list']")
        add_to_compare_btn.click()

