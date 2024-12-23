# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.implicitly_wait(10)
# driver.maximize_window()
#driver.get("https://demoapps.qspiders.com/ui/datePick?sublist=0")

# months={
#     "January":1,
#     "February":2,
#     "March":3,
#     "April":4,
#     "May":5,
#     "June":6,
#     "July":7,
#     "August":8,
#     "September":9,
#     "October":10,
#     "November":11,
#     "December":12

# month_element=driver.find_element("xpath",'//div[text()="November 2024"]')
# previous_btn=driver.find_element("xpath",'(//button[@type="button"])[1]')
# next_btn=driver.find_element("xpath",'//span[text()="Next Month"]')
# target_month="May"
# while True:
#     current_month=month_element.text.split()[0]
#     if current_month==target_month:
#         break
#     if months[target_month]<months[current_month]:
#         previous_btn.click()
#     else:
#         next_btn.click()
#     sleep(.5)

# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.implicitly_wait(10)
# driver.maximize_window()
#
# #driver.get("https://demoapps.qspiders.com/ui/datePick?sublist=0")
# #date_area=driver.find_element("xpath",'//input[@placeholder="Select A Date"]').send_keys("07/06/2003")
# # previous_btn=driver.find_element("xpath",'//span[text()="Previous Month"]').click()
# # sleep(2)
# driver.get("https://demoapps.qspiders.com/ui/datePick?sublist=0&scenario=4")
# input=driver.find_element("xpath",'//input[@placeholder="Select A Date"]').click()
# # date=driver.find_element("xpath",'//div[text()="13"]').click()
# next_btn=driver.find_element("xpath",'//div//button//span[text()="Next Month"]').click()
# sleep(1)
# date=driver.find_element("xpath",'//div[text()="23"]').click()
# sleep(2)
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/datePick?sublist=0&scenario=1")
# driver.find_element("xpath",'//input[@type="text"]'v).click()
# previous_btn=driver.find_element("xpath",'//div//button//span[text()="Previous Month"]').click()
# sleep
#
# departure_btn=driver.find_element("xpath",'//span[text()="Departure"]').click()
# next_button=driver.find_element("xpath",'//span[@aria-label="Next Month"]')
# prev_btn=driver.find_element("xpath",'//span[@aria-label="Previous Month"]')
# month_year=driver.find_element("xpath",'')
# from time import sleep
# from selenium.webdriver.chrome.webdriver import WebDriver
#
# driver = WebDriver()
# driver.implicitly_wait(10)
# sleep(1)
# driver.maximize_window()
# sleep(1)
# driver.get("https://www.makemytrip.com/")
# sleep(1)
# close_modal_btn = driver.find_element("css selector", "span[class='commonModal__close']")
# close_modal_btn.click()
# sleep(1)
# months = {"January" : 1,
#           "February" : 2,
#           "March" : 3,
#           "April" : 4,
#           "May" : 5,
#           "June" : 6,
#           "July" : 7,
#           "August" : 8,
#           "September" : 9,
#           "October" : 10,
#           "November" : 11,
#           "December" : 12
#           }
#
# def select_date_from_departure(target_date, target_month, target_year):
# #     from_calendar_btn = driver.find_element("xpath", "//span[text()='Departure']")
# #     from_calendar_btn.click()
# #     next_btn = driver.find_element("xpath", "//span[@aria-label='Next Month']")
# #     while True:
# #         current_month_year = driver.find_element("xpath", "(//div[@class='DayPicker-Caption'])[1]/div").text
# #         current_month = current_month_year.split()[0]
# #         current_year = int(current_month_year.split()[-1])
# #         if current_year == target_year and current_month == target_month:
# #             driver.find_element("xpath", f"(//div[@class='DayPicker-Body'])[1]//div/p[text()='{target_date}']").click()
# #             break
# #         elif current_year < target_year:
# #             next_btn.click()
# #         elif months[current_month] < months[target_month]:
# #             next_btn.click()





