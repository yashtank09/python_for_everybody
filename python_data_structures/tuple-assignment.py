"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
handle = open("mbox-short.txt")
list_hours = list()
counts = dict()
for line in handle:
    words = line.rstrip().split()
    # Finding lines which contains 'From'
    if len(words) < 3 or words[0] != 'From':
        continue
    # Finding index of `:` from line which is represents time
    time = line.find(":")
    # adding value of hour and count its frequency
    counts[line[time - 2:time]] = counts.get(line[time - 2:time], 0) + 1

# adding key, value pair tuples in list using comprehensive list
list_hours = [(key, value) for key, value in counts.items()]
list_hours.sort()

for key, value in list_hours:
    print(key, value)
