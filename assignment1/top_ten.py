import sys
import json
import re
from collections import Counter

def buildTweet2(f, value):
	''' From the file f, return a list of tweet texts as lists'''
	tweetList = []
	lines  = f.readlines()
	tweetList = [json.loads(line)[value].encode('utf-8') for line in lines if value in json.loads(line).keys()]
	return tweetList

def hashScore(tweetList):
	''' Find the words which are hashtags (#myhashtag), and count the occurences
		Return a dict using Counter (hashtags as keys, occurences as values)
	'''
	tag = re.compile('\#.+')
	hashtags = [tag.findall(word) for tweet in tweetList for word in tweet.split() if '#' in word]
	hashtags = [tag for sublist in hashtags for tag in sublist]
	return Counter(hashtags)

def main():
	tweet_file = open(sys.argv[1])
	tweetList = buildTweet2(tweet_file, 'text')
	Scores = hashScore(tweetList)
	topTen = Counter(Scores).most_common(10)	# return the top ten.
	for top in topTen:
		print re.sub('#', '', top[0]), float(top[1])

if __name__ == '__main__':
    main()
