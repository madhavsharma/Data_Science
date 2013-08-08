'''

@Author : Madhav

@Summary: Calculates the sentiment score of a tweet. Uses AFINN-111.txt

'''


import sys
import json
import re
def hw(sent_file,tweet_file):
    scores = {}
    with open(sent_file) as f:
        lines = f.readlines()
        for line in range(len(lines)):
            term, score  = lines[line].split("\t")
            scores[term] = int(score)
            
    #print 'end of function'
    #print scores
    tweets = []
    data = []
    with open(tweet_file) as f:
        filedata = f.readlines()
        for line in range(len(filedata)):
            linedata = dict(json.loads(filedata[line].strip()))
            if linedata.has_key('text'):
                tweets.append(linedata['text'].encode('utf-8'))

    
    single_tweet_filter = []
    tweet_score = []
    for i in range(len(tweets)):
        #single_tweet_filter = []
        #single_tweet = tweets[i]
        #for  word in range(len(single_tweet.split())):
        single_tweet = " ".join(re.findall("[@a-zA-Z]+", tweets[i]))
        #print "***********"
        single_tweet_filter.append(single_tweet)
        #print single_tweet_filter[i]
        #print i,tweets[i]
        #print "***********"

    for tweet in range(len(single_tweet_filter)):
        tweet_words = (single_tweet_filter[tweet]).split()
        total = 0
        for i in tweet_words:
            if scores.has_key(i):
                total+=scores[i]
            else:
                total+=0
        tweet_score.append(total)

    for i in tweet_score:
        print float(i)





def lines(fp):
    print str(len(fp.readlines()))

def main():
    _score = sys.argv[1]
    _tweet = sys.argv[2]
    sent_file = open(sys.argv[1],'r')
    tweet_file = open(sys.argv[2],'r')
    hw(_score,_tweet)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
