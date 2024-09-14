from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

# find an element with xpath
article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(article_count.text)

# click method selenium 
# automaticlcy clikes on the link or targeted elements on a webpage
all_portals = driver.find_element_by_partial_link_text("All portals")
# all_portals.click()


# search box on web page, finds a text on a webpage
search = driver.find_element_by_name("search")
# types "python" on the search bar
search.send_keys("Python")
# hits enter 
search.send_keys(Keys.ENTER)




# driver.quit()