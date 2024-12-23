from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = WebDriver(chrome_options)
driver.implicitly_wait(10)
sleep(1)
parent_handle = driver.current_window_handle
driver.maximize_window()
sleep(1)
driver.get("https://demoapps.qspiders.com/ui/auth?sublist=0")
sleep(1)
alert_btn = driver.find_element("id", "AuthLink")
alert_btn.click()
sleep(1)
child_handle = driver.window_handles[-1]

driver.switch_to.window(child_handle)
sleep(1)
active_url = driver.current_url.replace("//", "//admin:admin@")
print(active_url)
driver.get(active_url)
sleep(1)

