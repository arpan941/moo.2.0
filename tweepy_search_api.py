from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import csv

class Authentication:
    def authenticate(self, tweetsFile, searchQuery):
        auth = OAuthHandler("YO3onH8vbakEW2ZCzaXbx01VW", "FsupJ0Cu595QPXPswPWbmetm6ktZSy86QXN4TN3aHa3AdrVSU9")
        auth.set_access_token("42595577-IRgFyBq8btWa50H11GZIwE6EexFjQI2lmLGh5gOTV", "lxhe0unY42ZMF5bH9CLv7K9ioeoiSkM7PaPqQ2tDf6m0v")
        api = API(auth,wait_on_rate_limit=True)
        csvFile = open(tweetsFile, 'a')
        csvWriter = csv.writer(csvFile)
        for tweet in Cursor(api.search, q=searchQuery, lang="en", since_id=1070342209952730000, count=100).items(): #if you put count inside the cursor method as count=100, you can restrict the no of tweets
            print(tweet.created_at, tweet.id,tweet.text)
            csvWriter.writerow([tweet.created_at,tweet.id,tweet.text.encode('utf-8')])
        tweets=api.search(q="$AAPL")

if __name__ == '__main__':
    searchQuery = "$AAPL"
    tweetsFile = "tweets3.csv"
    auth = Authentication()
    auth.authenticate(tweetsFile, searchQuery)
