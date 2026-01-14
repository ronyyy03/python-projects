from utils import get_choice, get_task_input
from todo import load_task, save_task, add_task,mark_done,delete_task

def show_tasks(tasks):
    if not tasks:
        print("no task available")
        return
    
    for i ,task in enumerate(tasks,start=1):
        print(f"{i}:{task}")

def main():
    tasks = load_task()

    while True:
        choice = get_choice()

        if choice ==1:
            task = get_task_input()
            add_task(tasks,task)
            save_task(tasks)
            print("task added ")
            
        elif choice ==2:
            show_tasks(tasks)

        elif choice ==3:
            show_tasks(tasks)
            try:
                index = int(input("enter the index of task to be mark as done :"))-1
            except ValueError:
                print("Please Enter a valid number :")
                continue
            mark_done(tasks,index)
            save_task(tasks)
            print("task mark as done .")

        elif choice ==4:
            show_tasks(tasks)
            try:
                index =int(input("enter the index of task to be deleted :")) -1
            except ValueError:
                print("enter a valid number :")
            delete_task(tasks,index)
            save_task(tasks)
            print("task is deleted")

        elif choice==5:
            print("Bye, Thank you")
            break

if __name__=="__main__":
    main()



                