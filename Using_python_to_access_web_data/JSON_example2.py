import json
input = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
        },
    "email": {
        "hide": "yes"
    }
}
'''

info = json.loads(input)
print('Name', info['name'])
print('Hide', info['email']['hide'])