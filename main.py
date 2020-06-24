import tweepy, os, time
from dotenv import load_dotenv

load_dotenv()

# Setup API:
def twitter_setup():
    # Authenticate and access using keys:
    auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))

    # Return API access:
    api = tweepy.API(auth)
    return api

if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()

    # Set waiting time:
    secs = 3

    # Set tweet list:
    tweetlist = ["Esto es una prueba con un bot", "Parece que funciona", "El bot esta VIVO!!"]

    # Tweet posting:
    for tweet in tweetlist:
        # Print tweet:
        print(tweet)

        # Try to post tweet:
        try:
            bot.update_status(tweet)
            print("Successfuly posted!")
        except tweepy.TweepError as e:
            print(e.reason)

        # Wait till next sentence extraction:
        time.sleep(secs)