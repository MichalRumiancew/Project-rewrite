import os

os.system("cls || clear")

# user_age = input("Give your age: ")

# result_age = int(user_age) + 20


# os.system("cls || clear")

# user_name = input("Give your name: ")

# print(user_name + "! Your age after 20 years will be: " + str(result_age))

################################################

# int_number = [1,2,3,4] # 10

# range(len(int_number)) => [0,1,2,3,4,5,6.....10]

#################################################

# EXIT_WORD = "quit"

# should_continue = True
# while should_continue:
#     os.system("cls || clear")
#     user_input = input("Give a numer to calculate the sqaure: ")

#     if user_input == EXIT_WORD:
#         should_continue = False
#     else:
#         sqaure = int(user_input) * int(user_input)
#         print(f"The square {sqaure}" + str(user_input == EXIT_WORD) + " asdfas")
#         input("Press enter to continue " )

# print("End of program")

##########################################################
EXIT_WORD = "end"

def print_menu():
    print("(1) - calculate squre")
    print("(2) - calculate cube")
    print("(3) - printing hello world")
    print("(4) - sort numbers")
    print(f"{EXIT_WORD} - to end program")

def square():
    user_input = input("Give a numer to calculate the sqaure: ")
    sqaure = int(user_input) * int(user_input)
    print(f"The square is {sqaure}")
    input("Press enter to continue " )

def cube():
    user_input = input("Give a number to calculate the cube: ")
    cube = int(user_input) * int(user_input) * int(user_input)
    print(f"The cube is {cube}")
    input("Press enter to continue") 

def print_hello_world():
    print("hello world :)")
    print("hello world :)")

def sorting_numbers():
    number_of_numbers = input("Give a number of numbers: ")
    list_of_numbers = []
    for _ in range(int(number_of_numbers)):
        number = input("Give a number: ") # "20"
        list_of_numbers.append(int(number))
    print(f"Your numbers are: {list_of_numbers}")
    #TODO implment soritng
    input("Press enter to continue") 

should_continue = True
while should_continue:
    os.system("cls || clear")
    print_menu()
    user_option = input("Choose the function by number: ")

    if user_option == EXIT_WORD:
        should_continue = False

    if user_option == "1":
        square()

    if user_option == "2":
        cube()
    
    if user_option == "3":
        print_hello_world()

    if user_option == "4":
        sorting_numbers()

print("End of program")
