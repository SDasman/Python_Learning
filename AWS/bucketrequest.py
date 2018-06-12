import requests

exposed_bucket = requests.get("https://s3.amazonaws.com/shijit-datt-a3-meetup/important-dontshare.txt.rtf")

print(exposed_bucket.content)
