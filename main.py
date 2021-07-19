import tweepy
# Authenticate credentials
auth = tweepy.OAuthHandler("CONSUMER", "CONSUMERSECRET")
auth.set_access_token("ACCESS", "ACCESSSECRET")

# Create API object
twitter_api = tweepy.API(auth)

# Tweet from terminal
print("Enter tweet.")
tweet = input("TWEET:")
twitter_api.update_status(tweet)