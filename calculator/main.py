from operations import add,sub,mul,div

from utils import get_choice, get_numbers

def main():
    print("Calulator")

    while True:
       
        choice = get_choice()
            
        if choice == 5:
            print("Thank you for using calculator.")
            break
            
        a,b = get_numbers()
            
        match choice:
            case 1:
                    result= add(a,b)
            case 2:
                    result= sub(a,b)
            case 3:
                    result= mul(a,b)
            case 4:
                    result= div(a,b)

        print(f"result: {result}")

    print()

if __name__=="__main__":
        main()
