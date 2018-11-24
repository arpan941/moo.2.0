from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

class Authentication:
    def authenticate(self, tweetsFile, searchWords):
        auth = OAuthHandler("YO3onH8vbakEW2ZCzaXbx01VW", "FsupJ0Cu595QPXPswPWbmetm6ktZSy86QXN4TN3aHa3AdrVSU9")
        auth.set_access_token("42595577-IRgFyBq8btWa50H11GZIwE6EexFjQI2lmLGh5gOTV", "lxhe0unY42ZMF5bH9CLv7K9ioeoiSkM7PaPqQ2tDf6m0v")
        listener = Listener(tweetsFile)
        twitterStream = Stream(auth, listener)
        twitterStream.filter(track=searchWords)

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
        print (status)

if __name__ == '__main__':
    searchWords = ["AAPL"]
    tweetsFile = "tweets.txt"
    auth = Authentication()
    auth.authenticate(tweetsFile, searchWords)
