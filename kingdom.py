class Kingdom:
    def __init__(self):
        self.inventory = {"Star Wars": 10, 
                          "To Kill a Mockingbird" : 10, 
                          "1984" : 10, 
                          "The Great Gatsby" : 10,
                          "Animal Farm" : 10}
        self.history = []
        self.customers = []

    def getInventory(self):
        return self.inventory
    
    def completeTransaction(self, transaction):
        self.history.append(transaction)

        for x in transaction.getBookNames():
            if x in transaction.getCustomer().getWishList():
                transaction.getCustomer().removeFromWishList(x)
                self.removeFromInventory(x)


        # for book in transaction.getBookNames():
        #     transaction.getCustomer().removeFromWishList(book)
        #     self.removeFromInventory(book)

    def addCustomer(self, customer):
        self.customers.append(customer)

    def removeFromInventory(self, bookName):
        if bookName in self.inventory:
            placeHolder = self.inventory[bookName]
            self.inventory.update({bookName: placeHolder - 1})
        else:
            return False

    def returnDogQuantity(self, key):
        return self.inventory[key]
    
    def returnHistorySize(self):
        return len(self.history)
    
    def returnSpecificTransaction(self, index):
        return self.history[index - 1]