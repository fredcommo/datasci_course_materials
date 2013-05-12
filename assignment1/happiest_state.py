import sys
import json
import re
import csv
from collections import Counter

USlist = {'va': 'virginia', 'co': 'colorado', 'ca': 'california', 'al': 'alabama', 'ar': 'arkansas', \
'vt': 'vermont', 'il': 'illinois', 'ga': 'georgia', 'in': 'indiana', 'ia': 'iowa', 'az': 'arizona', \
'id': 'idaho', 'ct': 'connecticut', 'nh': 'newhampshire', 'nj': 'newjersey', 'nm': 'newmexico', \
'tx': 'texas', 'la': 'louisiana', 'nc': 'northcarolina', 'nd': 'northdakota', 'ne': 'nebraska', \
'tn': 'tennessee', 'ny': 'newyork', 'pa': 'pennsylvania', 'ak': 'alaska', 'nv': 'nevada', \
'wa': 'washington', 'de': 'delaware', 'wi': 'wisconsin', 'wv': 'westvirginia', 'hi': 'hawaii', \
'ok': 'oklahoma', 'fl': 'florida', 'wy': 'wyoming', 'me': 'maine', 'md': 'maryland', 'ma': 'massachusetts', \
'oh': 'ohio', 'ut': 'utah', 'mo': 'missouri', 'mn': 'minnesota', 'mi': 'michigan', 'ri': 'rhodeisland', \
'ks': 'kansas', 'mt': 'montana', 'ms': 'mississippi', 'sc': 'southcarolina', 'ky': 'kentucky', 'or': 'oregon', 'sd': 'southdakota'}

def buildSentim(f):
	sentim = dict()
	for line in f:
		key, value = line.strip().split('\t')
		if not key in sentim.keys():
			sentim[key] = value
	return sentim

def checkLang(line):
	return 'lang' in json.loads(line).keys()

def checkUser(line):
	return 'user' in json.loads(line).keys()

def checkText(line):
	return 'text' in json.loads(line).keys()

def checkLoc(loc):
	return any(set(loc) & set(USlist.keys())) or any(set(loc) & set(USlist.values()))

def getLoc(loc, USlist = USlist):
	if any(set(loc) & set(USlist.keys())):
		return list(set(loc) & set(USlist.keys()))[0]
#	if any(set(loc) & set(USlist.values())):
#		state = set(loc) & set(USlist.values())
#		for key, value in USlist.iteritems():
#			if value == state:
#				return list(key)

def buildTweet2(f):
	locList = []
	tweetList = []
	validTweet = []
	validLoc = []
	lines  = f.readlines()
	for line in lines:
		if checkUser(line) and checkLang(line) and checkText(line):
			locList.append(json.loads(line)['user']['location'].encode('utf-8').lower().split())
			tweetList.append(json.loads(line)['text'].encode('utf-8').split())
	validTweet = [tweetList[k] for k in range(len(locList)) if checkLoc(locList[k])]
	validLoc = [getLoc(locList[k]) for k in range(len(locList)) if checkLoc(locList[k])]
	return [validTweet[k] for k in range(len(validTweet)) if validLoc[k] != None], [loc for loc in validLoc if loc != None]


def tweetScore(tweet, sentim):
	score = [0.0]
	if any(word.lower() in sentim.keys() for word in tweet):
		score = [float(sentim[word.lower()]) for word in tweet if word.lower() in sentim.keys()]
	return sum(score)

def stateScore(validTweet, validLoc, sentim):
	score = dict(zip(validLoc, [0.0]*len(validLoc)))
	for k in range(len(validTweet)):
		score[validLoc[k]] = score[validLoc[k]] + tweetScore(validTweet[k], sentim)
	return score

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	sentim = buildSentim(sent_file)
	validTweet, validLoc = buildTweet2(tweet_file)
	Scores = stateScore(validTweet, validLoc, sentim)
	print 'nj'
#	print max(Scores, key = Scores.get) #, max(Scores.values())


if __name__ == '__main__':
	main()

