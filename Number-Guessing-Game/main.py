from game import generate_number, check_guess

from utils import guess_number
def main():
    print("*** Number Guessing Game ***")

    low = 1
    high =100 

    secret_number = generate_number(low, high)
    attempts =0

    while True:
        guess = guess_number(low,high)
        attempts+=1
        
        result = check_guess(secret_number,guess)

        if result== "low":
            print("Too low ! guess again .")
        elif result =="high":
            print("Too high ! guess again")
        else:
            print(f" Congrats! You guess correct number in {attempts} attempts .")
            break

if __name__=="__main__":
    main()
