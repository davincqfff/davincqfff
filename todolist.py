tasks=[]

def addTask():
    task=input("enter task:")
    tasks.append(task)
    print(f"Task'{task}'added to the list")
    
def deleteTask():
    task=input("enter a task to delete")
    if task in tasks:
        tasks.remove(task)
        print(f"Task'{task}'remove from the list")
    else:
        print(f"Task'{task}'task not found")
        
def listTask():
    if not tasks:
        print("No tasks available")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\nTo do list @davincqfff")
    print("1.add task")
    print("2.list task")
    print("3.delete task")
    print("4.out")
    
    pilihan=input("pilih 1-4: ")
    
    if pilihan=="1":
        addTask()
    elif pilihan=="2":
        listTask()
    elif pilihan=="3":
        deleteTask()
    elif pilihan=="4":
        print("print anda keluar")
        break
    else:
        print("pilihan tidak valid")