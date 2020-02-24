from fabric import Connection
from paramiko import SSHException, AuthenticationException, BadAuthenticationType
import socket


commands =['esxcli system snmp set -r #clear v2 community',
           'esxcli system snmp set -a SHA1 -x AES128',
           'esxcli system snmp set --users helixadmin/ae6faa849f2b369a07edff86892a0e7be8d29e56/c9a9d168a5213a7521a140237ced481497c5864e/priv',
           'esxcli system snmp set --enable true',
           'esxcli system snmp get'
           ]
   
#perform the functions on the remote devices
def snmp_function(hostname,password):
    con = Connection(host='root@'+hostname, connect_kwargs={'password':password}) #Construct connection
    
    if process_input(con):
        print ("No change needed for server "+ hostname)
        write_log(hostname + " was not changed")
        return
    else:
        write_data(con,hostname)
    
#Apply commands 
def write_data(c,host):
    for command in commands:
        c.run(command, hide=True)
        print("Updated " + host)
        write_log(host + " was changed")


#Determine if server should be processed
def process_input(c):
    try:
        snmp_data = c.run(commands[4], hide=True).stdout    #read SNMP data from server, store into a (long)string
        snmp_data_list = [line.strip() for line in snmp_data.splitlines()] #work the string into a list
        if snmp_data_list[0] == 'Authentication: SHA1' and snmp_data_list[1] == 'Communities:':
            return True
        else:
            return False
        
    except AuthenticationException: 
        print ("Bad authentication credentials provided.")
    except BadAuthenticationType: 
        print ("Authentication type not allowed.")
    except socket.gaierror:
        print ("DNS resolution failed for " + str(c.host)) 
        
   
   

def main():
    host_list_placeholder = open(r"C:\Users\preed\Documents\Code Junk\FILES\VM_SERVER_LIST.txt",'r')
    target_host_passwd = input ("Enter the password: ")
    
    if (host_list_placeholder[0] != '' or host_list_placeholdeer):
        host_list = [line.rstrip() for line in host_list_placeholder]
    for host in host_list:
        print ("Working on host: " + host)
        snmp_function(host, target_host_passwd)
        
def write_log(string):
    f = open(r"C:\Users\preed\Documents\Code Junk\FILES\SNMP_LOG.txt",'a+')
    f.write('\n' + string)
    f.close

#this function is a way to cleanly open files with no errors, and create missing files only when flag is set
def open_file(path_string, create_flag):
    try:
        print()
    except AuthenticationException:
        print()


main()
print ("Done!")
exit()


