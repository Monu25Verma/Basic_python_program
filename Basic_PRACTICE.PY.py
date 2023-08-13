# PRINT HELLO WORLD

print("Hello World!")

# take name and age provide greeting msg
# user_name = input("Enter the username: ")
# age = int(input("enter the age: "))
# print("Today i turned ", age, "its my birthday tada.")

# celcius to faranide
c = 6
f = c + (9 / 5) + 32
print("6 celcius = ", f)

# feranide to celcius
f = 54
c = (f - 32) / 1.8
# print("54 feranide =", ('%.2f' % c))

# area of rectangle
# l = int(input("enter the length: "))
# w = int(input("enter the width: "))
# area = l * w

# print(area)
x = 50
if x % 2 == 0:
    print(x, "is even number")
else:
    print(x, "odd number")

# find min and max


def min_max(L):
    L.sort()
    minmax = {"Min": L[0], "Max": L[-1]}
    return minmax

L = [3, 4, 5, 89, 9, 3, 10]
minmax = min_max(L)
print('the Minimum value is: ', minmax["Min"])
print("the Maximum value is: ", minmax["Max"])







