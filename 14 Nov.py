from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://omayo.blogspot.com/")
sleep(1)
textarea = driver.find_element("xpath", "//textarea[contains(text(),'playing')]")
actions = ActionChains(driver)
actions.click(textarea).send_keys("hello").perform()
sleep(1)
actions.key_down(Keys.BACKSPACE).key_down(Keys.BACKSPACE).key_down(Keys.BACKSPACE).perform()
# textarea.clear()
sleep(3)
# sleep(1)
# driver.get("https://demowebshop.tricentis.com/")
# sleep(1)
#
# register = driver.find_element("link text", "Register")
# print(register.text)
# sleep(3)
# register.screenshot("register.png")
#
# print(register.get_attribute('href'))
# print(register.size)
# print(register.tag_name)
# print(register.location)
# register.
