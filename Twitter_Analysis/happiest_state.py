'''

@Author : Madhav

@Summary: Computes the name of the happiest state (US)  based on the tweet score. Makes use of place object in tweet structure for location.

'''




import sys
import json
import re
def hw(sent_file,tweet_file):
    states = {'Alabama': 'AL','Alaska': 'AK','American Samoa': 'AS','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','District of Columbia': 'DC','Florida': 'FL','Georgia': 'GA','Guam': 'GU','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','National': 'NA','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Northern Mariana Islands': 'MP','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Puerto Rico': 'PR','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virgin Islands': 'VI','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}




    #print 'Hello, world!'
    #lines(sent_file)
    scores = {}
    with open(sent_file) as f:
        lines = f.readlines()
        for line in range(len(lines)):
            term, score  = lines[line].split("\t")
            scores[term] = int(score)
            #print term,score
    #print 'end of hw function'
    #print scores
    state_name = []
    tweets = []
    data = []
    with open(tweet_file) as f:
        filedata = f.readlines()
        for line in range(len(filedata)):
            linedata = dict(json.loads(filedata[line].strip()))
            if linedata.has_key('text'):
                place = linedata['place']
                if place is not None:
                    if (place['country_code'].lower()=='us'):
                    #place_filter = dict(json.loads(str(place)))
                        #print place['country_code'],place['name'], linedata['user']['location']
                        tweets.append(linedata['text'].encode('utf-8'))
                        state_name.append(place['full_name'])
    single_tweet_filter = []
    tweet_score = []
    for i in range(len(tweets)):
        single_tweet = " ".join(re.findall("[@a-zA-Z]+", tweets[i]))
        single_tweet_filter.append(single_tweet)

    for tweet in range(len(single_tweet_filter)):
        tweet_words = (single_tweet_filter[tweet]).split()
        total = 0
        for i in tweet_words:
            if scores.has_key(i):
                total+=scores[i]
            else:
                total+=0
        tweet_score.append(total)
    
    sentiment_count = {}
    for i in range(len(tweet_score)):
        if sentiment_count.has_key(state_name[i]):
            sentiment_count[state_name[i]]+=tweet_score[i]
        else:
            sentiment_count[state_name[i]] = tweet_score[i]    
            
                
        #print float(i)

    max_sentiment = max(sentiment_count,key=sentiment_count.get)
    state_name = max_sentiment.split(',')[1].strip()
    happiest_state = state_name.encode('utf-8')
    print happiest_state

def main():
    _score = sys.argv[1]
    _tweet = sys.argv[2]
    sent_file = open(sys.argv[1],'r')
    tweet_file = open(sys.argv[2],'r')
    hw(_score,_tweet)

if __name__ == '__main__':
    main()
