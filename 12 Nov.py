from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://seleniumssautomation.blogspot.com/")
sleep(1)
links = driver.find_elements("xpath", "//a")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).perform()
for link in links:
    link.click()
    sleep(.5)
sleep(1000)


#############################################################
# sleep(1)
# parent_handle = driver.current_window_handle
# apple_link = driver.find_element("link text", "Apple")
# apple_link.click()
# current_handle = driver.current_window_handle
# print(parent_handle == current_handle)
# sleep(1)
# print(parent_handle)
# handles = driver.window_handles
# child_handle = handles[-1]
# print(handles)
# driver.switch_to.window(child_handle)
# contact_karo = driver.find_element("xpath", "//a[text()='Contact Apple']")
# contact_karo.click()
# sleep(3)



############################################################
# driver.get("https://ui.vision/demo/webtest/frames/")
# sleep(1)
# green_frame = driver.find_element("xpath", "(//frame)[2]")
# driver.switch_to.frame(green_frame)
# textbox1 = driver.find_element("css selector", "input[name='mytext2']")
# textbox1.send_keys("hello anna")
# driver.switch_to.default_content()
# sleep(1)
# yellow_frame = driver.find_element("xpath", "(//frame)[1]")
# driver.switch_to.frame(yellow_frame)
# textbox2 = driver.find_element("css selector", "input[name='mytext1']")
# textbox2.send_keys("how are you anna")
# driver.switch_to.default_content()
# sleep(1)
# gray_frame = driver.find_element("xpath", "(//frame)[4]")
# driver.switch_to.frame(gray_frame)
# textbox3 = driver.find_element("css selector", "input[name='mytext4']")
# textbox3.send_keys("bye anna")
# sleep(3)
