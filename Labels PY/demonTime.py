import tweepy
auth = tweepy.OAuthHandler("FMmQxpa3L5eI80hvGc9CsVWcV",
"OseyrQyAeA0UYV2UCzoZkCyGmA9Aw5Ugd2Na6lEp4pxAsNoBN9")
auth.set_access_token("2422708117-uSCk1pRBv1VnFd51zk0l2DNfZnxM0Qkw3UPjnPu",
 "04zzmF5b2GPhS8JcjGs7kExh2Zu8xtMVjPXiBkjrjR2QZ")
api = tweepy.API(auth)
print ("Labels Twitter")
print ("Twitter For DEMON TIME :3")
tweet = input("Escribe el Tweet: \n")
api.update_status(status =(tweet))
print ("Done!")
input()
