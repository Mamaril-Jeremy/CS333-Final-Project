class Customer:
    def __init__(self, name):
        self.name = name
        self.wishlist = []

    def getName(self):
        return self.name
    
    def getWishList(self):
        return self.wishlist

    def addToWishlist(self, dogName):
        self.wishlist.append(dogName)

    def removeFromWishList(self, dogName):
        if dogName in self.wishlist:
            self.wishlist.remove(dogName)