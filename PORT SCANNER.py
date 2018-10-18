
import socket
from datetime import datetime
import threading


hostname=input("HOSTNAME: ")
ip=socket.gethostbyname(hostname)


t1=datetime.now()


def scan(hostname,i):
        try:
            socks=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socks.settimeout(0.5)
            result=socks.connect((hostname,port))
            print("Port",i,"is OPEN")
            socks.close()
        
        except KeyboardInterrupt:
            print("QUITTING")

        except socket.gaierror:
            print("Hostname couldn't be resolved")
        
        except:
            pass

for i in range (10000): 
    t1=threading.Thread(target=scan,kwargs={'hostname':i})
    i=i+1
    t1.start
   
print("DONE")
