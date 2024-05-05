import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def test_getName(self):
        customer = Customer("Jeremy")
        self.assertEqual(customer.getName(),"Jeremy", "Invalid Name")

    def test_addToWishlist(self):
        customer = Customer("Carlos")
        sampleBook1 = "Reckless Love"
        sampleBook2 = "Maybe Someday"

        customer.addToWishlist(sampleBook1)
        customer.addToWishlist(sampleBook2)

        self.assertIn(sampleBook1, customer.getWishList(), "Book name not in wishlist.")
        self.assertIn(sampleBook2, customer.getWishList(), "Book name not in wishlist.")

        self.assertNotIn("Star Wars", customer.getWishList(), "Book name incorrectly in wishlist.")

    def test_removeFromWishList(self):
        customer = Customer("Mary")
        customer.addToWishlist("Reckless Love")
        customer.addToWishlist("Maybe Someday")
        customer.removeFromWishList("Reckless Love")

        self.assertIn("Maybe Someday", customer.getWishList(), "Book name not in wishlist.")
        self.assertNotIn("Reckless Love", customer.getWishList(), "Book name incorrectly in wishlist.")

    # class Customer:
    # def __init__(self, name):
    #     self.name = name
    #     self.wishlist = []

    # def getName(self):
    #     return self.name
    
    # def getWishList(self):
    #     return self.wishlist

    # def addToHistory(self, dogName):
    #     self.wishlist.append(dogName)

if __name__ == '__main__':
    unittest.main()