class Person():
    def __init__(self, name, age, hobbies, nationality):
        self.name = name
        self.age = age
        self.hobbies = hobbies
        self.nationality = nationality

    def display(self):
        print(self.name)
        print(self.age)
        print(self.hobbies)
        print(self.nationality)
person = Person("Kalp", 12, "Football, Running, Cycling, Cricket", "Indian")
person.display()

class Car(Person):
    def __init__(self, model, milage, color, n, a,  h, na):
        super().__init__(n, a, h, na)
        self.model = model
        self.milage = milage
        self.color = color

    def display(self):
        print(self.model)
        print(self.milage)
        print(self.color)
car = Car("BMW M5", "50,000", "Black", "Kalp", 12, "Football, Running, Cycling, Cricket", "Indian")
car.display()