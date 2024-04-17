class Transaction:
    def __init__(self, customer, dog_names, price, date):
        self.customer = customer 
        self.dog_names = dog_names
        self.price = price
        self.date = date

    def getCustomer(self):
        return self.customer
    
    def getDogNames(self):
        return self.dog_names
    
    def getPrice(self):
        return self.price
    
    def getDate(self):
        return self.date
    