tweet = input('Please tweet here: ')
tweet_length = len(tweet)
print('Total length of this tweet was ' + str(tweet_length) + '.')

if tweet_length <= 140:
    print("Good Job - Twitter works and tweet length is solid!")
elif tweet_length > 140:
    print("Twitter is still good, your tweet is not. (Too Long). ")
elif tweet_length == 0:
    print("Gotta type something bud.")

