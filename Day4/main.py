# Import BeautifulSoup
from bs4 import BeautifulSoup

# read the file and hold it in variable
with open("index.html") as file:
  contents = file.read()

# create a beautifulsoup object
soup = BeautifulSoup(contents, 'html.parser')

# To get html title tag
# print(soup.title)

# To get content of title tag
# print(soup.title.string)

# To see full html without any format
# print(soup)

# To see full html with format
# print(soup.prettify())

# To get a tag and text
#print(soup.a)
#print(soup.a.name)
#print(soup.a.string)

# To get all anchor tags
#all_anchor_tags = soup.find_all(name='a')

#for tag in all_anchor_tags:
 # print(tag.getText())
  #print(tag.get("href"))

# To get particular element based on attribute
#heading_tag = soup.find(name='h1', id='name')
#print(heading_tag)

# To get element based on class attribute
#paragraph_info = soup.find(name='p', class_='about')
#print(paragraph_info)


# To get a hyper link based on nested element selector
#selector = soup.select_one(selector = "p a")
#print(selector)

# To get a hyper link based on css selector

selector_css = soup.select_one(selector = ".about")
print(selector_css)
