import psycopg

def displayMenu():
    try:
        print("1. View a dog by breed.")
        print("2. Adopt a dog.")
        print("3. Exit")
        selection = int(input("\nWhat would you like to do? "))
        
        if selection >= 1 and selection <= 3:
            return selection
        else:
            raise ValueError("Invalid selection. Please choose between 1 and 3.")   
    except ValueError as e:
        print(e)
        return -1
    
def viewDogByBreed():
    pass

def adoptADog():
    pass

def main():
    print("Welcome to Dog Kingdom! Here is where you can view dogs of any breed and adopt them!")
    print("You can view dogs by breed, and then decide if you would like to adopt them!")
    print("Let's get started! Ready to view some cute dogs?\n")

    selection = displayMenu()

    while(selection != 3):
        if(selection == 1):
            viewDogByBreed()
        elif(selection == 2):
            adoptADog()
        else:
            break

    return 0

if __name__ == "main":
    main()