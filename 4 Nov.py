from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(15)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://omayo.blogspot.com/")
sleep(1)
double_click = driver.find_element("xpath", "//button[text()=' Double click Here   ']")
actions = ActionChains(driver)
# actions.double_click(double_click).perform()
# actions.context_click(double_click).perform()

try_it = driver.find_element("xpath", "//button[text()='Try it']")
actions = ActionChains(driver)
# actions.scroll_by_amount(0, 500).perform()
# actions.scroll_to_element(try_it).perform()
username = driver.find_element("name", "userid")
actions.click(username).send_keys("shazzy").perform()


sleep(3)


#################################################################
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")
# sleep(1)
# oslo = driver.find_element("id", "box1")
# norway = driver.find_element("id", "box101")
# actions = ActionChains(driver)
# actions.click_and_hold(oslo).move_to_element(norway).release().perform()
# # actions.drag_and_drop(oslo, norway).perform()
# sleep(1)
# link = driver.find_element("xpath", "//a[contains(text(), 'DHTMLGoodies')]")
# actions.click(link).perform()
#
# sleep(3)

###########################################################
# sleep(1)
# driver.get("https://www.myntra.com/")
# sleep(1)
# men_link = driver.find_element("xpath", "//a[@href='/']/../../..//a[@href='/shop/men']")
# actions = ActionChains(driver)
# actions.move_to_element(men_link).perform()
# sleep(3)