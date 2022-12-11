from urllib import request, parse, error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# This is API key for given service url
api_key = 42
serviceURL = "http://py4e-data.dr-chuck.net/json?"

address = input('Enter location: ')

param = dict()
param['address'] = address

if api_key is not False: param['key'] = api_key
# print(param)
# a = parse.urlencode(param)
# print(a)
url = serviceURL + parse.urlencode(param)

print('Retrieving', url)

uh = request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    # continue

# print(json.dumps(js, indent=4))

placeID = js['results'][0]['place_id']
print(placeID)