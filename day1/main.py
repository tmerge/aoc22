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
    

    # get values sorted and solve second part of the day
    sorted_x = sorted(x)

    print(f"Second most value: {sorted_x[-2]}")
    print(f"Second most value: {sorted_x[-3]}")
    print(f"Sum of the top three: {sorted_x[-1] + sorted_x[-2] + sorted_x[-3]}")