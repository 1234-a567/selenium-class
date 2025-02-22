from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
'''Nested with multiple'''
driver.get("https://demoapps.qspiders.com/ui/frames/nestedWithMultiple?sublist=3")
sleep(1)
grandpa_frame = driver.find_element("xpath", "//section[@id='demoUI']//iframe")
driver.switch_to.frame(grandpa_frame)
parentFrame = driver.find_element("xpath", "//p[contains(text(),'Note')]/../..//iframe")
driver.switch_to.frame(parentFrame)
child1_frame = driver.find_element("xpath", "(//h2[text()='Login']/..//iframe)[1]")
driver.switch_to.frame(child1_frame)
email = driver.find_element("id", "email")
email.send_keys("the_undertaker@rip.com")
sleep(1)
driver.switch_to.parent_frame()
child2_frame = driver.find_element("xpath", "(//h2[text()='Login']/..//iframe)[2]")
driver.switch_to.frame(child2_frame)
password = driver.find_element("id", "password")
password.send_keys("choke slam")
sleep(1)
driver.switch_to.parent_frame()
child3_frame = driver.find_element("xpath", "(//h2[text()='Login']/..//iframe)[3]")
driver.switch_to.frame(child3_frame)
confirm_password = driver.find_element("id", "confirm")
confirm_password.send_keys("choke slam")
sleep(1)
driver.switch_to.parent_frame()
child4_frame = driver.find_element("xpath", "(//h2[text()='Login']/..//iframe)[4]")
driver.switch_to.frame(child4_frame)
submit = driver.find_element("id", "submitButton")
submit.click()
sleep(1)
driver.switch_to.default_content()
ui_button = driver.find_element("id", "options")
ui_button.click()
sleep(3)


###############################################################
'''Nested'''
# driver.get("https://demoapps.qspiders.com/ui/frames/nested?sublist=1")
# sleep(1)
# parent_frame = driver.find_element("xpath", "//section[@id='demoUI']//iframe")
# driver.switch_to.frame(parent_frame)
# child_frame = driver.find_element("xpath", "//section[@class='main_form_container']//iframe")
# driver.switch_to.frame(child_frame)
# email = driver.find_element("id", "email")
# email.send_keys("randy_orton@wwe.com")
# sleep(1)
# password = driver.find_element("id", "password")
# password.send_keys("rko")
# sleep(1)
# confirm_password = driver.find_element("id", "confirm-password")
# confirm_password.send_keys("rko")
# sleep(1)
# submit = driver.find_element("id", "submitButton")
# submit.click()
# sleep(1)
# driver.switch_to.default_content()
# ui_button = driver.find_element("id", "options")
# ui_button.click()
# sleep(2)