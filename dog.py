class Dog:
    name  = ""
    breed = ""
    
    def __init__(self, n, b):
        self.name = n
        self.breed = b
        
    def speak(self):
        return "Woof!"