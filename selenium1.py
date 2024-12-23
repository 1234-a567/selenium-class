'''from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from selenium .webdriver.chrome.webdriver import WebDriver
from  time import sleep

'''
import time

''''''''
'''driver.get("https://omayo.blogspot.com")
sleep(1)
driver.maximize_window()
driver.implicitly_wait(10)
check_this=driver.find_element("xpath","//button[text()='Check this']")
check_this.click()
wait=WebDriverWait(driver,15)
condition=expected_conditions.element_to_be_clickable(("id","dte"))
check_this=wait.until(condition)
check_this.click()
sleep(3)'''
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/progress/element?sublist=2")
time=driver.find_element("xpath","//input [@placeholder='Enter time in seconds']").send_keys("3")
start=driver.find_element("xpath","//button[text()='Start']").click()
sleep(5)
'''
'''name=driver.find_element("id","name")
name.send_keys("anil kumar")
email=driver.find_element("id","email").send_keys("anil@gmail.com")
pwd=driver.find_element("id","password").send_keys("anil4863")
register=driver.find_element("xpath",'//button[text()="Register"]')
register.click()
sleep(5)
'''
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")
all=driver.find_element("id","searchDropdownBox")
listbox=Select(all)
listbox.select_by_index(11)
sleep(1)
search=driver.find_element("id","twotabsearchtextbox").send_keys("bikes")
driver.find_element('id',"nav-search-submit-button").click()
sleep(2)
'''
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/dropdown/multiSelect?sublist=1")
multiples_listbox=driver.find_element("id","select-multiple-native")
s1=Select(multiples_listbox)
print(s1.is_multiple)
all_options=s1.options
for option in all_options:
    text_of_the_element=option.text
    s1.select_by_visible_text(text_of_the_element)
    sleep(.5)
sleep(3)
'''
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.get("https://www.facebook.com/")
#
# links=driver.find_elements("xpath",'//a[text()="Facebook Lite"]/../..//a')
# driver.minimize_window()
# for link in links:
#     count=0
#     text_of_element=link.text
#     sleep(.3)
#     count+=1
# print(count)
# sleep(3)
###action chains
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver import ActionChains
driver=WebDriver()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)
actions=ActionChains(driver)
actions.scroll_by_amount(0,30)
sleep(3)
'''
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver import ActionChains
driver=WebDriver()
driver.maximize_window()
driver.get("https://www.worldometers.info/geography/alphabetical-list-of-countries/")
driver.implicitly_wait(10)
time.sleep(1)
actions=ActionChains(driver)
#ind=driver.find_element("xpath","//td[text()='India']")
actions.scroll_by_amount(0,60).perform()
sleep(2)'''



