import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def test_getName(self):
        customer = Customer("Jeremy")
        self.assertEqual(customer.getName(),"Jeremy", "Invalid Name")

    def test_getHistory(self):
        customer = Customer("Mary")
        customer.addToHistory("golden retriever")
        customer.addToHistory("husky")

        self.assertIn("golden retriever", customer.getHistory(), "Dog name not in history.")
        self.assertNotIn("shihtsu", customer.getHistory(), "Dog name incorrectly in history.")

    def test_addToHistory(self):
        customer = Customer("Nathan")
        customer.addToHistory("golden retriever")
        customer.addToHistory("germanshepherd")
        customer.addToHistory("chihuahua")

        self.assertIn("chihuahua", customer.getHistory(), "Dog name not in history.")
        self.assertNotIn("waterdog", customer.getHistory(), "Dog name incorrectly in history.")

if __name__ == '__main__':
    unittest.main()