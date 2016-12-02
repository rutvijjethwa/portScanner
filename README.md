# portScanner
Script to Check the status(Closed/Open) of a port

Welcome to the portScanner wiki!

This is a simple port scanner to check whether a port is open or not.

You can either check for a specific port or for a range of ports, syntax for which is as follows:
#############################################################################
To Check for a Single port
SYNTAX:

  python portScanner.py <ip_address> <port_number>
  
EXAMPLE:
  
  python portScanner.py 8.8.8.8 53  

- Above command will let you know whether port no 53 is open or not.
#############################################################################

To check for a range of port
SYNTAX:

  python portScanner.py <ip_address> <port_range_start> <port_range_end>

  python portScanner.py 8.8.8.8 53 60

- Above command will check which ports are open or closed from port number 53 to 60.
