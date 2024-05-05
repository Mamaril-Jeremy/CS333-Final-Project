import unittest
from customer import Customer
from transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_getCustomer(self):
        myself = Customer("carlos")
        dogName = "shihtsu"
        myTransaction = Transaction(myself, dogName, 60)

        self.assertEqual(myTransaction.getCustomer().getName(), "carlos", "Name did not save properly")

    def test_getDogName(self):
        myself = Customer("carlos")
        dogName = "shihtsu"
        myTransaction = Transaction(myself, dogName, 60)

        self.assertEqual(dogName, myTransaction.getDogName(), "Dog name did not save properly")

    def test_getPrice(self):
        myself = Customer("carlos")
        dogName = "shihtsu"
        myTransaction = Transaction(myself, dogName, 60)

        self.assertEqual(60, myTransaction.getPrice(), "Price did not save properly")

if __name__ == '__main__':
    unittest.main()