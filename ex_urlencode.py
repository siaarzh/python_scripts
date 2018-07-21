from urllib.parse import urlencode

f = { 'eventName' : 'myEvent', 'eventDescription' : 'cool event'}

print(urlencode(f))