import tweepy
auth = tweepy.OAuthHandler("OWQPvEP5ugxvYNi9ZUYHY8mnl",
"pUWKwGqmBBof8sIQ0zIDWgksA0l5MQYlgBGIcn7RdO52iPWVHo")
auth.set_access_token("2422708117-iGpySGUt8mV2ANcTvxmV49ec0ywgLDs5ab10879",
 "usa6kDYZUyhil35R4ZBtyT4BMkZqFD1T9LqxpYT1TUvm2")
api = tweepy.API(auth)

tweetId = input("TweetID del tweet que se va a responder: \n")
reply = input("Escribe la respuesta del tweet: \n")

api.update_status(status = reply , in_reply_to_status_id = tweetId , auto_populate_reply_metadata=True)

print ("Done!")
input()
