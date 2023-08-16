class Dog:
    species = "Golden"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, sound = "Woof Woof"):
        return f'{self.name} barks {sound}'
    
    def details(self):
        return f'{self.name} is {self.age} Years Old'
    
class Golden(Dog):
    def __init__(self, name, age, nickname):
        super().__init__(name, age)
        self.nickname = nickname

    def bark(self, sound="Au au"):
        return super().bark(sound)

