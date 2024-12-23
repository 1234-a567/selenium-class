# from time import sleep
#
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = WebDriver()
# driver.implicitly_wait(10)
# sleep(1)
# driver.maximize_window()
# sleep(1)
# driver.get("https://www.bigbasket.com/")
# sleep(1)
# driver.

###############################################################
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

############################################################

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

driver  = WebDriver()
driver.implicitly_wait(15)
driver.maximize_window()
driver.get("https://tutorialsninja.com/")
link_website = driver.find_element("xpath","//a[text()='https://tutorialsninja.com/demo']")
link_website.click()
camera_link = driver.find_element("xpath","//a[text()='Cameras']")
camera_link.click()
chooseSort = 'Name (A - Z)'
# wait = WebDriverWait(driver,15)
# condition = expected_conditions.staleness_of(("xpath","//label[text()='Sort By:']/../select[@class='form-control'] "))
# option = wait.until(condition)
option = driver.find_element("xpath","//label[text()='Sort By:']/../select[@class='form-control']")
sortBysel = Select(option)
all_options = sortBysel.options
# print(opt)
for option in all_options:
    option_click = option.text
    if option_click == chooseSort:
        sortBysel.select_by_visible_text(option_click)
        break

# show webelement to pass the argument for the Select class
# show_options = driver.find_element("xpath","input-limit")
# show_sel = Select(show_options)
# for index in range(4):
#     if index == 3:
#         show_sel.select_by_index(index)

sleep(3)
