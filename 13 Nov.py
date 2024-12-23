from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.implicitly_wait(10)
sleep(1)
driver.maximize_window()
sleep(1)
driver.get("https://www.instagram.com/")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).perform()
links = driver.find_elements("xpath", "//footer//a")
for link in links:
    link.click()
    sleep(.5)

def go_to(target_title):
    target_title = "title of the page"
    all_handles = driver.window_handles
    for handle in all_handles:
        driver.switch_to.window(handle)
        current_title = driver.title
        sleep(.5)
        if current_title == target_title:
            break

threads_title = "Threads"
go_to(threads_title)
sleep(3)

meta_title = "Meta | Social Metaverse Company"
go_to(meta_title)
sleep(3)

help_title = "Help Center"
go_to(help_title)
sleep(3)


sleep(2)



###########################################################
# driver.get("https://seleniumssautomation.blogspot.com/")
# sleep(1)
# links = driver.find_elements("xpath", "//a")
# actions = ActionChains(driver)
# actions.key_down(Keys.CONTROL).perform()
# for link in links:
#     link.click()
#     sleep(.5)
#
# def go_to(target_title):
#     all_handles = driver.window_handles
#     for handle in all_handles:
#         driver.switch_to.window(handle)
#         current_title = driver.title
#         sleep(.5)
#         if current_title == target_title:
#             break
#
#
# apple_title = "Apple (India)"
# go_to(apple_title)
# sleep(2)
#
# facebook_title = "Facebook – log in or sign up"
# go_to(facebook_title)
# sleep(2)
#
# demo_Web_shop_title = "Demo Web Shop"
# go_to(demo_Web_shop_title)
# sleep(2)

