# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()

# If we need to read line 33, and assign it to some variable
count = 0
increaseCount = 0
decreaseCount = 0
for line in Lines:
    if count == 0:
        count += 1
    elif count > 0:
        if line > Lines[count -1]:
            increaseCount += 1
            count += 1
        else:
            decreaseCount += 1
            count += 1
print(increaseCount)

