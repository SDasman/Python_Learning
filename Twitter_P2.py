tweet = input('Please tweet here: ')
tweet_length = len(tweet)
print('Total length of this tweet was ' + str(tweet_length) + '.')
twitter_limit
difference = abs(144 - tweet_length)
if tweet_length <= 140:
    print("Good Job - Twitter works and tweet length is solid! "
          "You can add " + str(difference) + " more characters if you'd like.")
elif tweet_length > 140:
    print("Twitter is still good, your tweet is not. Please trim  " + str(difference) + " characters from it.")
elif tweet_length == 0:
    print("Gotta type something bud. You have 144 characters to speak your mind!")

