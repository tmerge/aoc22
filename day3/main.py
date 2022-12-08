# array of different items in lower case
items = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# store all splited in a list and sum
rucksacksSet = []
sum = 0

# function to find duplicates in string
def find_duplicates(arr1, arr2):
    
    # store duplicate items from arrays
    x = []
    
    # remove duplicate values in each array
    arr1 = set(arr1)
    arr2 = set(arr2)

    for c in arr1:
        if c in arr2:
            # append c if the char was found in arr2
            x.append(c)
    return x

with open('input.txt') as rucksacks:
    for r in rucksacks.readlines():
        # prepare everything for duplicate check
        lofr = len(r)
        half = int(lofr / 2)

        # check for duplicates
        titems = find_duplicates(r[:half], r[half:])
        
        for i in titems:
            # skip if the array is empty
            if len(titems) <= 0:
                continue
            if i.isupper():
                # convert uppercase to lower case to get values based of lower chars
                i = i.lower()
                sum += items.index(i) + 27
            else:
                sum += items.index(i) + 1
    
    # print the sum of the calc before
    print(f'The sum of all items are: {sum}')