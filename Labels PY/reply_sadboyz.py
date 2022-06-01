import tweepy
auth = tweepy.OAuthHandler("5aRRJGmXkMaV1zgWANQ6ewH18",
"jxgKQQbRZJkzbnAkRQwtdwjSq3zI9tGVWDlPDKIq8btX0O9g57")
auth.set_access_token("2422708117-rhZElHXGKPY9N0scj1K0AfqzktRpgPRNUt82GCy",
 "L5Kxlq4QLIYBPNVgcul6VGn7qGBnxueCZLx1SpmuXGBwp")
api = tweepy.API(auth)

tweetId = input("TweetID del tweet que se va a responder: \n")
reply = input("Escribe la respuesta del tweet: \n")

api.update_status(status = reply , in_reply_to_status_id = tweetId , auto_populate_reply_metadata=True)

print ("Done!")
input()
