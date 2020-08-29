class Dog():
    """General class about dog"""
    def __init__(self,breed,name):
    #Attributes
        self.breed = breed
        self.name = name

    #Behavior, methods
    def bark(self):
        print("wouf, wouf!")

mydog = Dog("German shepard", "Rex")  #object is the instance(representative) of the class
print(mydog.breed)
print(mydog.name)
mydog.bark()
his_dog = Dog(name="Hazel", breed="Pudel")
print(his_dog.name)
print(his_dog.breed)
