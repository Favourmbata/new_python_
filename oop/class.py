class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} say hello!'


dog = Animal("Charley")
print(dog.speak())
