# from selenium import ActionChains
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/alert/confirm?sublist=1")
# #alert_button=driver.find_element("id","buttonAlert2").click()
# # promt_button=driver.find_element("id","buttonAlert1").click()
# button=driver.find_element("id","buttonAlert5").click()
# alert=driver.switch_to.alert
# sleep(1)
# print(alert.text)
# alert.dismiss()
# sleep(1)
# # alert.send_keys("yes")
# # alert.accept()
# #alert.dismiss()
# #alert.accept()
#
# # dropdeown=driver.find_element("id","options").click()
# sleep(2)
###webpush book notifications cramples
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# chrome_options=Options()
# chrome_options.add_argument("--disable-notifications")
# driver=WebDriver(chrome_options)
# driver.maximize_window()
# driver.get("https://web-push-book.gauntface.com/demos/notification-examples/")
# btn=driver.find_element("xpath",'//input[@type="checkbox"]').click()
# sleep(2)
##########cookies#
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
#driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://kodakco.com/")
# cross=driver.find_element("id","closeButton").click()
# sleep(2)
###############3
# driver.get("https://online.kfc.co.in/")
# set_locaton=driver.find_element("xpath",'//button[text()="Set Location"]').click()
# sleep(5)

# def sum(a,b):
#     return tuple (a+b)
# var=sum(10,20)
# print(var)
#
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
#
# from selenium.webdriver.support.select import Select
#
# driver=WebDriver()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://demoapps.qspiders.com/ui/dropdown")
# number=driver.find_element("id","select1")
# s=Select(number)
# s.select_by_index(3)
# sleep(1)
# s.select_by_value("+44")
# all=s.options
# s.select_by_visible_text("+91")
# print(all)
# for option in all:
#     print(type(all))
#     text=option.text
#     print(text)
#     sleep(.5)
# print(s.is_multiple)
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/dropdown")
# all=driver.find_elements("xpath","//a")
# driver.minimize_window()
# for item in all:
#     print(item.text,sep="@  ",end=" ")
#     sleep(.5)

from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/auth?sublist=0")
btn=driver.find_element("id","AuthLink").click()
child_handle=driver.window_handles[-1]
driver.switch_to.window(child_handle)


