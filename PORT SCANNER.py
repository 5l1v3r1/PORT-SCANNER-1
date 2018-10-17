# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 23:24:04 2018

@author: CAPTAIN
"""

import socket
from datetime import datetime
import threading

subprocess.call("clear", shell=True)

hostname=input("HOSTNAME: ")
ip=socket.gethostbyname(hostname)



print('-'*77)
print('SCANNING PORTS')
print('-'*77)

t1=datetime.now()


    
for port in range(1025):
        try:
            
            socks=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socks.settimeout(0.5)
            result=socks.connect((hostname,port))
            print("Port",port,"is OPEN")
            socks.close()
        
        except KeyboardInterrupt:
            print("QUITTING")

        except socket.gaierror:
            print("Hostname couldn't be resolved")
        
        except:
            pass

    
    
t2=datetime.now()
t3=t2-t1

print("Scan completed in",t3)