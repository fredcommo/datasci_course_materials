import sys
import json
import re


def buildSentim(f):
    sentim = dict()
    for line in f:
        key, value = line.strip().split('\t')
        if not key in sentim.keys():
            sentim[key] = value
    return sentim

def getTweet(line, value):
    d = json.loads(line)
    if value in d.keys():
        tweet = json.dumps(d[value])
        return str(tweet).split()
	    
def tweetScore(tweet, sentim):
    score = 0.0
    for word in tweet:
        print word.lower() in sentim.keys()

#    for word in tweet:
#        print word

def main():
    sent_file = open('AFINN-111.txt')
    tweet_file = open('output2.txt')
    sentim = buildSentim(sent_file)
    for line in tweet_file:
        tweet = getTweet(line, 'text')
        tweet = str(tweet).split()
        tweetScore(tweet, sentim)
    return sentim


#		tweetScore(tweet, sentim)


#	tweetList = buildTweet(tweet_file)
#	for tweet in tweetList:
#		newSentim(tweet, sentim)


if __name__ == '__main__':
    sentim = main()
