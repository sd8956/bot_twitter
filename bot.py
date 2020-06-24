import tweepy, os, re
from dotenv import load_dotenv
from random import randint

load_dotenv()

def twitter_setup():
    auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))

    api = tweepy.API(auth)
    return api

def extract_status(path=None):

    if not path:
        return "No book opened!"

    try:
        with open(path, 'r', encoding='utf-8', errors="surrogateescape") as book:
            text = book.read()

        if text:
            return search_sentence(text)
    except:
        return "Book not found."


def search_sentence(text):
    status = 200

    while not (5 < status < 125):
        index = randint(0, len(text))

        init_index = text[index:].find(".") + 2 + index
        last_index = text[init_index:].find(".")
        status = len(text[init_index:last_index])

    sentence = text[init_index:last_index]
    sentence = re.sub("\n", " ", sentence)
    return sentence


def make_tweet():
    bot = twitter_setup()
    status = extract_status("texto.txt")

    try:
        bot.update_status(status)
        print("Successfuly posted!")
    except tweepy.TweepError as e:
        print(e.reason)
