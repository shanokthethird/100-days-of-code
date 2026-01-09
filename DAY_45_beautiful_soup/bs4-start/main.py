from bs4 import BeautifulSoup
import requests


def get_upvotes(liszt: list) -> int:
    return liszt[2]


resp = requests.get('https://news.ycombinator.com/news')

web_page = resp.text

soup = BeautifulSoup(web_page, 'html.parser')
anchor_tags = soup.find_all('a')
scores = soup.find_all(name='span', class_='score')
upvotes = []
for upvote in scores:
    upvotes.append(int(upvote.getText().split(' ')[0]))
links = []
ctrl = 0
for link in anchor_tags:
    if ctrl < 29:
        if 'https' in link.get('href'):
            if link.string == None:
                links.append(['HACKER NEWS', link.get('href'), 0])
            else:
                links.append([link.string, link.get('href'), upvotes[ctrl]])
                ctrl += 1
# for link in links:
#     print(link[0], link[1], link[2])
links.sort(key=get_upvotes, reverse=True)
print(links[0])
# with open('website.html') as html_doc:
#     soup = BeautifulSoup(html_doc, 'html.parser')
#
# print(soup.prettify())
