#Used to make requests
import urllib.request
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()
x = urllib.request.urlopen("https://pornhub.com", context=context)

print(x.read())