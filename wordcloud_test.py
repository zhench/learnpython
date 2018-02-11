# -*- coding:utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordtextpath="./yes minister.txt"

with open(wordtextpath,mode='r') as f:
    mytext=f.read()
#print(mytext)
wordcloud=WordCloud().generate(mytext)
plt.show(wordcloud)
plt.axis("off")