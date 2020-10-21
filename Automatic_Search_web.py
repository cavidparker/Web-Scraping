from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




driver = webdriver.Firefox()

driver.get("https://www.techwithtim.net/")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
# print(driver.page_source)



##  Wait untill go to next page : 
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "site-main"))

    )
    main.clear()
    print(main.text)
except:
    print("failed")
    driver.quit()

# main = driver.find_element_by_id("main")
print(main.text) 
