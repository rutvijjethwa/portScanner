import socket
import sys
def rangeScanner(targetIP,portStart,portEnd):
    """ SCAN FOR A RANGE OF PORT
###################################################################################
   To check for a range of port SYNTAX:

python portScanner.py

python portScanner.py 8.8.8.8 53 60

Above command will check which ports are open or closed from port number 53 to 60.
####################################################################################    
    """
    portEnd+=1
    try:
        for port in range(portStart, portEnd):
            mySoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            targetPcScanResult = mySoc.connect_ex((targetIP, port))
            if targetPcScanResult == 0:
                print("Port {0}: Open".format(port))
            mySoc.close()
    except socket.error:
         print("Please Validate the input")
    #finally:
        # print("Connectivity Issue or the target isn't available")
###########################################################################
def singlePortScanner(targetIP,port):
    """ SCAN FOR A SINGLE PORT  ONLY
     #############################################################################
To Check for a Single port
SYNTAX:

  python portScanner.py <ip_address> <port_number>
  
EXAMPLE:
  
  python portScanner.py 8.8.8.8 53  

- Above command will let you know whether port no 53 is open or not.
#############################################################################
    """
    try:
            mySoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            targetPcScanResult = mySoc.connect_ex((targetIP,port))
            if targetPcScanResult == 0:
                print("Port {0}: Open".format(port))
            else:
                print("Port {0}: Close".format(port))
            mySoc.close()
    except socket.error:
        print("Please Validate the input")
   # finally:
    #    print("Connectivity Issue or the target isn't available")
############################################################################

if __name__=='__main__':
    targetPc = sys.argv[1]
    try:
        targetPcName = socket.gethostbyaddr(targetPc)[0]
        print("Target Hostname : {}".format(targetPcName))
        if len(sys.argv) == 3:
            singlePortScanner(targetPc,int(sys.argv[2]))
        elif len(sys.argv) == 4:
            rangeScanner(targetPc,int(sys.argv[2]),int(sys.argv[3]))
    except socket.herror:
        print("Connectivity Issue or the target isn't available")
