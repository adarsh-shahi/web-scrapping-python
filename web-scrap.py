import requests
from bs4 import BeautifulSoup
url = "http://localhost:5500"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'lxml');
# print(soup.prettify())
body = soup.find('section')

print(body)

# Adarsh Shahi (BCOA4)