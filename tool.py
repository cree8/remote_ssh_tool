from fabric import Connection

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
    

def write_data(c,host):
    for command in commands:
        c.run(command, hide=True)
        print("Updated " + host)
        write_log(host + " was changed")



def process_input(c):
    snmp_data = c.run(commands[4], hide=True).stdout    #read SNMP data from server, store into a (long)string
    snmp_data_list = [line.strip() for line in snmp_data.splitlines()] #work the string into a list
    
    if snmp_data_list[0] == 'Authentication: SHA1' and snmp_data_list[1] == 'Communities:':
        return True
    else:
        return False
   

def main():
    target_host_passwd = input ("Enter the password: ")
    #For each host in the list, run the function
    host_list = [line.rstrip() for line in open(r"C:\Users\preed\Documents\Code Junk\VM_SERVER_LIST.txt",'r')]
    for host in host_list:
        print ("Working on host: " + host)
        snmp_function(host, target_host_passwd)
        
def write_log(string):
    f = open(r"C:\Users\preed\Documents\Code Junk\SNMP_LOG.txt",'a+')
    f.write('\n' + string)
    f.close

main()
print ("Done!")



