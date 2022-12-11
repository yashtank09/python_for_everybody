import xml.etree.ElementTree as ET
import xml.etree.ElementPath as EP

# writing XML data
data = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>
'''

# Parsing XML data
stuff = ET.fromstring(data)

# storing list of xml tree tags
lst = stuff.findall('users/user')
print('User count: ', len(lst)) # Object address

# go through list and XML tree tag elements and prints users
for items in lst:
    print('Name: ',items.find('name').text)
    print('ID: ',items.find('id').text)
    print('Attribute: ',items.get('x'))