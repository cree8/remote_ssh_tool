# remote_ssh_tool
Apply commands to remote SSH servers
This is my first Python script written to actually accomplish something other than printing text to stdout. 
Hopefully this is the beginning of a long and interesting career in DevOps.

The program uses Fabric, which is a high level Python application which implements a couple other 
Python apps at a mid and lower level to accomplish the task of performing tasks remotly via SSH.

I am certain it is quite janky and junky. Heres to the future growth of my coding skills!

The application started off as a method for changing a large number of VMWare SNMP configurations in an 
automated fashion. Some functions contained within have the "snmp" moniker, althogh they actually have 
nothing to do with the actual SNMP protocol. This will be changed in a future update. 

Eventually the application will be structured in a manner which allows it to send any arbitrary commands to a group
of remote servers based on comparison to input parameters. 
