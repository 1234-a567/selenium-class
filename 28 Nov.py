from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")
sleep(1)
third_column = driver.find_elements("xpath", "//table/tbody/tr/td[3]")
ages = [int(cell.text) for cell in third_column]
for age in ages:
    if age > 30:
        delete = driver.find_element("xpath", f"//table/tbody/tr/td[text()='{age}']/../td/a[2]")
        delete.click()

sleep(2)
2


############################################################################
# driver.get("https://demoapps.qspiders.com/ui/table?scenario=1")
# sleep(1)
# third_column = driver.find_elements("xpath", "//table/tbody/tr/td[2]")
# quantities = []
# for element in third_column:
#     quantity = int(element.text)
#     quantities.append(quantity)
#
# for quantity in quantities:
#     if quantity > 3:
#         name = driver.find_element("xpath", f"//table/tbody/tr/td[text()='{quantity}']/../th").text
#         print(name)
#
#
# sleep(2)