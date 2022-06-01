import tweepy
auth = tweepy.OAuthHandler("5aRRJGmXkMaV1zgWANQ6ewH18",
"jxgKQQbRZJkzbnAkRQwtdwjSq3zI9tGVWDlPDKIq8btX0O9g57")
auth.set_access_token("2422708117-rhZElHXGKPY9N0scj1K0AfqzktRpgPRNUt82GCy",
 "L5Kxlq4QLIYBPNVgcul6VGn7qGBnxueCZLx1SpmuXGBwp")
api = tweepy.API(auth)
print ("IMG Labels Twitter")
print ("Twitter For sadboyz u.u")
filename = ("lol.JPG")
status = input("que quieres que diga el tweet??")
api.update_status_with_media(filename = (filename), status = (status))
print ("Done!")
input()
