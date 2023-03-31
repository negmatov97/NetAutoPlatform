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

# Command for explotation

commands = [
    "terminal length 0",
    "show ver"
]

# for network devices

for command in commands:
    ssh_session = ssh_client.invoke_shell()
    ssh_session.send("enable\n")
    time.sleep(1)
    output = ssh_session.recv(65535).decode()
    print(output)

    ssh_session.send(command + "\n")

    # Wait for the command to finish executing
    time.sleep(1)

    # Read the output from the command
    output = ssh_session.recv(65535).decode()

    # Print the output
    print(output)

# Close the SSH connection
ssh_client.close()