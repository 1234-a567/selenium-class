# # from selenium.webdriver import ActionChains, Keys
# # from selenium.webdriver.chrome.webdriver import WebDriver
# # from time import sleep
# # driver=WebDriver()
# # driver.maximize_window()
# # driver.implicitly_wait(10)
# # driver.get("https://www.flipkart.com/")
# # sleep(2)
# # ac=ActionChains(driver)
# # sleep(1)
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/button?sublist=0")
# ac=ActionChains(driver)
# left_click1=driver.find_element("id","btn")
# print(left_click1.text)
# ac.click(left_click1).perform()
# sleep(1)
# # right_click=driver.find_element("id","btn30")
# # ac.context_click(right_click).perform()
# # sleep(1)
# #
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/button?sublist=0")
# ac=ActionChains(driver)
# btn=driver.find_element("id","btn")
# ac.click(btn).perform()
# sleep(1)
# ac.key_down(Keys.CONTROL)
# driver.get("https://demoapps.qspiders.com/ui/button/buttonRight?sublist=1")
# btn_right=driver.find_element("id","btn30")
# ac.context_click(btn_right).perform()
# sleep(1)
##########explicity wait#######3
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/progress/element?sublist=2")
# time_textbox=driver.find_element("xpath",'(//input[@type="text"])[1]').send_keys("4")
# sleep(1)
# btn=driver.find_element("xpath",'//button[text()="Start"]').click()
# sleep(5)
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# driver=WebDriver()
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
# wait = WebDriverWait(driver, 15)
# wait.until(condition)
# pause_button.click()
# sleep(3

# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep



# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
#driver.get("https://omayo.blogspot.com/")
# alert_info=driver.find_element("id","alert1").click()
# sleep(1)
# al=driver.switch_to.alert
# al.dismiss()
#alert_conf=driver.find_element("id","confirm").click()
# promt_alert=driver.find_element("id","prompt").click()
# sleep(1)
# al=driver.switch_to.alert
# al.send_keys("anil")
# print(al.text)
# sleep(1)
# al.accept()
# sleep(1)
# driver.get("https://tutorialsninja.com/demo/")
# heart=driver.find_element("xpath","(//i)[4]").click()
# sleep(2)
# driver.get("http://127.0.0.1:5500/web/index.html")
# dropdown=driver.find_element("id","drop")
# s=Select(dropdown)
# s.select_by_index(2)
# for option in
#
# sleep(2)
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver. support.select import Select
from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# driver.implicitly_wait(10)
# moboile=driver.find_element("css selector",'img[alt="Mobiles"]').click()
#
# print(driver.name)
# print(driver.title)
# print(driver.current_url)
# print(driver.current_window_handle)
# driver.get_window_size()
# from  selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.get("")
# driver.implicitly_wait(10)
# driver.find_elements()
from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
#
# from web_elements import driver
# chrome_options=Options()
# chrome_options.add_experimental_option("pref",{"download_default-directory":r"C:\Users\Administrator\Desktop\selenium"})
# driver=WebDriver(chrome_options)
# driver.maximize_window()
# driver.get("https://ww1.naasongs.app/a/trending-new-hits-tollywood.html")
# download=driver.find_element("xpath",'(//a/span[text()=" Song Download "])[1]').click()
# driver.implicitly_wait(10)
# driver=WebDriver()
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.implicitly_wait(10)
#driver.find_element("id","singleFileInput").send_keys(r"C:\Users\Administrator\Desktop\python\homepage.py")

# headings=driver.find_elements("xpath","((//table)[1]/tbody/tr)[1]/th")
# count=0
# for heading in headings:
#     count+=1
#     print(heading.text)
# print(count)

# from selenium.webdriver.chrome.webdriver import WebDriver
# driver=WebDriver()
# driver.maximize_window()
# driver.get("https://demowebshop.tricentis.com/")
# driver.implicitly_wait(10)
# a=ActionChains(driver)
# web=driver.find_element("xpath",'//div/h3[text()="Customer service"]')
# #ind='(//table)[1]/tbody/tr/td[text()="India"]'
# #a.scroll_by_amount(0,300)
# #a.scroll_to_element()
# web1=driver.find_element("partial link text","Commerce")
# a.move_to_element(web1)
# a.perform()
# sleep(3)
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver import ActionChains
# driver=WebDriver()
# driver.get("https://demowebshop.tricentis.com/")
# ele=driver.find_element("id","small-searchterms")
# sa=ActionChains(driver)
# sa.send_keys("anilkuamr")
# print(sa.__dict__)

# print(s.__dict__)
# driver=WebDriver()
# items=driver.__dict__
# for item in  items :
#     print(item,end= "\n")

# cls=WebDriver.__dict__
# for item in cls:
#     print(item)
