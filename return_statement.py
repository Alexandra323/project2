def full_name(first,last):
    return (f"{first.title()} {last.title()}")

# name = full_name("alexa", "butterfly")
#
# print(f"{name}, Welcome to class!")

def adding(a,b):
    return a+b

# total= adding(2,3)
#
# print(f"Total is {total}")
# print(f"Total is {adding(2,3)}")

def full_name_dict(first:str,last:str)->dict:
    result = {'first':first.title(), 'last': last.title()}
    return result

#print(full_name_dict("lena","zaiceva"))

#nums = [5,55,6,2,4,88, -9, 1, 0,456]

def find_number(nums_list, number):
    for num in nums_list:
        if num == number:
            print(f"I found {number}")
            break

#find_number(nums,0)

def desc_pizza(*toppings):
    print(f"We have only cheese pizza with following toppings: ")
    print(*toppings)

#desc_pizza("pepperoni", "mushroom", "bbq chicken")




