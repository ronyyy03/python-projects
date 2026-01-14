file_name = "tasks.txt"

def load_task():
    try:
        with open(file_name, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_task(tasks):
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(task)
            
def add_task(tasks,task):
    tasks.append("[] "+task)

def mark_done(tasks,index):
    if tasks[index].startswith("[]"):
        tasks[index]= tasks[index].replace("[]", "[D]", 1)

def delete_task(tasks,index):
    tasks.pop(index)

    
