
def get_choice():
    while True:
        try:
            print("\n TO DO LIST ")
            print("1: add task")
            print("2: view task")
            print("3: Mark task as done ")
            print("4: Delete task")
            print("5: Exit")

            choice = int(input("Enter choice (1-5): "))
            
            if  1<= choice <=5:
                return choice
            else:
                print("Please ! choose between 1 to 5 :")
        except ValueError as e:
            print("Please eneter a number,", e)
    
def get_task_input():
    task = input("Enter task description :").strip()
    return task


