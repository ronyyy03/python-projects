def get_choice():
    while True:
        try:
            print("choose a operation :")
            print("1: addition")
            print("2: subtract")
            print("3: multiply")
            print("4: divide")
            print("5: Exit")

            choice = int(input("Enter you choice (1-5): "))
            if 1<= choice <=5:
                return choice
            else:
                print("please enter a number between 1 to 5 :")
        
        except ValueError:
            print("Envalid Input ! please Enter a number :")

def get_numbers():
    while True:
        try:
            a = float(input("Enter a first number :"))
            b = float(input("Enter secound number :"))
            return a,b
        except ValueError:
            print("Invalid Input! please enter numeric values")
        

