from bs4 import BeautifulSoup
import requests

# url = "https://www.instagram.com/amosxhunter/"    # URL you want to read from internet
entry = input("Please enter the persons username: ")    # Asks user for input to finish URL
dynamicUrl = "https://www.instagram.com/" + entry + "/"    # The default path for an instagram URL + Users Input
print(dynamicUrl)

result = requests.get(dynamicUrl)    # Uses package to pull URL from the internet
doc = BeautifulSoup(result.text, "html.parser")    # Saves URL as variable called doc
print(doc)

followers = doc.find_all(string="followers")    # Searches doc for any instance of 'followers'
print(followers)    # Need to narrow the search results down to just find follower count itself.
