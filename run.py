#This is the main python file.
#It takes an argument containing the path of the input file when run in the command line.
#This input file should contain the URLs of 5 news articles.
#It will return output into 10 files.
#5 of these will be in the Data\processed directory and will contain only the article text.
#The other 5 will contain the headline, author, and publish date as well and will be in the Data\raw
#directory

#Of the SOLID principles, I used D while creating the modules. The WebScraper class is an abstraction
#of the functionality of the interface. The SoupScraper subclass implements this functionality using
#a python package. Other implemetations can be created as seperate subclasses of WebScraper and still
#be compatible with the OutputHandler class. 

from module_1 import webscraper as ws
from module_2 import output_handler as oh
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="inputPath", help="Enter path of input file with URLs", type=str)
    args = parser.parse_args()
    inputFileName = args.inputPath
    inFile = open(inputFileName, "r")
    count = 1
    for line in inFile:
        filename = "article" + str(count) + ".txt"
        output = oh.OutputHandler(ws.SoupScrapper(line))
        output.printArticle(filename)
        output.printExtraData(filename)
        count += 1

main()