class Transaction:
    def __init__(self, customer, dog_name, price):
        self.customer = customer 
        self.dog_name = dog_name
        self.price = price

    def getCustomer(self):
        return self.customer
    
    def getDogName(self):
        return self.dog_name
    
    def getPrice(self):
        return self.price
    