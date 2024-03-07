#This module contains the OutputHandler class which takes an instance of the WebScraper class
#as an input.
#Using the methods of this class 2 files can be output:
#One contains only the main text of the article, the other contains the headline, author,
#and publish date in addition to the article
#The methods take a filename as input and will put the article text file into the processed folder
#and the extra data file into the raw folder

from module_1 import webscraper as ws

class OutputHandler():
    def __init__(self, page: ws.WebScraper) -> None:
        self.page = page

    def printArticle(self, filename: str) -> None:
        outFile = open("Data/processed/" + filename, "w")
        outFile.write(self.page.getArticle())
        outFile.close()
    
    def printExtraData(self, filename: str) -> None:
        outFile = open("Data/raw/" + filename, "w")
        outFile.write("Headline: ")
        outFile.write(self.page.getHeadline() + "\n")
        outFile.write(self.page.getAuthor() + "\n")
        outFile.write(self.page.getDate() + "\n")
        outFile.write("Article:\n" + self.page.getArticle())
        outFile.close()