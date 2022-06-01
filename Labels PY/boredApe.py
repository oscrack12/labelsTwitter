import tweepy
auth = tweepy.OAuthHandler("xI6xxsJ1H9OMGsw8cCw6hQJV8",
"ifmBmN29uK2sBufRqEwFSW0XADlj0FpwCzUdg2689IOlXpBwrc")
auth.set_access_token("2422708117-ZtwOxtn8INfIBRYfc9b8ROute91dZliJNq3aREf",
 "YCYvi3i9zAf2eRFW90DK45zXELESppfqRggSSWkJCUIla")
api = tweepy.API(auth)
print ("Labels Twitter")
print ("Twitter For Bored Ape Yacht Club")
tweet = input("Escribe el Tweet: \n")
api.update_status(status =(tweet))
print ("Done!")
input()
