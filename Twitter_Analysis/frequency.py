'''

@Author : Madhav

@Summary: compute the term frequency histogram of the livestream data.

'''


import sys
import json
import re
import collections
def hw(tweet_file):
    tweets = []
    data = []
    with open(tweet_file) as f:
        filedata = f.readlines()
        for line in range(len(filedata)):
            linedata = dict(json.loads(filedata[line].strip()))
            if linedata.has_key('text'):
                tweets.append(linedata['text'].encode('utf-8'))

    #print "printing data"
    single_tweet_filter = []
    tweet_score = []
    unscored_words = []
    unscored_words_score = []
    total_count = 0
    word_count = {}
    word_list = []
    for i in range(len(tweets)):
        single_tweet = " ".join(re.findall("[@a-zA-Z]+", tweets[i]))
        single_tweet_filter.append(single_tweet)

    for tweet in range(len(single_tweet_filter)):
        tweet_words = (single_tweet_filter[tweet]).split()
        total_count+=(len(tweet_words))   


    for tweet in range(len(single_tweet_filter)):
        tweet_words = (single_tweet_filter[tweet]).split()
        for i in tweet_words:
            word_list.append(i)

    term_frequency = collections.Counter(word_list)
    for key, value in term_frequency.items():
        print key, (float(value)/float(total_count))



def main():
    _tweet = sys.argv[1]
    hw(_tweet)

if __name__ == '__main__':
    main()
