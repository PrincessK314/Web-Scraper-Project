#This module contains the abstract class WebScraper.
#A subclass will take a URL as an input.
#Using the methods of the class, the output of author, publish date, haedline, and article text
#can be retrieved from the webpage.
#The class SoupScraper, a subclass of WebScraper, uses the python package BeautifulSoup to retrieve
#this data from the html of the webpage.

from urllib.request import urlopen
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class WebScraper(ABC):
    def __init__(self, url: str) -> None:
        self.url = url

    @abstractmethod
    def getArticle(self) -> str:
        pass
    
    @abstractmethod
    def getAuthor(self) -> str:
        pass
    
    @abstractmethod
    def getDate(self) -> str:
        pass
    
    @abstractmethod
    def getHeadline(self) -> str:
        pass
    
class SoupScrapper(WebScraper):
    def __init__(self, url: str) -> None:
        self.url = url
        page = urlopen(self.url)
        html = page.read().decode("utf-8")
        self.soup = BeautifulSoup(html, "html.parser")

    def getArticle(self) -> str:
        body = self.soup.find_all("div", class_="article__section_type_text")
        text = ""
        for match in body:
            text += match.text.strip()
            text += "\n"
        return text
    
    def getAuthor(self) -> str:
        text = self.soup.find("div", class_="article__author")
        return text.text.strip()
    
    def getDate(self) -> str:
        text = self.soup.find("div", class_="article__published")
        return text.text.strip()
    
    def getHeadline(self) -> str:
        text = self.soup.find("h1", class_="article__headline")
        return text.text.strip()