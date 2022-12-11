#urllib is a package that collects several modules for working with URLs: urllib. request for opening and reading URLs. urllib. error containing the exceptions raised by urllib.
import urllib.request, urllib.parse, urllib.error

# `urllib.request.urlopen()` Define function and classes to open urls
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())