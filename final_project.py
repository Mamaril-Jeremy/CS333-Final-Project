from customer import Customer
from kingdom import Kingdom
from transaction import Transaction
import requests

def displayMenu():
    try:
        print("\n\nWelcome!")
        print("1. View a dog by breed.")
        print("2. Adopt a dog.")
        print("3. View Customer History")
        print("8. Exit")
        selection = int(input("\nWhat would you like to do? "))
        
        if selection not in range(1, 5):
            raise ValueError("Invalid selection. Please choose between 1 and 4.")   
        return selection
    except ValueError as e:
        print(e)
        return -1
    
def viewDogByBreed(kingdom):
    try:
        print("\nFrom our inventory, select which dog you would like to view by breed!\n")
        for i, dog in enumerate(kingdom.keys(), start=1):
            print(f"{i}. {dog}")

        dog_index = int(input()) - 1
        dog_breed = list(kingdom.keys())[dog_index]

        if kingdom[dog_breed]:
            print("\nSelect a sub-breed:")
            for i, sub_breed in enumerate(kingdom[dog_breed], start=1):
                print(f"{i}. {sub_breed}")
            sub_breed_index = int(input()) - 1
            sub_breed = kingdom[dog_breed][sub_breed_index]
            url = f"https://dog.ceo/api/breed/{dog_breed}/{sub_breed}/images/random/1"
        else:
            sub_breed = ""
            url = f"https://dog.ceo/api/breed/{dog_breed}/images/random/1"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "success":
            image_url = data["message"]
            print(f"Here's a cute {sub_breed} {dog_breed}: {image_url}")
        else:
            print("Failed to fetch the dog image.")
    except Exception as e:
        print(f"An error occurred: {e}")

def adoptADog(kingdom):
    try:
        dog_breed = ""
        sub_breed = ""

        customer_name = input("\nThank you for choosing to adopt a dog! Please tell us your name! ")
        new_customer = None
        for customer in kingdom.getCustomers():
            if customer.getName() == customer_name:
                new_customer = customer
                break
        if new_customer is None:
            new_customer = Customer(customer_name)
            kingdom.addCustomer(new_customer)

        print("\nPlease tell us which breed you would like to adopt.")
        for i, dog in enumerate(kingdom.getInventory().keys(), start=1):
            print(f"{i}. {dog}")

        dog_index = int(input()) - 1
        dog_breed = list(kingdom.getInventory().keys())[dog_index]

        if kingdom.getInventory()[dog_breed]:
            print("\nSelect a sub-breed:")
            for i, sub_breed in enumerate(kingdom.getInventory()[dog_breed], start=1):
                print(f"{i}. {sub_breed}")
            sub_breed_index = int(input()) - 1
            sub_breed = kingdom.getInventory()[dog_breed][sub_breed_index]

        new_transaction = Transaction(customer_name, sub_breed+dog_breed, 100)
        kingdom.completeTransaction(new_transaction)
        new_customer.addToHistory(sub_breed+" "+dog_breed)

        print(f"\nThank you so much for adopting a {sub_breed} {dog_breed} today! We hope to see you again soon!")

    except Exception as e:
        print(f"An error occurred: {e}")

def viewCustomerHistory(kingdom):
    customer_name = input("\nLet's determine if you're a returning customer! Please enter your name: ")
    customers = kingdom.getCustomers()
    for customer in customers:
        if customer.getName() == customer_name:
            history = customer.getHistory()
            print("Your adopted dogs: ")
            for dog in history:
                print(dog)
        else:
            print("You are not a returning customer. Why not adopt a dog?!")
        
def main():
    print("Welcome to Dog Kingdom! Here is where you can view dogs of any breed and adopt them!")
    print("You can view dogs by breed, and then decide if you would like to adopt them!")
    print("Let's get started! Ready to view some cute dogs?\n")

    newKingdom = Kingdom()
    selection = 0

    while selection != 4:
        selection = displayMenu()
        if selection == 1:
            viewDogByBreed(newKingdom.getInventory())
        elif selection == 2:
            adoptADog(newKingdom)
        elif selection == 3:
            viewCustomerHistory(newKingdom)
        else:
            break

    return 0

if __name__ == "__main__":
    main()
