from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Get cookie to click on.
cookie = driver.find_element_by_id("bigCookie")
num = 0
while num < 10:
    cookie.click()
    
    
