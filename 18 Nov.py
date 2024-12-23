from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


chrome_options = Options()
chrome_options.add_argument('--disable-notifications')

driver = WebDriver(chrome_options)
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://web-push-book.gauntface.com/demos/notification-examples/")
sleep(1)
push_notification = driver.find_element("xpath", "//input[@type='checkbox']")
push_notification.click()
sleep(1)
push_notification.click()
sleep(2)