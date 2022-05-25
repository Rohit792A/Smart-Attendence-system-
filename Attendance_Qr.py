import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys  #provides modules to access variables and functions
import time
import pybase64  #used for encoding the data


# starting the webcam using opencv 
cap = cv2.VideoCapture(0)

fob=open('attendence.txt','a+')  #creating a file to store attendence record

names=[]  #names of the students

#function for writing the data into text file

def enterData(z):
    if z in names:   
        pass
    else:
        names.append(z)
        z=''.join(str(z))
        print(z)
        fob.write(z+'\n')
    return names

print('Reading Code...')



#function for check the data is present or not

def checkData(data):
    data=str(data)    
    if data in names:
        print('Already Present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'Present done')
        enterData(data)

#command to read the camera frame  
while True:
    _, frame = cap.read() 
    decodedObjects = pyzbar.decode(frame)  #decoding the frame and  storing it
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)   #used to add delay in program
       
    cv2.imshow("Frame", frame)

#closing the program when s is pressed
    
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.destroyAllWindows()
        break
    
fob.close()
