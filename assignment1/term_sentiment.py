import sys
import json
import re

# def hw():
#     print 'Hello, world!'

# def lines(fp):
#     print str(len(fp.readlines()))

# def main():
#     sent_file = open(sys.argv[1])
#     tweet_file = open(sys.argv[2])
#     hw()
#     lines(sent_file)
#     lines(tweet_file)

def buildSentim(f):
	sentim = dict()
	for line in f:
		key, value = line.strip().split('\t')
		if not key in sentim.keys():
			sentim[key] = value
	return sentim

# def buildTweet(f, value):
# 	tweetList = []
# 	for line in f:
# 		d = json.loads(line)
# 	 	if value in d.keys():
# 	 		tweetList.append(json.dumps(d[value]))
# 	return tweetList

def buildTweet2(f, value):
	tweetList = []
	lines  = f.readlines()
	tweetList = [json.loads(line)[value].encode('utf-8').split() for line in lines if value in json.loads(line).keys()]
	return tweetList

def tweetScore(tweet, sentim):
	score = [0.0]
	if any(word.lower() in sentim.keys() for word in tweet):
		score = [float(sentim[word.lower()]) for word in tweet if word.lower() in sentim.keys()]
	return sum(score)

def newScore(tweet, sentim):
	newWord = []
	newScore = []
	score = tweetScore(tweet, sentim)
	for word in tweet:
	 	if not word in sentim.keys():
	 		newWord.append(word)
	 		newScore.append(score)
	return newWord, newScore

def getTweet(line, value):
	d = json.loads(line)
	if value in d.keys():
		tweet = json.dumps(d[value]).split()
		return tweet

def cleanTweet(tweet):
	cleaned = ''
	for word in tweet:
		cleaned += ' '+ re.sub('\W|\\\\|^@|\/|^u|http.+', ' ', word).lower()
# 		word = re.sub('@.+', '', word)
# 		word = re.sub('\\\u.+', '', word)
# 		word = re.sub('\\\\', '', word)
# #		word = re.sub('RT', '', word)
# 		word = re.sub('//', '', word)
# 		word = re.sub('http.+', '', word)
# 		word = re.sub('#.+', '', word)
# 		word = re.sub(' ', '', word)
# 		word = re.sub('\"', '', word)
# 		if word != '':
# 			cleaned += ' '+ word
#		print 'word', cleaned, str(cleaned) == ' "'
	#if str(cleaned) != ' "':
	return str(cleaned).split()
#	else:
#		return str('_')

def buildDict(currentDict, word, score):
	for i in range(len(word)):
		if not word[i] in currentDict:
			currentDict[word[i]] = float(score[i])
		else:
			currentDict[word[i]] = currentDict[word[i]] + float(score[i])
	return currentDict


def main():
	newDict = {}
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	sentim = buildSentim(sent_file)
	tweetText = buildTweet2(tweet_file, 'text')
	for tweet in tweetText:
		cleaned = cleanTweet(tweet)
		word, score = newScore(tweet, sentim)
		newDict = buildDict(newDict, word, score)
	for word in newDict.keys():
		print word, newDict[word]


if __name__ == '__main__':
    main()
