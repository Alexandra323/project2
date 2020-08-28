import time

def greet_user():
    print("Welcome to class!")

def greet_user1(name, company = "google"):  #arguments
    print(f"{company}Welcome to LevelUp, {name}!")


"""execute the code/call the function"""
temp = "Inom"
greet_user()
greet_user1("Alexa", "Weddingigs") #parametr
time.sleep(2)
greet_user1(temp)

#greet_user1(input("enter company name: "))

