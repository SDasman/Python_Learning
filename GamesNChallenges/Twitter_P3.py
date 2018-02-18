tweet = input('Please tweet here: ')
tweet_length = len(tweet)
print('Total length of this tweet was ' + str(tweet_length) + '.')
twitter_limit = 144
difference = abs(twitter_limit - tweet_length)
if tweet_length <= twitter_limit:
    print("Good Job - Twitter works and tweet length is solid! "
          "You can add " + str(difference) + " more characters if you'd like.")
elif tweet_length > twitter_limit:
    print("Twitter is still good, your tweet is not. Please trim  " + str(difference) + " characters from it.")
elif tweet_length == 0:
    print("Gotta type something bud. You have " + twitter_limit + " characters to speak your mind!")

