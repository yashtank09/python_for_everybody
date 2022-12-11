import xml.etree.ElementTree as ET
import xml.etree.ElementPath as EP

# writing XML data
data = '''
    <person>
        <name>Chuck</name>
        <phone type="int1">
            +1 734 303 4456
        </phone>
        <email hide="yes" />
    </person>
'''

# Parsing XML data
XMLDataTree = ET.fromstring(data)
print(XMLDataTree) # Object address
print('Name: ', XMLDataTree.find('name').text) # prints text of tag/node
print('Attr: ', XMLDataTree.find('email').get('hide')) # prints attribute's value
