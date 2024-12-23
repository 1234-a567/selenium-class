from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(5)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("http://omayo.blogspot.com/")
textbox = driver.find_element("id", "ta1")
target_textbox = driver.find_element("xpath", "//textarea[contains(text(), 'garden')]")
actions = ActionChains(driver)
actions.click(textbox).send_keys("MARY HAD A LITLE LAMB LITTLE LAMB LITTLE LAMB").key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).click(target_textbox).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
sleep(2)
