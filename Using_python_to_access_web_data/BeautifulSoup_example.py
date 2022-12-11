# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or install using
#       - pip install beautifulsoup4
# and unzip it in the same directory as this file

from bs4 import BeautifulSoup
from urllib import request, parse, error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www."+input("Enter Url - ")
# url = "https://www.github.com"
html = request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))