'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/frames?sublist=0")
iframe=driver.find_element("xpath","//iframe")
driver.switch_to.frame(iframe)
username=driver.find_element("id","username").send_keys("anilkumar").
password=driver.find_element("id","password").send_keys("anil@4863")
login=driver.find_element("id","submitButton").click()
sleep(2)'''
from selenium.webdriver import ActionChains, Keys

'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/frames/multiple?sublist=2")
frame1=driver.find_element("xpath","(//iframe)[1]")
driver.switch_to.frame(frame1)
email=driver.find_element("id","email").send_keys("anil@gmail.com")
sleep(1)
pwd=driver.find_element("id","password").send_keys("anil@4863")
sleep(1)
c_pwd=driver.find_element("id","confirm-password").send_keys("anil@4863")
sleep(1)
signup=driver.find_element("id","submitButton").click()
sleep(2)
driver.switch_to.default_content()
iframe2=driver.find_element("xpath","(//iframe)[2]")
driver.switch_to.frame(iframe2)
username=driver.find_element("id","username").send_keys("anilkumar")
sleep(1)
password=driver.find_element("id","password").send_keys("anil@4863")
sleep(1)
login=driver.find_element("id","submitButton").click()
sleep(2)'''
##########3nested iframe#################
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import  sleep
driver=WebDriver()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui/frames/nested?sublist=1")
sleep(1)
parent=driver.find_element("xpath","//section[@id='demoUI']//iframe")
driver.switch_to.frame(parent)
child=driver.find_element("xpath","//section[@class='main_form_container']//iframe")
driver.switch_to.frame(child)
email=driver.find_element("id","email").send_keys("anil@gmail.com")
pwd=driver.find_element("id","password").send_keys("anil4863")
confirm_pwd=driver.find_element("id","confirm-password").send_keys'''
######nested multiple iframe########
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://demoapps.qspiders.com/ui/frames/nestedWithMultiple?sublist=3")
#
# main=driver.find_element("xpath",'//section[@id="demoUI"]//iframe')
# driver.switch_to.frame(main)
#
# main1=driver.find_element("xpath",'(//h2[text()="Login"]/..//iframe)[1]')
# driver.switch_to.frame(main1)
# email=driver.find_element("id","email").send_keys("anil@gmail\.com")
# sleep(1)
#
# main2=driver.find_element("xpath",'(//h2[text()="Login"]/..//iframe)[2]')
# driver.switch_to.frame(main2)
# email=driver.find_element("id","email").send_keys("anil@gmail\.com")
# sleep(1)
#
# main3=driver.find_element("xpath",'(//h2[text()="Login"]/..//iframe)[3]')
# driver.switch_to.frame(main3)
# pwd=driver.find_element("id","password").send_keys("anil4863")
# sleep(1)
#
# main4=driver.find_element("xpath",'(//h2[text()="Login"]/..//iframe)[4]')
# driver.switch_to.frame(main4)
# con_pwd=driver.find_element("id","confirm").send_keys("anil4863")
# sleep(1)
#
# main5=driver.find_element("xpath",'(//h2[text()="Login"]/..//iframe)[5]')
# driver.switch_to.frame(main5)
# button=driver.find_element("id","submitButton").click()
# sleep(1)
###########frames##########3
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://ui.vision/demo/webtest/frames/")
# frame_green=driver.find_element("xpath","(//frame)[2]")
# driver.switch_to.frame(frame_green)
# green_textbox=driver.find_element("xpath",'//input[@name="mytext1"]').send_keys("anil kumar")
# driver.switch_to.default_content()
# sleep(1)
#
# frame_yellow=driver.find_element("xpath","(//frame)[1]")
# driver.switch_to.frame(frame_yellow)
# yellow_textbox=driver.find_element("xpath",'//input[@name="mytext1"]').send_keys("anil kumar")
# driver.switch_to.default_content()
# sleep(1)
#
# frame_grey=driver.find_element("xpath","(//frame)[4]")
# driver.switch_to.frame(frame_grey)
# grey_textbox=driver.find_element("xpath",'(//frame)[4]').send_keys("anil kumar")
# driver.switch_to.default_content()
# sleep(1)
#
# blue=driver.find_element("xpath","(//frame)[3]")
# driver.switch_to.frame(blue)
















