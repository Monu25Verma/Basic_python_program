def sum_(x):

    count = 0
    for i in x:
        if i < 0:
            print(0)
        else:
            count = count + i
    print(count)


sum_([3, 5, 8, 9, 2])