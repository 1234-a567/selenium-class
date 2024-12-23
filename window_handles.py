# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://seleniumssautomation.blogspot.com/")
# links=driver.find_elements("xpath","//a")
# actions=ActionChains(driver)
# actions.key_down(Keys.CONTROL).perform()
# for link in links:
#     link.click()
#     sleep(.5)
# target_file="Apple (India)"
# all_handles=driver.window_handles
# for handle in all_handles:
#     driver.switch_to.window(handle)
#     current_title=driver.title
#     sleep(1)
#     if current_title==target_file:
#         break
# contact=driver.find_element("link text","Contact Apple")
# contact.click()
# sleep(2)
##################################
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.ie.webdriver import WebDriver

from ActionChnage import driver

# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.instagram.com/")
# all_links=driver.find_elements("xpath","//footer//a")
# for link in all_links:
#     link.click()
#     sleep(.5)
# target_file="Terms of Use | Instagram Help Center"
# all_handles=driver.window_handles
# for handle in all_handles:
#     driver.switch_to.window(handle)
#     current_title=driver.title
#     sleep(1)
#     if current_title==target_file:
#         break
# sleep(3)
##FACEBOOK WINDOWS HANDLE
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.facebook.com/")
# all_links=driver.find_elements("xpath",'//a[@title="Browse our Facebook Services directory."]/../..//a')
# print(all_links)
# print(driver.current_window_handle)
# print(driver.current_url)
# actions=ActionChains(driver)
# actions.key_down(Keys.CONTROL).perform()
# for links in all_links:
#     links.click()
#     sleep(.5)
# all_handles=driver.window_handles
# print(all_handles)
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep






















































