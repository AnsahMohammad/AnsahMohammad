from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

print("imports done")

driver = webdriver.Edge()
print("Initialized the driver")

# Open the login page
driver.get("https://172.16.1.1:8090")

if driver.title == "Privacy error":
    # click on advanced

    print("Privacy error encountered.")
    
    # Click on the "Advanced" link
    advanced_link = driver.find_element(By.ID, "details-button")
    advanced_link.click()
    
    time.sleep(2)
    
    proceed_link = driver.find_element(By.ID, "proceed-link")
    proceed_link.click()

if "User Session is already opened" in driver.page_source:
    print("Already logged")
    driver.quit()
else:
    try:
        username_field = driver.find_element(By.ID, "name")
        password_field = driver.find_element(By.ID, "password")

        u_name = os.environ.get("username")
        u_pass = os.environ.get("password")
        username_field.send_keys(u_name)
        password_field.send_keys(u_pass)
        password_field.send_keys(Keys.RETURN)
    except:
        print("Error occured")


time.sleep(5)
driver.quit()
