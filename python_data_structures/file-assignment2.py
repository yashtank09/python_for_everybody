fh = open("mbox-short.txt")
count = 0

for line in fh:
    # line = line.rstrip()
    words = line.rstrip().split()
    # Guardians
    # if line == '':
    #     print("Skipped Lines")
    #     continue

    # Guardians a bit strong
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")
