import tweepy 
from textblob import TextBlob 


#Twitter API Credentials 
consumer_key = 'y71A0fXP1BEaNs5vt1pWb03Cl'
consumer_secret = 'jHXgPQYdU8kbIwXAJJU9zZdNOmISfikrB6jhVBjCFGYAaAFjBr'
access_token = '1823660903474343936-46NqrD5TCaPkgPXEz3EjxFR7CHn4Bn'
access_token_secret = 'qMRbYPcJ99b8kSZiivrcn50fxPIa2Y60RUAVyG16BAJ4P'

#X authetication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,  access_token_secret)

#access api 
api = tweepy.API(auth)

public_tweet = api.search_tweets('Lebron James')
for tweet in public_tweet: 
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
