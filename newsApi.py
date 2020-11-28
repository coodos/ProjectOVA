# I wanted to make so many jokes about it
# but I am annoyed AF 
# why do I always have to be such a nerd SMH ;_;

from bs4 import BeautifulSoup
import requests

class news: 

    @staticmethod
    def getNews():

        page = requests.get('https://www.bbc.com/')
        soup = BeautifulSoup(page.text, 'html.parser')

        news = soup.findAll("a", class_ = "media__link")
        
        newsItems = []

        for newsItem in news: 
            newsItems.append(newsItem.text.strip())
        return newsItems[0:10]

if __name__ == "__main__":
    news()