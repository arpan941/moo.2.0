from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
from tweepy import Cursor

class TwitterClient:
    def __init__(self, handle=None):
        a= Authentication()
        self.auth = a.twitterAuthentication()
        self.twitterClient = API(self.auth, wait_on_rate_limit=True)
        self.handlefortimeline = handle
   
    def get_tweets_of_someone(self):
        tweets = []
        for tweet in Cursor(self.twitterClient.user_timeline, id = self.handlefortimeline).items(3):
            #tweets.append(tweet.text)
            print(tweet.text)
            tweets.append(tweet)
        return tweets

    def find_replies_to_tweets(self, tweets):
        id = tweets[0].id_str
        print(tweets[0])
        print(id)
        for_user = 'to:'+self.handlefortimeline
        replies = []
        for tweet in Cursor(self.twitterClient.search,q=for_user, since_id=id).items(100):
            print("replies----------------------------------*******")
            print(tweet)
            print("text----------------------------------*******")
            
            print(tweet.text)
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                print(tweet.in_reply_to_status_id_str)
                print(id)
                if (tweet.in_reply_to_status_id_str==id):
                    print("FOUND IT YAYYYYYYYYYYYYYYYYYYYY :D----------------------------------*******")
                    print(tweet)
                    replies.append(tweet)
        return replies

class Authentication:
    
    def twitterAuthentication(self):
        auth = OAuthHandler("YO3onH8vbakEW2ZCzaXbx01VW", "FsupJ0Cu595QPXPswPWbmetm6ktZSy86QXN4TN3aHa3AdrVSU9")
        auth.set_access_token("42595577-IRgFyBq8btWa50H11GZIwE6EexFjQI2lmLGh5gOTV", "lxhe0unY42ZMF5bH9CLv7K9ioeoiSkM7PaPqQ2tDf6m0v")
        return auth

class StreamTweets:
    def __init__(self):
        self.twAuth = Authentication()

    def streamtweets(self, tweetsFile, searchWords):
        listener = Listener(tweetsFile)
        stream = Stream(listener, self.twAuth.twitterAuthentication())
        stream.filter(track=searchWords)

class Listener(StreamListener):

    def __init__(self, tweetsFile):
        self.tweetsFile = tweetsFile

    def on_data(self, data):
        try:
            print(data)
            with open(self.tweetsFile,"w+") as f:
                f.write(data)
                f.close()
            return(True)
        except BasicException as e:
            print("Error : %s" % str(e))
        return true

    def on_error(self, status):
        if status==420:
            return false
        print (status)

if __name__ == '__main__':
##    searchWords = ["AAPL"]
##    tweetsFile = "tweets.txt"
##    auth = Authentication()
##    auth.authenticate(tweetsFile, searchWords)
    tc = TwitterClient('andrea_1994')
    tweets = tc.get_tweets_of_someone()
    replies = tc.find_replies_to_tweets(tweets)
