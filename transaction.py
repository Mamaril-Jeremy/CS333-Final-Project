class Transaction:
    def __init__(self, customer, book_names, price, date):
        self.customer = customer 
        self.book_names = book_names
        self.price = price
        self.date = date

    def getCustomer(self):
        return self.customer
    
    def getBookNames(self):
        return self.book_names
    
    def getPrice(self):
        return self.price
    
    def getDate(self):
        return self.date
    