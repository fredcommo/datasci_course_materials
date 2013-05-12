import sys
import json
import re

#def hw():
#    print 'Hello, world!'

#def lines(fp):
#    print str(len(fp.readlines()))

def buildSentim(f):
	sentim = dict()
	for line in f:
		key, value = line.strip().split('\t')
		if not key in sentim.keys():
			sentim[key] = value
	return sentim

def buildTweet(f):
	tweetList = []
	for line in f:
		d = json.loads(line)
	 	if u'text' in d.keys():
	 		tweetList.append(json.dumps(d['text']))
	return tweetList

def tweetScore(tweet, sentim):
	score = 0.0
	if any(set(sentim.keys()) & set(tweet.split())):
		words = set(sentim.keys()) & set(tweet.split())
		for w in words:
			score += float(sentim[w])
	return score

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	sentim = buildSentim(sent_file)
	tweetList = buildTweet(tweet_file)
	Scores = [tweetScore(t, sentim) for t in tweetList]
	for s in Scores:
		print str(s)


if __name__ == '__main__':
	main()
