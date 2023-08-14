# type 1
def swap_no(x, y):
    x, y = y, x
    print("x =", x, "y =", y)


swap_no(20, 30)


# type 2

def swap_(x, y):
    temp = x
    x = y
    y = temp
    print("x =", x, "y =", y)


swap_(20, 9)










