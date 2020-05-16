import random
import string

def private_url_maker():
    url = ""
    while len(url) < 6:
        url = random.choice(string.ascii_letters) + url
    return url
