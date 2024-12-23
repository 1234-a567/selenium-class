from fnmatch import fnmatch
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
sleep(1)
fname_textbox = driver.find_element("id", "input-firstname")
actions = ActionChains(driver)
actions.click(fname_textbox).send_keys("Shashank").send_keys(Keys.TAB).send_keys("BG").send_keys(Keys.TAB).send_keys("abc@nonsense.com").send_keys(Keys.TAB).send_keys("0123456789").send_keys(Keys.TAB).send_keys("123412345").send_keys(Keys.TAB).send_keys("123412345").send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.SPACE).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
sleep(3)

############################################################
# driver.get("https://seleniumssautomation.blogspot.com/")
# sleep(1)
# fname_textbox1 = driver.find_element("id", "firstname")
# fname_textbox1.send_keys("I AM DISCO DANCER")
# fname_textbox2 = driver.find_element("name", "  this text box is spam               ")
# actions = ActionChains(driver)
#
# actions.key_down(Keys.CONTROL).send_keys('a').send_keys("c").key_up(Keys.CONTROL).click(fname_textbox2).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# sleep(3)