# Import the required libraries
import paramiko
import ssh_modul
import time

# Load the credentials from the ssh_model module
device_ip = ssh_modul.device_ip
username = ssh_modul.username
password = ssh_modul.password
vl_id = str(input("Enter Vlan ID: "))
vl_name = str(input("Vlan Nomini kirit: "))
#v = "vlan"

# Create an SSH client and connect to the switch
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=device_ip, username=username, password=password)

# Command for explotation

#vlan_id = ''.join(vl_id)

#vlan1 = [
#    v + list(vlan_id)
#]


# for network devices

#for command in vlan1:
ssh_session = ssh_client.invoke_shell()
ssh_session.send(f"enable\n")
ssh_session.send(f"config terminal\n")
ssh_session.send(f"vlan {vl_id}\n")
ssh_session.send(f"name {vl_name}\n")
ssh_session.send(f"end\n")
ssh_session.send(f"exit\n")
time.sleep(1)
output = ssh_session.recv(65535).decode()
print(output)

# Close the SSH connection
ssh_client.close()