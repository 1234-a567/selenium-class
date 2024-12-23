from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver


driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://demoapps.qspiders.com/ui/modal?sublist=0")
sleep(1)
modal_button = driver.find_element("id", "modal1")
modal_button.click()
some_alert = driver.switch_to.alert
some_alert.dismiss()
sleep(2)

##############################################################
# driver.get("https://demoapps.qspiders.com/ui/alert/prompt?sublist=2")
# sleep(1)
# confirm_button = driver.find_element("id", "buttonAlert1")
# confirm_button.click()
# sleep(1)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.send_keys("yes")
# alert.accept()
# sleep(2)

################################################################
# driver.get("https://demoapps.qspiders.com/ui/alert?sublist=0")
# sleep(1)
# alert_button = driver.find_element("id", "buttonAlert2")
# alert_button.click()
# sleep(1)
# # info_alert = driver.switch_to.alert
# # info_alert.dismiss()
# sleep(2)
# ui_dropdown = driver.find_element("id", "options")
# ui_dropdown.click()
# sleep(2)