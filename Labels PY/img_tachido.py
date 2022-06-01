import tweepy
auth = tweepy.OAuthHandler("OWQPvEP5ugxvYNi9ZUYHY8mnl",
"pUWKwGqmBBof8sIQ0zIDWgksA0l5MQYlgBGIcn7RdO52iPWVHo")
auth.set_access_token("2422708117-iGpySGUt8mV2ANcTvxmV49ec0ywgLDs5ab10879",
 "usa6kDYZUyhil35R4ZBtyT4BMkZqFD1T9LqxpYT1TUvm2")
api = tweepy.API(auth)
print ("IMG Labels Twitter")
print ("Twitter For DemonTIme ")
filename = ("lol.JPG")
status = input("que quieres que diga el tweet??")
api.update_status_with_media(filename = (filename), status = (status))
print ("Done!")
input()
