class Customer:
    def __init__(self, name):
        self.name = name
        self.wishlist = []

    def getName(self):
        return self.name
    
    def getWishList(self):
        return self.wishlist

    def addToWishlist(self, bookName):
        self.wishlist.append(bookName)

    def removeFromWishList(self, bookName):
        if bookName in self.wishlist:
            self.wishlist.remove(bookName)