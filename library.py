class Library:
    def __init__(self, driver):
        self.driver = driver

    def grab_screenshot(self, name):
        self.driver.save_screenshot(rf"C:\Users\shash\PycharmProjects\pytest_\screenshots\{name}.png")

    def click_on_back_2_times(self):
        self.driver.back()
        self.driver.back()
