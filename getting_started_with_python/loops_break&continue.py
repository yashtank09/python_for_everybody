# keyword: break
# The break statement ends the current loop and jumps to the statement immediately following the loop

# Program to print inputted value until input is equal to `done`
while True:
    line = input('> ')
    if line == 'done':
        break  # if condition will be true break keyword will terminate the loop
    print(line)
print('DONE!')

print('Exited')
# keyword: continue
# The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration

# Program to print inputted value and if inputted value starts with `#` that line will not to be printed
while True:
    line1 = input('> ')
    if line1[0] == '#':
        continue  # if the given condition true then it will continue and print nothing
    if line1 == 'done':
        break
    print(line1)
print('Done!')
