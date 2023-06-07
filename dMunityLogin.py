
# from typing import KeysView
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

# driver_path = 'path/to/chromedriver'

# driver = webdriver.Chrome(executable_path=driver_path)
    
# driver.get('https://dmunity.com/')
# time.sleep(2)
# driver.maximize_window()

# time.sleep(5)
# driver.find_element(By.CLASS_NAME,"me-3.d-none.d-lg-block.btn.btn-primary").click()
# time.sleep(5)
# driver.find_element(By.ID,":r0:").send_keys("admin@dmunity.com")
# driver.find_element(By.ID,":r1:").send_keys("123456")
# driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div/div/div/div[1]/div/div/div/form/button').click()
# time.sleep(5)

# # from the admin login codes are working fine 


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def login(driver, email, password):
    driver.find_element(By.CLASS_NAME, "me-3.d-none.d-lg-block.btn.btn-primary").click()
    time.sleep(5)
    driver.find_element(By.ID, ":r0:").send_keys(email)
    driver.find_element(By.ID, ":r1:").send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[1]/div/div/div/form/button').click()
    time.sleep(5)

# Create and set up the WebDriver
driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://dmunity.com/')
time.sleep(2)
driver.maximize_window()

# Call the login method with the credentials
login(driver, "admin@dmunity.com", "123456")

# Other code or actions after login
# ...

# Close the browser
driver.quit()





