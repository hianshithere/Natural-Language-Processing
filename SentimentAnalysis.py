#Natural Language Processing
#Sentiment Analysis Using textblob library
from textblob import TextBlob
def file():
	#file path should be peovided in _File Path_
	read = open("_FILE PATH_","r")
	reading = read.readlines()
	return reading


read = ' '.join(file()) # converting lists to string
wiki = TextBlob(read)
print(wiki.sentiment.polarity)
