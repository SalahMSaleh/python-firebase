from firebase import firebase
import struct
import time
from time import sleep


print('intialiaizing firebase object')    
firebase = firebase.FirebaseApplication('https://python-task-c5867.firebaseio.com/', None)


lastTODO_Task_data=firebase.get('/TODO_Task',None)
lastTODO_Mirror_data=firebase.get('/TODO_Mirror',None)
 
def check_TODO_Task():
    
    global lastTODO_Task_data
    global lastTODO_Mirror_data
    TODO_Task_data= firebase.get('/TODO_Task',None)

    if(lastTODO_Task_data!=TODO_Task_data):
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
            print('something changed in TODO_Task and something deleted')
            
def check_TODO_Mirror():

    global lastTODO_Task_data
    global lastTODO_Mirror_data
    TODO_Mirror_data= firebase.get('/TODO_Mirror',None)

    if(lastTODO_Mirror_data!=TODO_Mirror_data):
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
            print('something changed in TODO_Mirro and something deleted')
            
while(1):

    check_TODO_Task()
    time.sleep(1)
    check_TODO_Mirror()    
    time.sleep(1)
    
