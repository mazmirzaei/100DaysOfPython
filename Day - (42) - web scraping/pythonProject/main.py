from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

#get title of each article 
article_tags = soup.find_all(name='a', class_="storylink")
text_list=[]
link_list=[]
for tag in article_tags:
    text = tag.getText()
    text_list.append(text)
    link = tag.get('href')
    link_list.append(link)
print(link_list)
print(text_list)

article_pionts = soup.find_all(name='span', class_='score')
point_list = [int(tag.getText().split()[0]) for tag in article_pionts]
print(point_list)

#highest voted index

max_vote = max(point_list)
index = point_list.index(max_vote)
print(f"The higest voted article is {text_list[index]} the URL is {link_list[index]} and has {max_vote} vote")

























#web scarping
# html parser(beautiful soup)
# BT is a Python library for pulling data out of HTML and XML files

#in case of xml file
# import lxml


# 
# with open('website.html', encoding="utf8") as file:
#     contents = file.read()
# 
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a.string)

#how to get all tags ex all p tags..
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# 
# all_paraghraph_tags = soup.find_all(name="p")
# print(all_paraghraph_tags)
# 
# #to get all string in p tag
# for tag in all_paraghraph_tags:
#     print(tag.getText())
# 
# #to get all anchor tag stirng
# for tag in all_anchor_tags:
#     print(tag.getText())
# 
# for tag in all_anchor_tags:
#     print((tag.get("href")))
# 
# heading = soup.find(name="h1", id='name')
# print(heading)
# 
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))
# 
# 
# #Select_one selects first matching item
# name = soup.select_one(selector="#name")
# print(name.getText())
# 
# habbit_url = soup.select_one(selector=".habb")
# print(habbit_url.get('href'))
# 
# company_url=soup.select_one(selector="p a")
# print(company_url.get("href"))