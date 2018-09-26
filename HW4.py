#Ashley Rackley / HW 4 / 9-26-2018
from threading import Thread, Lock
#intialize mutex
mutex = Lock()
#Def the variable given in assignment
CAN_message_1= [0x01, 0x40, 0x00, 0x00, 0x00]

#Decoding function
def CANDecode():
  #Checks to see if mutex is locked/unlocked
  mutex.acquire()
  #Masks the first 2 MSB of the first bite 
  CAN_message_1[0]=CAN_message_1[0] & 0x3f
  #Decodes CAN Message
  decoded = (CAN_message_1[0] << 3) + (CAN_message_1[1] >> 5)
  #Display decoded value
  print(decoded)
  #Unlocks Mutex
  mutex.release()

def CANUpdate():
  #Checks to see if mutex is locked/unlocked
  mutex.acquire()
  #Add 10 to CAN message 
  CAN_message_1[1] = CAN_message_1[1]+10
  #Unlocks Mutex
  mutex.release()

#Create the 2 threads
th_CANDecode  = Thread(target=CANDecode)
th_CANUpdate  = Thread(target=CANUpdate)

#Starts the Threads
th_CANDecode.start()
th_CANUpdate.start()
