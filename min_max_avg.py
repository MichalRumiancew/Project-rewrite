# a = 2
# b = 6

# def my_min(a,b):
#     if b<a:
#         print(b)
#     else:
#         print(a)
#     pass


# def my_max(a,b):
#     if b>a:
#         print(b)
#     else:
#         print(a)
#     pass
    

# def my_avg(a,b):
#      avg = a + b / 2
#      print(avg)
    

# print(my_min(2,6))
# print(my_max(2,6))
# print(my_avg(2,6))

list_1 = [2,5,7,8,3,5,2,9,6,0]
list_2 = [1,4,5,7,4,3,4,5,7,7,8,3,3,33,4,44,12,75,23]

def my_min(my_list):
    min = my_list[0]
    for element in my_list:
        if element < min:
            min = element
    print(min)



my_min(list_1)
my_min(list_2)

# test 