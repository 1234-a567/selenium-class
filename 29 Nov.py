from idlelib.rpc import LOCALHOST
from plistlib import loads
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://ninjatables.com/examples-of-data-table-design-on-website/")
sleep(1)
sixth_column = driver.find_elements("xpath", "//table[@id='footable_17874']/tbody/tr/td[6]")

salaries = []
for cell in sixth_column:
    salary = cell.text
    salaries.append(salary)

locations = []
for salary in salaries:
    int_sal = int(salary.replace(",", ""))
    if int_sal > 200000:
        location = driver.find_element("xpath", f"//table[@id='footable_17874']/tbody/tr/td[text()='{salary}']/../td[4]").text
        locations.append(f"{salary} -> {location}")

print(locations)

sleep(2)