x=0
while x<10:
    print(x)
    if x==5:
        print("start breaking")
        break 
    x+=1
print("done")  
print(" ")

import os
print(os.getcwd())
files=os.listdir("/home/mutambo/Downloads") 
print(files)  
print("")  

#Simple Seven layer protocol simulation
import numpy as np
class message_prot:
    #set the header,meassage parameters
    def __init__(self,message,header7,header6):
        self.message="I am a winer"
        self.header7="http"
        self.header6="set the session"
    def layer_sev(self): 
        print(self.header7+" this is the message "+self.message)
    def layer_six(self):
        print(self.header6 + self.header7+" this is the message "+self.message)
p1=message_prot("Http GET","I am Peter Mutambo","set another session")
p1.layer_sev ()
p1.layer_six()
print("")

print("Continue man")  
    
        
          
        
      
                                                                                                                                                                                                                                            