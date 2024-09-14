from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Maz")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Miz")

email = driver.find_element_by_name("email")
email.send_keys("max@yahoo.com")

sign_up = driver.find_element_by_xpath('/html/body/form/button')
sign_up.send_keys(Keys.ENTER)
