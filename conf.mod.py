# Import the required libraries
import paramiko
import ssh_modul
import time

# Load the credentials from the ssh_model module
device_ip = ssh_modul.device_ip
username = ssh_modul.username
password = ssh_modul.password

# Create an SSH client and connect to the switch
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=device_ip, username=username, password=password)

ssh_session = ssh_client.invoke_shell()
ssh_session.send("enable\n")
time.sleep(1)
output = ssh_session.recv(65535).decode()
print(output)

# Create VLAN 675
ssh_session.send("terminal length 0 \n")
time.sleep(1)
output = ssh_session.recv(65535).decode()
print(output)

ssh_session.send("show run\n")
time.sleep(1)
output = ssh_session.recv(65535).decode()
print(output)

ssh_session.send("exit\n")
time.sleep(1)
output = ssh_session.recv(65535).decode()
print(output)

# Close the SSH connection
ssh_client.close()