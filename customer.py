class Customer:
    def __init__(self, name):
        self.name = name
        self.wishlist = []

    def getName(self):
        return self.name
    
    def getWishList(self):
        return self.wishlist

    def addToHistory(self, dogName):
        self.wishlist.append(dogName)