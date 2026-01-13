
def guess_number(low,high):
    while True:
        try:
            guess = int(input(f"Enter a number between {low} and {high} : "))
            if low <= guess <=high:
                return guess
            else:
                print(f"Please Enter a number between {low} and {high} :" )
        except ValueError:
            print("invalid input! Please enter a number.")

        