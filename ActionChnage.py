# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver import ActionChains, Keys
# from time import sleep
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://seleniumssautomation.blogspot.com")
# fname1=driver.find_element("id","firstname").send_keys("anil kumar")
# action=ActionChains(driver)
# action.key_down(Keys.CONTROL).send_keys("a").send_keys("c")
# fname2=driver.find_element("name","  this text box is spam            ")
'''driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
fname=driver.find_element("id","input-firstname")
actions=ActionChains(driver)
actions.click(fname).send_keys("anil").send_keys(Keys.TAB).send_keys("kumar").send_keys(Keys.TAB).send_keys("anil@gmail.com").perform()
sleep((2))'''

# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import  sleep
# from selenium.webdriver import ActionChains, Keys
# driver1=WebDriver()
# driver1.get("https://testautomationpractice.blogspot.com/")
# driver1.maximize_window()
# sour=driver1.find_element("id","draggable")
# tar=driver1.find_element("id",'droppable')
# a1=ActionChains(driver1)
# a1.drag_and_drop(sour,tar).perform()
# sleep(3)
##right click
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import  sleep
from selenium.webdriver import ActionChains, Keys
driver1=WebDriver()
driver1.maximize_window()
driver1.implicitly_wait(10)
driver1.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

'''
'''from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
from time import  sleep
driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/")
uname=driver.find_element("xpath","//input[@type='text']")
pwd=driver.find_element("name","password")
login=driver.find_element("xpath","//input[@type='submit']")
ac=ActionChains(driver)
ac.send_keys_to_element(uname,"anilkumar").perform()
ac.send_keys_to_element(pwd,"dileep24863").perform()
ac.click(login).perform()
sleep(2)'''
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/selectable/#display-grid")
one=driver.find_element("xpath","//li[text()='1']")
two=driver.find_element("xpath","//li[text()='2']")
three=driver.find_element("xpath","//li[text()='3']")
four=driver.find_element("xpath","//li[text()='4']")
five=driver.find_element("xpath","//li[text()='5']")
ac=ActionChains(driver)
ac.click(one).perform()
ac.click(two).perform()
ac.click(three).perform()
ac.click(four).perform()
ac.click(five).perform()
sleep(2)'''
'''from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
ac=ActionChains(driver)
username=driver.find_element("id","name").send_keys("anilkumar")
ac.key_down(Keys.CONTROL).send_keys("c")'''
# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# from selenium.webdriver import ActionChains, Keys
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
'''driver.get("https://omayo.blogspot.com/")
ac=ActionChains(driver)
textfield=driver.find_element("id","ta1").send_keys("my name is anil")
ac.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL)
'''
'''driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
src=driver.find_element("xpath",'//img[@alt="The chalet at   the Green mountain lake"]')
tar=driver.find_element("id","trash")
ac=ActionChains(driver)
ac.drag_and_drop(src,tar).perform()
sleep(2)
'''
'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
fname=driver.find_element("id","name").send_keys("anilkumR")
ac=ActionChains(driver)
ac.click(fname).key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()
email=driver.find_element("id","email")
ac.click(email).key_down(Keys.CONTROL).send_keys("v").perform()
sleep(2)
0'''