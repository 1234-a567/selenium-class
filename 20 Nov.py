from time import sleep
from types import new_class

from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://demoapps.qspiders.com/ui/datePick?sublist=0")
sleep(1)
calender_btn = driver.find_element("css selector", "input[placeholder='Select A Date']")
calender_btn.click()
sleep(1)

def select_future_date(target_month, target_date):
    next_btn = driver.find_element("css selector", "button[aria-label='Next Month']")
    month_element = driver.find_element("css selector", "div[class='react-datepicker__current-month']")
    while True:
        current_month = month_element.text
        if current_month == target_month:
            break
        next_btn.click()
        sleep(.5)

    date = driver.find_element("xpath", f"//div[@class='react-datepicker__month-container']//div[text()='{target_date}']")
    date.click()



def select_past_date(target_month, target_date):
    previous_btn = driver.find_element("css selector", "button[aria-label='Previous Month']")
    month_element = driver.find_element("css selector", "div[class='react-datepicker__current-month']")
    while True:
        current_month = month_element.text
        if current_month == target_month:
            break
        previous_btn.click()
        sleep(.5)

    date = driver.find_element("xpath", f"//div[@class='react-datepicker__month-container']//div[text()='{target_date}']")
    date.click()

# select_future_date("October 2025", 15)
# select_past_date("October 2020", 15)
sleep(2)

months = {"January" : 1,
          "February" : 2,
          "March" : 3,
          "April" : 4,
          "May" : 5,
          "June" : 6,
          "July" : 7,
          "August" : 8,
          "September" : 9,
          "October" : 10,
          "November" : 11,
          "December" : 12
          }
target_month = "December"
target_date = 12
target_year = 2022

next_btn = driver.find_element("css selector", "button[aria-label='Next Month']")
previous_btn = driver.find_element("css selector", "button[aria-label='Previous Month']")
month_element = driver.find_element("css selector", "div[class='react-datepicker__current-month']")
def choose_any_date(target_date:int, target_month:str, target_year:int=2024):
    while True:
        current_month = month_element.text.split()[0]
        current_year = int(month_element.text.split()[1])
        if current_month == target_month and current_year == target_year:
            break
        if current_year > target_year:
            previous_btn.click()
        elif current_year < target_year:
            next_btn.click()
        elif months[current_month] < months[target_month]:
            next_btn.click()
        else:
            previous_btn.click()
    date = driver.find_element("xpath",f"//div[@class='react-datepicker__month-container']//div[text()='{target_date}']")
    date.click()


choose_any_date(20, "May", 2019)
sleep(2)




























