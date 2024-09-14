#Automated Job Application with Selenium, Automated job application bot
# drives a browser to open a website and apply for a job
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# the linkdein endpoint
URL ="https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=python%20developer"
driver.get(url=URL)

# finds signin  button and clicks on it
sign_in = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")
sign_in.click()

# waits for 1 second to load the page
time.sleep(2)

# Finds email bar and inserts the email
email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys("**************")

# Finds the password bar and inserts the password
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("**********")

sign_in_click = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
sign_in_click.click()

time.sleep(2)
apply_button = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/button')
apply_button.send_keys(Keys.ENTER)

time.sleep(2)
submit_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button')
submit_button.send_keys(Keys.ENTER)







