import sys
import json
import re
from collections import Counter

def buildTweet(f, value):
	tweetList = []
	for line in f:
		d = json.loads(line)
	 	if value in d.keys():
			tweetList.append(d[value].encode('utf-8').split())
	return tweetList

def cleanTweet(tweet):
	cleaned = ''
	for word in tweet.split():
#		cleaned += ' '+(re.sub('\\\\|^@|\/|^u|http.+', ' ', word).lower())
		word = re.sub('@.+', '', word)
		word = re.sub('\\\u.+', '', word)
		word = re.sub('\\\\', '', word)
#		word = re.sub('RT', '', word)
		word = re.sub('//', '', word)
		word = re.sub('http.+', '', word)
		word = re.sub('#.+', '', word)
		word = re.sub(' ', '', word)
		if word != '':
			cleaned += ' '+ word # .lower()
#		print 'word', cleaned, str(cleaned) == ' "'
	if str(cleaned) != ' "':
		return str(cleaned)
	else:
		return str('_')

def cleanWord(word):
	word = re.sub('@.+', '', word)
	word = re.sub('\\\u.+', '', word)
	word = re.sub('\\\\', '', word)
#	word = re.sub('RT', '', word)
	word = re.sub('//', '', word)
	word = re.sub('http.+', '', word)
	word = re.sub('#.+', '', word)
	word = re.sub('"', '', word)
	word = re.sub(' ', '', word)
	return str(word)

def buildTweet2(f, value):
	tweetList = []
	lines  = f.readlines()
	tweetList = [json.loads(line)[value].encode('utf-8').split() for line in lines if value in json.loads(line).keys()]
	return tweetList

def freqWord(tweetText):
	alltweets = [word for tweet in tweetText for word in tweet]
	freq = Counter(alltweets)
	return freq

def main():
	tweet_file = open(sys.argv[1])
	tweetText = buildTweet2(tweet_file, 'text')
	wordFreq = freqWord(tweetText)
	nTerms = float(len(wordFreq))
	for word in wordFreq:
	 	print str(word) , str(wordFreq[word]/nTerms)

if __name__ == '__main__':
    main()
