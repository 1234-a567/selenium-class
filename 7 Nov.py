from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
sleep(1)
driver.implicitly_wait(10)
driver.maximize_window()
sleep(1)
driver.get("https://demoapps.qspiders.com/ui/frames/multiple?sublist=2")
sleep(1)
frame1 = driver.find_element("xpath", "(//iframe)[1]")
driver.switch_to.frame(frame1)
email = driver.find_element("id", "email")
email.send_keys("abc@123.com")
sleep(1)
password = driver.find_element("xpath", "//h2[text()='Sign Up']/..//input[@id='password']")
password.send_keys("123456")
confirm_password = driver.find_element("id", "confirm-password")
confirm_password.send_keys("123456")
sleep(1)
sign_up = driver.find_element("xpath", "//h2[text()='Sign Up']/..//button[@id='submitButton']")
sign_up.click()
sleep(1)
driver.switch_to.default_content()
frame2 = driver.find_element("xpath", "(//iframe)[2]")
driver.switch_to.frame(frame2)
sleep(1)
username = driver.find_element("id", "username")
username.send_keys("shazzy")
sleep(1)
password = driver.find_element("xpath", "//h2[text()='Login']/..//input[@id='password']")
password.send_keys("123456")
sleep(1)
login = driver.find_element("xpath", "//h2[text()='Login']/..//button[@id='submitButton']")
login.click()
sleep(3)


###############################################################
'''Only one iframe'''
# driver.get("https://demoapps.qspiders.com/ui/frames?sublist=0")
# sleep(1)
# iframe = driver.find_element("xpath", "//iframe")
# driver.switch_to.frame(iframe)
# username = driver.find_element("id", "username")
# username.send_keys("shashank")
# sleep(1)
# password = driver.find_element("id", "password")
# password.send_keys("123123123")
# sleep(1)
# login = driver.find_element("id", "submitButton")
# login.click()
# sleep(3)








