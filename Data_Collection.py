from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
from tweepy import Cursor
import csv
import datetime

class TwitterClient:
    def __init__(self, handle=None):
        a= Authentication()
        self.auth = a.twitterAuthentication()
        self.twitterClient = API(self.auth, wait_on_rate_limit=True)
        self.handlefortimeline = handle

    def get_tweets_of_someone(self):
        today = datetime.datetime.today()
        yesterday = today - datetime.timedelta(days=1)
        prevFileName = "tweets-"+str(self.handlefortimeline)+'-'+str(yesterday.date())+'.csv'
        prevfile = './Resources/Tweets/'+prevFileName
        openFile = open(prevfile,'r')
        csvReader = csv.reader(openFile)
        firstRow = []
        firstRow = next(csvReader)
        from_id = firstRow[1]
        openFile.close()
        newFileName =  "tweets-"+str(self.handlefortimeline)+'-'+str(today.date())+'.csv'
        newfile = './Resources/Tweets/'+newFileName
        csvFile = open(newfile,'w',newline='')
        csvWriter = csv.writer(csvFile)
        print(self.handlefortimeline,from_id)
        for tweet in Cursor(self.twitterClient.user_timeline, id = self.handlefortimeline, since_id = from_id).items(100):
            csvWriter.writerow([tweet.created_at,tweet.id,tweet.text.encode('utf-8')])
        csvFile.close()

    def find_replies_to_tweets(self):
        today = datetime.datetime.today()
        yesterday = today - datetime.timedelta(days=1)
        prevFileName = "tweets-"+str(self.handlefortimeline)+'-'+str(yesterday.date())+'.csv'
        prevfile = './Resources/tweets/'+prevFileName
        openFile = open(prevfile,'r')
        csvReader = csv.reader(openFile)
        for row in csvReader:
            id = row[1]
            newFileName =  "replies-"+str(self.handlefortimeline)+'-'+'for_tweet_id-'+id+'-'+str(today.date())+'.csv'
            newfile = './Resources/Replies/'+newFileName
            csvFile = open(newfile,'w',newline='')
            csvWriter = csv.writer(csvFile)
            for_user = 'to:'+self.handlefortimeline
            for tweet in Cursor(self.twitterClient.search,q=for_user, since_id=id).items(200):
                if hasattr(tweet, 'in_reply_to_status_id_str'):
                    if (tweet.in_reply_to_status_id_str==id):
                        csvWriter.writerow([tweet.created_at,tweet.id,tweet.text.encode('utf-8'),tweet.in_reply_to_status_id_str])
            csvFile.close()
        openFile.close()

class Authentication:

    def twitterAuthentication(self):
        auth = OAuthHandler("YO3onH8vbakEW2ZCzaXbx01VW", "FsupJ0Cu595QPXPswPWbmetm6ktZSy86QXN4TN3aHa3AdrVSU9")
        auth.set_access_token("42595577-IRgFyBq8btWa50H11GZIwE6EexFjQI2lmLGh5gOTV", "lxhe0unY42ZMF5bH9CLv7K9ioeoiSkM7PaPqQ2tDf6m0v")
        return auth


if __name__ == '__main__':
    file = "./Resources/Handles.csv"
    handles=[]
    with open(file,'r') as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            handles.append(row[0])
    csvFile.close()
    for handle in handles:
        print(handle)
        tc = TwitterClient(handle)
        tc.get_tweets_of_someone()
        tc.find_replies_to_tweets()
