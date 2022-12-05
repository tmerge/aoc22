# store all sums in a list
x = []
sum = 0
max = 0
with open('input.txt', 'rt') as data:
    # loop through the data and select all values and sum it up
    for i in data:
        if i == '\n':
            x.append(sum)
            sum = 0
            continue
        sum += int(i)
    # search for max value 
    for e in x:
        if e > max:
            max = e
    # print result of max search
    print(f'Max value: {max}')