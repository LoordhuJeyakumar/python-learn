#Task Manager

tasks = []
task_counter = 1

def add_task(title):
    global task_counter
    tasks = {
        "id": task_counter, 
        "title": title, 
        "completed": False
        }
    tasks.append(tasks)
    task_counter += 1
    
def list_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} [{status}]')
        
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f'Task {task_id} marked as completed.')
            return
    print(f'Task {task_id} not found.')
    
#-----------------------------------------------
#Menu
#-----------------------------------------------

def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Exit")
    choice = input("Choose an option: ")
    return choice
#-----------------------------------------------
#Main App Loop
#-----------------------------------------------

def run_app():
    while True:
        choice = show_menu()
        if choice == "1":
            title = input("Task title: ")
            add_task(title)
            print("Task added.")
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Task ID: "))
                complete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        
#-----------------------------------------------
#break/continue demo
#-----------------------------------------------

def break_continue_demo():
    print("\nContinue Demo:")
    count = 0
    while count < 5:
        if count == 2:
            count += 1
            continue
        print(count)
        count += 1
        
#-----------------------------------------------
#Program Start
#-----------------------------------------------

if __name__ == "__main__":
    break_continue_demo()
    run_app()