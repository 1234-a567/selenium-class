
'''from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.support.select import Select

driver=WebDriver()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
country_listbox=driver.find_element("id","select3")
s=Select(country_listbox)'''

#s.select_by_index(3)
#s.select_by_value("India")
#s.select_by_visible_text("United Arab Emirates")
#sleep(5)

#from selenium.webdriver.chrome.webdriver import WebDriver
'''from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
driver=WebDriver()'''
#driver.get("https://tutorialsninja.com/demo")
#multiple_listbox=driver.find_element("id","multiple_cars")
#s=Select(multiple_listbox)
'''for index in range(10):
    s.select_by_index(index)  
    sleep(.5)'''
'''s.select_by_index(0)
sleep(.5)
s.select_by_index(1)
sleep(.5)
s.select_by_index(3)
s.deselect_by_index(1)
sleep(5)
'''
'''all_options=s.options
for option in all_options:
    text_of_the_element=option.text
    s.select_by_visible_text(text_of_the_element)
    sleep(.5)
print(s.first_selected_option)
print(s.all_selected_options)
'''
'''camera=driver.find_element("xpath",'//a[text()="Cameras"]')
camera.click()
sort=driver.find_element("id","input-sort")
s1=Select(sort)
s1.select_by_index(1)
sleep(.5)
sleep(5)


value=driver.find_element("id","input-limit")
s2=Select(value)
s2.select_by_index(1)
sleep(2)
print(s2.is_multiple)
sleep(2)'''
'''driver.get("https://practice.expandtesting.com/dropdown")
simple=driver.find_element('id','dropdown')
s3=Select(simple)
s3.select_by_index(1)
sleep(1)
print(s3.is_multiple)
sleep(3)
'''
'''from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
driver=WebDriver()
#driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/dropdown/multiSelect?sublist=1")
multiple_listbox=driver.find_element("id","select-multiple-native")
s1=Select(multiple_listbox)
s1.select_by_index(1)
sleep(1)
s1.select_by_index(2)
sleep(3)'''
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.select import Select
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.britannica.com/science/geography")
# all=driver.find_element("xpath","//a[text()='Thailand']/../../../../../../..//a")
# s=Select(all)
# all_tags=s.options
# for tag in all_tags:
#     text_of_the_element = tag.text
#     s.select_by_visible_text(text_of_the_element)
#     sleep(.5)
# driver.minimize_window()
# sleep(2)

# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from time import sleep
# driver=WebDriver()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://demoapps.qspiders.com/ui/progress/element?sublist=2")
# sleep(1)
# textbox = driver.find_element("xpath", "//input[@placeholder='Enter time in seconds']")
# textbox.send_keys("6")
# sleep(1)
# start_button = driver.find_element("xpath", "//button[text()='Start']")
# start_button.click()
#
#
# pause_button = driver.find_element("xpath", "//button[text()='Pause']")
# condition = expected_conditions.visibility_of_element_located(("xpath", "//span[text()='70%']"))
# wait = WebDriverWait(driver, 15, poll_frequency=0.001)
# wait.until(condition)
# pause_button.click()
# sleep(3)





















