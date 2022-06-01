import tweepy
auth = tweepy.OAuthHandler("OWQPvEP5ugxvYNi9ZUYHY8mnl",
"pUWKwGqmBBof8sIQ0zIDWgksA0l5MQYlgBGIcn7RdO52iPWVHo")
auth.set_access_token("2422708117-iGpySGUt8mV2ANcTvxmV49ec0ywgLDs5ab10879",
 "usa6kDYZUyhil35R4ZBtyT4BMkZqFD1T9LqxpYT1TUvm2")
api = tweepy.API(auth)
print ("Labels Twitter")
print ("Twitter For Oye Ta Chido Tu Tsuru")
tweet = input("Escribe el Tweet: \n")
api.update_status(status =(tweet))
print ("Done!")
input()
