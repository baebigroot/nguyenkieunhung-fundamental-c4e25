# #Ex 7:
# def remove_dollar_sign(s):
#     print(s.replace("$", ""))
#     return s.replace("$", "")

# # s = remove_dollar_sign("$80% percent of $life is to show $up")

# #Ex 8:
# string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
# if string_with_no_dollars == "80% percent of life is to show up":
#     print("Your function is correct")
# else:
#     print("Oops, there's a bug")

# #Ex 9:
# def get_even_list(l):
#     even = []
#     for i in l:
#         if i % 2 == 0:
#             even.append(i)
#     print(even)
#     return even
    
# get_even_list([1, 4, 5, -1, 10])

# #Ex 10: 
# even_list = get_even_list([1, 2, 5, 9, -10, 6])

# if set(even_list) == set([2, -10, 6]):
#     print("Your function is correct")
# else:
#     print("Ooops, bugs detected")

#Ex 11 & 12:
def is_inside(x, y):
    r_height = y[1] + y[3]
    r_width = y[0]+ y[2]
    if (y[1] < x[1] < r_height) and (y[0] < x[0] < r_width) :
        return True
    else:
        return False

print(is_inside([100, 120], [100, 120, 140, 60]))


