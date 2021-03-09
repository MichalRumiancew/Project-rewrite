# # # # # # # # # # # # # # # 
# :)                        #
# # # # # # # # # # # # # # #

list_to_find_min = [9,6,7,4,9,1,6,7,8]
list_to_find_min_2 = [12,6,7,4,9,1,-6,7,8,1,6,0,2,5,3]

def my_min(my_list):
    current_min = my_list[0]
    for elem in my_list:
        if elem < current_min:
            current_min = elem

    return current_min
    
    

min_from_1 = my_min(list_to_find_min)
# min_from_2 = my_min(list_to_find_min_2)

# print(f"Pierwszy min: {min_from_1} a drugi min: {min_from_2}")

def my_min_from_two_numbers(a, b):
    if a < b:
        return a
    else:
        return b


#min_age = my_min_from_two_numbers(8, 3)
#print(f"Younger girl is {min_age} yeasr old")





def is_in_list(my_list, to_find):
    print("You are using my fun called: is_in_list")
    for elem in my_list:
        print(f"elem = {elem}, to_find = {to_find}")
        if elem == to_find:
            return True
    return False

list_to_test = ["a","b","c","z","f","o"]
element_to_find = "o"

#is_in_list(list_to_test, element_to_find) # Warring why are you ignoring return resutl



# its_good_list = ["a","b","c","z","f","o"]
# its_another_good_list = ["1","2","3","4"]
# ["a1","b2","c3","z4","f","o"]
def cocat_elements_between_lists(first_list, second_list):
    result_list = []

    #4
    min_length = my_min_from_two_numbers(len(first_list), len(second_list))
    for index in range(min_length):
        new_element = first_list[index] + second_list[index]
        result_list.append(new_element)
    # 8 > 4
    
    if len(first_list) > len(second_list):
        for index in range(min_length, len(first_list)):
            result_list.append(first_list[index])

    if len(second_list) > len(first_list):
        for index in range(min_length, len(second_list)):
            result_list.append(second_list[index])

    return result_list

#################0   1   2    3   4   5   6   7
first_list = ["a","b","c","z","f","o","h","t"]
second_list = ["1","2","3","4"]
result = cocat_elements_between_lists(second_list, first_list)
print(result)


def print_user_data(name, age, street):
    print("User name is " + str(name))