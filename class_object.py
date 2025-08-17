class Dog():
    def __init__(self, name, age):
        self.dog_name = name
        self.dog_age = age
    
    def description(self):
        return f"The Dog with name {self.dog_name} is {self.dog_age} years old"
    
    def sound(self, dog_sound):
        return f"Dog {self.dog_name} speaks {dog_sound}"
    

miles = Dog("miles", 4)
print(miles.description())
print(miles.sound("Woof Woof"))

charlie = Dog("Charlie", 10)
print(charlie.description())
print(charlie.sound("Bow Wow"))