import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
dict = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        dict[word] = dict.get(word, 0) + 1
print(dict)