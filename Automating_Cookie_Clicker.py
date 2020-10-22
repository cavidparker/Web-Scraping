from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Loading for the page 
driver.implicitly_wait(5)


cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

# Load them in a list:
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

action = ActionChains(driver)
action.click(cookie)

for i in range(5000):
    action.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgade_actions = ActionChains(driver)
            upgade_actions.move_to_element(item)
            upgade_actions.click()
            upgade_actions.perform()
    
    print(count)
    
