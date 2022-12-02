# Finding the top 10 most common words
fhand = open('romeo.txt')
count = dict()

for line in fhand:
    words = line.rstrip().split()
    for w in words:
        count[w] = count.get(w, 0) + 1
"""
lst = list()
for key, value in count.items():
    newTuple = (value, key)
    lst.append(newTuple)
"""
# list comprehension
# creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.
lst = [(value, key) for key, value in count.items()]
lst = sorted(lst, reverse=True)
for value, key in lst[:6]:
    print(key, value)