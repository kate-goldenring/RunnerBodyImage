"""
The purpose of this program is to extract text from a series of running websites and
collect data on the number of occurrences of specific body negative words
and record the sites at which they occur
the ultimate goal is to create a google chrome extension that rates a web-page's body positivity using this count
and replaces these words with new words
and links to sites with positive body ideals!
"""

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#read in the target URLs into a list
with open("urls.txt") as f:
    urls = f.readlines()
urls = [x.strip() for x in urls]

#read in the target words into a list
with open("keyWords.txt") as f:
    words = f.readlines()
words = [x.strip() for x in words]

#fill dictionary with words
#contains words as key and value and num occurances; innitialize to be 0
wordDict = {}
for w in words:
    wordDict[w] = 0

def wordCount(word, text):
    count = text.count(word)
    wordDict[word] = wordDict.get(word) + count

def checkWordsInURL(wordList, urlList):
    for url in urlList:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.get_text("|", strip=True)  # returns all text as a unicode string
        for word in wordDict:
            wordCount(word,text)

checkWordsInURL(words, urls)
fig, ax = plt.subplots()
plt.bar(range(len(wordDict)), wordDict.values(), align="center")
plt.xticks(range(len(wordDict)), list(wordDict.keys()), rotation = 30)
plt.title("Occurrences of Negative Words")
plt.xlabel("Target Words")
plt.ylabel("Number of Occurrences")

plt.show()
print(wordDict)