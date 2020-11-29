import requests
from bs4 import BeautifulSoup

class dateSignificance:

    @staticmethod
    def getImportantEventToday():
        page = requests.get("https://www.britannica.com/on-this-day")
        pageData = BeautifulSoup(page.text, 'html.parser')
        
        significanceTitle = pageData.select_one(".otd-featured-event .title").text.strip()
        significanceBody = pageData.select_one(".otd-featured-event .description").text.strip()
       
        return f"On this day in history, {significanceTitle}, {significanceBody}"

    @staticmethod
    def dateHolidays():
        page = requests.get("https://www.timeanddate.com/")
        pageData = BeautifulSoup(page.text, 'html.parser')

        info = f'Did you know that today is {pageData.select_one("#feat1 .rd-inner h4").text}, {pageData.select("#feat1 .rd-inner p")[-1].text.strip().split("Full Story")[0]}'
        return info

if __name__ == "__main__":
    print(dateSignificance.dateHolidays())