# input
# def eval(x, y, o):
    # x = int(input("Enter x:"))
    # y = int(input("Enter y:"))
    # o = input("Enter an operator:")

    # process
def eval(x, y, op):    
    s = 0
    if op == "+":
        s = x + y
    elif op == "-":
        s = x - y
    elif op == "*":
        s = x * y
    elif op == "/":
        s = x / y
    
    return s

# r = eval(4, 5, "+")
# print(r)

# a = int(input("a = "))
# b = int(input("b = "))
# op = input("op =")

# r = eval(a, b, op)
# print(r)


# # output
# print(s)


#FUNCTION
#def <tên hàn> (function parameters/arguments):
# def sayHi(n):
#     print("Hi") #function body
#     print("Hi", n)
#     print("Bye bye")

# def add(x, y):
#     r = x + y
#     return r #cách nhau bằng dấu phẩy
#     # hàm không có return: non fruitful or else fruitful


# s = add(4, 5)
# print(s)

# sayHi("Nhung")
# sayHi("Huyen")