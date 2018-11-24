from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print ("Errorrrrr")

auth = OAuthHandler("YO3onH8vbakEW2ZCzaXbx01VW", "FsupJ0Cu595QPXPswPWbmetm6ktZSy86QXN4TN3aHa3AdrVSU9")
auth.set_access_token("42595577-IRgFyBq8btWa50H11GZIwE6EexFjQI2lmLGh5gOTV", "lxhe0unY42ZMF5bH9CLv7K9ioeoiSkM7PaPqQ2tDf6m0v")
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["AAPL"])
