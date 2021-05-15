from bs4 import BeautifulSoup
import requests

scrapping_from_source ='https://news.ycombinator.com/'

# Read entire content from url
web_response = requests.get(scrapping_from_source)

yc_web_page = web_response.text

# parse this website
soup = BeautifulSoup(yc_web_page, 'html.parser')

# print(soup.prettify())


# To get first title, link and score
# article_info = soup.find(name='a', class_="storylink")

# article_text = article_info.getText()
# print(article_text)
# article_link = article_info.get('href')
# print(article_link)
# article_tag_score = soup.find(name='span', class_="score").getText()
# print(article_tag_score)

# To get all articles, links and score
article_texts = []
article_links = []
articles = soup.find_all(name='a', class_="storylink")

for article_info in articles:
  article_texts.append(article_info.getText())
  article_links.append(article_info.get('href'))

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_="score")]
  
# print(article_texts)
# print(article_links)
# print(article_scores)

# print the highest score record

largest_number = max(article_scores)
print(largest_number)
# Get index of this largest number
index = article_scores.index(largest_number)
print(index)

# Print largest value based on index
print(article_texts[index])
print(article_links[index])
print(article_scores[index])

# for tag in anchros:
#   print(tag.get_text())
#   print(tag.get('href'))