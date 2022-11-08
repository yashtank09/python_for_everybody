num = 0
total = 0
count = 0
while True:
    sval = input('Enter Number: ')
    # exit mechanism
    if sval == 'done':
        break

    # sanity checking for inputted value
    try:
        floatValue = float(sval)
    except:
        # continuation on bad input
        print("Error: Wrong Input!")
        continue
    total += floatValue
    count += 1

print('ALL DONE')
try:
    avrage = total / count
except:
    print('Please enter any number...\n Your input is invalid.')
print(total, count,)
