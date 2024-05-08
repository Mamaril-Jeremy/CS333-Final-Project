# Integration Tests
import unittest
from customer import Customer
from transaction import Transaction
from kingdom import Kingdom

class TestKingdom(unittest.TestCase):
    def setUp(self):
        self.kingdom = Kingdom()

    def test_addCustomer(self):
        customer = Customer("John")
        self.kingdom.addCustomer(customer)
        self.assertIn(customer, self.kingdom.getCustomers())

    def test_completeTransaction(self):
        customer = Customer("Jeremy")
        dog_name = "husky"
        transaction = Transaction(customer.getName(), dog_name, 100)
        self.kingdom.completeTransaction(transaction)
        self.assertIn(transaction, self.kingdom.getHistory())
        self.assertNotIn(dog_name, self.kingdom.getInventory())

    def test_getInventory(self):
        inventory = self.kingdom.getInventory()
        self.assertIsInstance(inventory, dict)
        self.assertTrue(len(inventory) > 0)

    def test_getCustomers(self):
        customers = self.kingdom.getCustomers()
        self.assertIsInstance(customers, list)
        self.assertEqual(len(customers), 0)

    def test_addDuplicateCustomer(self):
        customer1 = Customer("John")
        customer2 = Customer("Joe")
        self.kingdom.addCustomer(customer1)
        self.kingdom.addCustomer(customer2)
        self.assertEqual(len(self.kingdom.getCustomers()), 2)

    def test_getCustomerNamePerTransaction(self):
        customer = Customer("Mike")
        new_transaction = Transaction(customer, "shihtzu", 100)
        self.assertEqual(new_transaction.getCustomer().getName(), "Mike")

    def test_removeFromInventoryExistingDog(self):
        kingdom = Kingdom()
        dog_name = "poodle"
        kingdom.removeFromInventory(dog_name)
        self.assertNotIn(dog_name, kingdom.getInventory())

    def test_removeFromInventoryNonExistingDog(self):
        kingdom = Kingdom()
        non_existing_dog = "unicorn"
        result = kingdom.removeFromInventory(non_existing_dog)
        self.assertFalse(result)

    def test_getCustomerHistoryPerTransaction(self):
        kingdom = Kingdom()
        customer = Customer("Mike")
        new_transaction = Transaction(customer, "shihtzu", 100)
        kingdom.addCustomer(customer)
        customer.addToHistory(new_transaction.getDogName())
        kingdom.completeTransaction(new_transaction)
        self.assertIn("shihtzu", kingdom.getCustomers()[0].getHistory())

    def test_getTransactionUponAddingCustomer(self):
        kingdom = Kingdom()
        customer = Customer("Mike")
        new_transaction = Transaction(customer, "shihtzu", 100)
        kingdom.completeTransaction(new_transaction)
        self.assertEqual(kingdom.getHistory()[0].getCustomer().getName(), "Mike")
        self.assertEqual(kingdom.getHistory()[0].getDogName(), "shihtzu")
        self.assertEqual(kingdom.getHistory()[0].getPrice(), 100)

if __name__ == '__main__':
    unittest.main()
