import sys

sent_file = open('AFINN-111.txt', 'r')
#tweet_file = open(sys.argv[2], 'r')

sent = dict()
for line in sent_file:
    print line
