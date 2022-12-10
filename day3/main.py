# array of different items in lower case
items = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# store all splited in a list and sum
rucksacksSet = []
sum_one = 0
sum_two = 0
counter = 0
tmp_r = []

# function to find duplicates in three strings
def find_duplicates_3(arr1, arr2, arr3):
    x = []

    arr1 = set(arr1)
    arr2 = set(arr2)
    arr3 = set(arr3)

    for c in arr1:
        if c in arr2 and c in arr3:
            x.append(c)
    return x

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
        
        tmp_r.append(r)
        counter += 1

        # get each three rucksacks to proceed
        if counter == 3:
            ttitems = find_duplicates_3(tmp_r[0].rstrip(), tmp_r[1].rstrip(), tmp_r[2].rstrip())
            tmp_r = []
            counter = 0

            for it in ttitems:
                # skip if the array is empty
                if len(ttitems) <= 0:
                    continue
                if it.isupper():
                # convert uppercase to lower case to get values based of lower chars
                    it = it.lower()
                    sum_two += items.index(it) + 27
                else:
                    sum_two += items.index(it) + 1

        # check for duplicates
        titems = find_duplicates(r[:half], r[half:])
        #ttitems = find_duplicates()
        
        for i in titems:
            # skip if the array is empty
            if len(titems) <= 0:
                continue
            if i.isupper():
                # convert uppercase to lower case to get values based of lower chars
                i = i.lower()
                sum_one += items.index(i) + 27
            else:
                sum_one += items.index(i) + 1
    
    # print the sum of the calc before
    print(f'The sum of all items are: {sum_one}')

    # print the sum of second part of daily task
    print(f'The sum of all items are based on three rucksacks: {sum_two}')