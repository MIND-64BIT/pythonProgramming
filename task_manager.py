
# Task Manager

all_task = []
priority = ['       Low      ','     Medium     ','      High     ']

def addTask():
    print('\n\nADD TASK\n\n')
    print('date format: dd/mm/yy')
    date = input("Enter Date: ")
    task = input("Enter your task: ")
    print("1. Low\n2. Medium\n3. High")
    priority = input("Enter Priority of the Task: ")
    priority = '1'
    if priority.isdigit():
        print('PirorityError : invalid priority, prority set to low')
        priority = '1'
    elif int(priority) < 1 or int(priority) > 3:
        print("PriorityError : priority set to low")
        priority = '1'
    task = {
    'date' : date,
    'task' : task,
    'priority' : priority
        }
    
    task = {
    'date' : '31/12/1996',
    'task' : 'How To manage the maksing and the game',
    'priority' : '1'
        }
    
    all_task.append(task)
    print("Done...")

def removeTask():
    task_no = input("Enter task number to remove: ")
    if not task_no.isdigit():
        print("Invalid task number")
    elif int(task_no) - 1 > len(all_task):
        print("\nTaskNumberError : task number don't exist\n")

    else:
        removed_task = [all_task[int(task_no)-1]]
        temp,all_task = all_task,remove_task
        print(f"\nAbove is removed..")
        all_task.remove(all_task[int(task_no)-1])
        
def updateTask():
    pass

def printTask():
    print("    Sr    |       Date     |    Priority    |          Task          ")
    for i in range(len(all_task)):
        task_prio = priority[int(all_task[i].get('priority'))-1]
        print(f"     {i+1}    |   {all_task[i].get('date')}   |{task_prio}|          {all_task[i].get('task')}          ")

print('''     Welcome to Task Manager     ''')

while(True):
    choice = input("\n\n1.Add a new Task\n2.Remove a Task\n3.Update a Task\n4.Display all Task\n5.Exit\nEnter Choice: ")
    
    match(choice):

        case "1":
            addTask()

        case "2":
            removeTask()
        
        case "3":
            updateTask()

        case "4":
            printTask()

        case "5":
            exit()

        case _ :
            print("ChoiceError : invalid choice ")        





        
    
        
