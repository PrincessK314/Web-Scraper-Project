from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getArticleText(url: str) -> str:
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    regex = re.compile("Related Articles.*|.*Updated", re.DOTALL)
    text = regex.sub("", text)
    regex = re.compile("\A.*\s*|\s*\Z|Credit.*|FILE.*")
    text = regex.sub("", text)
    text = re.sub("\s\s+", "\n", text)
    return text

inFile = open("url.txt", "r")
count = 1
for line in inFile:
    text = getArticleText(line)
    outFile = open("article" + str(count) + ".txt", "w")
    outFile.write(text)
    outFile.close()
    count += 1

