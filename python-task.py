from firebase import firebase
import time
from time import sleep


#intialiaizing firebase object.    
firebase = firebase.FirebaseApplication('https://python-task-c5867.firebaseio.com/', None)


#Last variables are to get the data in the objects for first time so it dosent trigger changes in the first time.
lastTODO_Task_data=firebase.get('/TODO_Task',None)
lastTODO_Mirror_data=firebase.get('/TODO_Mirror',None)


#A function to check TODO_Task. 
def check_TODO_Task():

    global lastTODO_Task_data
    global lastTODO_Mirror_data
    TODO_Task_data= firebase.get('/TODO_Task',None)

#Check for any changes from the last.
    if(lastTODO_Task_data!=TODO_Task_data):

#Check what changes happend by comparing the length of data for deletion length must decrease.
        if(len(str(TODO_Task_data))>=len(str(lastTODO_Task_data))):
            TODO_Mirror_patch= firebase.patch('/TODO_Mirror',TODO_Task_data)
            lastTODO_Task_data=TODO_Task_data
            lastTODO_Mirror_data=TODO_Task_data
            print('something changed in TODO_Task but nothing deleted')
        else:
            TODO_Mirror_delete=firebase.delete('/TODO_Mirror',None)
            TODO_Mirror_patch= firebase.patch('/TODO_Mirror',TODO_Task_data)
            lastTODO_Task_data=TODO_Task_data
            lastTODO_Mirror_data=TODO_Task_data
            print('something deleted')

#A function to check TODO_Mirror.            
def check_TODO_Mirror():

    global lastTODO_Task_data
    global lastTODO_Mirror_data
    TODO_Mirror_data= firebase.get('/TODO_Mirror',None)

#Check for any changes from the last.
    if(lastTODO_Mirror_data!=TODO_Mirror_data):

#Check what changes happend by comparing the length of data for deletion length must decrease.
        if(len(str(TODO_Mirror_data))>=len(str(lastTODO_Mirror_data))):
            TODO_Task_patch= firebase.patch('/TODO_Task',TODO_Mirror_data)
            lastTODO_Mirror_data=TODO_Mirror_data
            lastTODO_Task_data=TODO_Mirror_data
            print('something changed in TODO_Mirror but nothing deleted')
        else:
            TODO_Task_delete=firebase.delete('/TODO_Task',None)
            TODO_Task_patch= firebase.patch('/TODO_Task',TODO_Mirror_data)
            lastTODO_Mirror_data=TODO_Mirror_data
            lastTODO_Task_data=TODO_Mirror_data
            print('something deleted')

#A while loop to keep the program running            
while(1):

#Calling the checking funtions with delay to make sure everything patched to the firebase correctly
    check_TODO_Task()
    time.sleep(1)
    check_TODO_Mirror()    
    time.sleep(1)
    
