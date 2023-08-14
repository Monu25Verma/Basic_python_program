def min_max(l):
    l.sort()
    result = {"Min": l[0], "Max": l[-1]}
    return result


input_value = [3, 4, 5, 89, 9, 3, 10]
minmax = min_max(input_value)
print('the Minimum value is: ', minmax["Min"])
print("the Maximum value is: ", minmax["Max"])

