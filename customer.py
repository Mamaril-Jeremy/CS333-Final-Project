class Customer:
    def __init__(self, name):
        self.name = name
        self.history = []

    def getName(self):
        return self.name
    
    def getHistory(self):
        return self.history

    def addToHistory(self, dogName):
        self.history.append(dogName)