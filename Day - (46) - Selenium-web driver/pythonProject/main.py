#Selenium web Driver
# Selenium automates browsers
# get the browser to do things automatically depending on a script or a piece of code that we write. 
from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/ororo-Womens-Lightweight-Heated-Battery/dp/B01H50RDW0/ref=sr_1_1?dchild=1&pf_rd_p=b259e858-a049-48b9-bb0e-40a71a113bbc&pf_rd_r=Y8R7M2WJA1JZ54AZ10NN&qid=1611383590&s=apparel&sr=1-1")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

title_name= driver.find_element_by_xpath('//*[@id="productTitle"]')
print(title_name.text)




# # closes single tab
# driver.close()
# # closes entire browsers
driver.quit()
