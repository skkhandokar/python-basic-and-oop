import datetime
import uuid

class Task:

    show_task=[]
    update=[]
    def __init__(self,tname,s1,ID):
        self.task_name=tname  
        self.Created_time=s1
        self.updated_time='NA'
        self.completed_time="NA"
        self.task_done='False'
        self.id=ID
        self.entrynew =[self.id, self.task_name,self.Created_time,self.updated_time,
                        self.task_done,self.completed_time]

        Task.show_task.append(self.entrynew)
       
       
    @staticmethod
    def update_task(task_no,task_up):
    #    self.taskno=task_no
    #    self.task=task_up
         Task.show_task[task_no][1]=task_up
         now = datetime.datetime.now()
         upt = now.strftime("%m/%d/%Y  %H:%M:%S")
         Task.show_task[task_no][3]=upt
         print("Task Update Succesfully")
    
    @staticmethod
    def complete_task(tskobj):
         now = datetime.datetime.now()
         upt = now.strftime("%m/%d/%Y  %H:%M:%S")    
         Task.show_task[tskobj][5]=upt
         Task.show_task[tskobj][4]='True'
         print("Task Complete Succesfully")
p=0
while True:
    print("\n")
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Task")
    print("4. Show Complete Tasks")
    print("5. Update Task")
    print("6. Mark A Task Complete")

    inp=int(input("Enter Option: "))

    if inp==1: 
       
        usertask= input('Enter New Task: ')
        now = datetime.datetime.now()
        s1 = now.strftime("%m/%d/%Y  %H:%M:%S")
        id=uuid.uuid1()

        tp=Task(usertask,s1,id)
        p=+1
        print('Task Created Succesfully')
        print("\n")           

    if inp==2:
     if len(Task.show_task)==0:
      print("There's no task")  
     print('\n')
     for j in range(len(Task.show_task)):
         for i in range(len(Task.show_task[j])):
           
           if i==0:
              print("ID - ",end="")
              print(Task.show_task[j][i])
           if i==1:
              print("Task - " + Task.show_task[j][i])
           if i==2:
              print("Created Time - " + Task.show_task[j][i])
           if i==3:
              print("Updated Time - " + Task.show_task[j][i])
           if i==4:
               print("Completed- " + Task.show_task[j][i])
           if i==5:
               print("Completed Time - " + Task.show_task[j][i])

         print('\n')
    
    if inp==3:
     f=0
     print('\n')
     for j in range(len(Task.show_task)):

        if Task.show_task[j][4]=='False':

              for i in range(len(Task.show_task[j])):

                  if i==0:
                     print("ID - ",end="")
                     print(Task.show_task[j][i])
                  if i==1:
                     print("Task - " + Task.show_task[j][i])
                  if i==2:
                     print("Created Time - " + Task.show_task[j][i])
                  if i==3:
                      print("Updated Time - " + Task.show_task[j][i])
                  if i==4:
                      print("Completed- " + Task.show_task[j][i])
                  if i==5:
                      print("Completed Time - " + Task.show_task[j][i])
              f=1
              print('\n')

    #  if f==0:
    #     print('No Complete Task\n')


    if inp==4:
      print('\n')
      f=0
      for j in range(len(Task.show_task)):
        if Task.show_task[j][4]=='True':
              for i in range(len(Task.show_task[j])):
                  if i==0:
                     print("ID - ",end="")
                     print(Task.show_task[j][i])
                  if i==1:
                     print("Task - " + Task.show_task[j][i])
                  if i==2:
                     print("Created Time - " + Task.show_task[j][i])
                  if i==3:
                      print("Updated Time - " + Task.show_task[j][i])
                  if i==4:
                      print("Completed- " + Task.show_task[j][i])
                  if i==5:
                      print("Completed Time - " + Task.show_task[j][i])
              print('\n')
              f=1
      if f==0:
        print('No Complete Task\n')

    
    if inp==5:
     f=0
     for j in range(len(Task.show_task)):
      if Task.show_task[j][4]=='True':   
         f=1
      if Task.show_task[j][4]=='False':
         f=0
     if f==1:
       print('No Task To update')    
     if f==0:   
        print("\n")
        print("Select Whice Task To Update")
        print("\n")
        for j in range(len(Task.show_task)):  
         if  Task.show_task[j][4]=='False':    
          print("Task No - ",end="")
          print( j+1) 
          for i in range(len(Task.show_task[j])):
           
           if i==0:
              print("ID - ",end="")
              print(Task.show_task[j][i])
           if i==1:
              print("Task - " + Task.show_task[j][i])
           if i==2:
              print("Created Time - " + Task.show_task[j][i])
           if i==3:
              print("Updated Time - " + Task.show_task[j][i])
           if i==4:
               print("Completed- " + Task.show_task[j][i])
           if i==5:
               print("Completed Time - " + Task.show_task[j][i])
               print('\n')
        ts=int(input("Enter Task No: "))
        task_up=input("Enter New Task: ")
        ts=ts-1
        Task.update_task(ts,task_up)
   
   
      
    if inp==6:
     f=0
     for j in range(len(Task.show_task)):
      if Task.show_task[j][4]=='True':   
         f=1
      if Task.show_task[j][4]=='False':
         f=0
     if f==1:
       print('No Task To complete')    
     if f==0:
        print("\n")
        print("Select Whice Task To Complete")
        print("\n")
        for j in range(len(Task.show_task)):  
          if  Task.show_task[j][4]=='False': 
              
            print("Task No - ",end="")
            print( j+1) 
            for i in range(len(Task.show_task[j])):
            
                if i==0:
                    print("ID - ",end="")
                    print(Task.show_task[j][i])
                if i==1:
                    print("Task - " + Task.show_task[j][i])
                if i==2:
                    print("Created Time - " + Task.show_task[j][i])
                if i==3:
                    print("Updated Time - " + Task.show_task[j][i])
                if i==4:
                    print("Completed- " + Task.show_task[j][i])
                if i==5:
                    print("Completed Time - " + Task.show_task[j][i])
                    print('\n')
        tsk=int(input("Enter Task No: "))   
        tsk=tsk-1
        Task.complete_task(tsk)  
  
           
                



