'''

@Author : Madhav

@Summary: Computes the ten most frequently occurring hash tags from the twitter data collected during streaming.

'''



import sys
import json
import re
import collections
def hw(tweet_file):
    tweets = []
    hashtag_data = []
    with open(tweet_file) as f:
        filedata = f.readlines()
        for line in range(len(filedata)):
            linedata = dict(json.loads(filedata[line].strip()))
            if linedata.has_key('text'):
                entities = linedata['entities']
                if entities['hashtags'] is not None:
                    tweet_hashtags = entities['hashtags']
                    #print type(tweet_hashtags)
                    for i in range(len(tweet_hashtags)):
                        hashtag_data.append(tweet_hashtags[i]['text'].encode('utf-8'))
    
    dict_hashtag = collections.Counter(hashtag_data)
    import operator
    sorted_hashtag = sorted(dict_hashtag.iteritems(), key=operator.itemgetter(1))[-10:]
    for i in sorted_hashtag:
        print i[0], float(i[1])
    
    '''
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

    '''

def main():
    _tweet = sys.argv[1]
    hw(_tweet)

if __name__ == '__main__':
    main()
