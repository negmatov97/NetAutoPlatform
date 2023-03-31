import psycopg2
import paramiko

# Connect to the NAP database
conn = psycopg2.connect(
    host="localhost",
    database="negmatov1",
    user="postgres",
    password="toor"
)

# Get the device IP address and user credentials from user input
device_ip = input("Qurilmaning IP mazilini kiriting: ")
username = input("Username kiriting: ")
password = input("Password kiriting: ")

# Query the device table to check if the IP address exists
cursor = conn.cursor()
cursor.execute("SELECT d_ip_add FROM devices WHERE d_ip_add=%s", (device_ip,))
result = cursor.fetchone()

if result is None:
    print("Kechirasiz kiritilgan IP manzil ma'lumotlar bazasida mavjud emas.")
else:
    # Query the s_adm table to check if the username and password match
    cursor.execute("SELECT s_user, s_pass FROM s_adm WHERE s_user=%s AND s_pass=%s", (username, password))
    s_result = cursor.fetchone()

    # Query the u_adm table to check if the username and password match
    cursor.execute("SELECT u_user, u_pass FROM u_adm WHERE u_user=%s AND u_pass=%s", (username, password))
    u_result = cursor.fetchone()

    # Query the r_adm table to check if the username and password match
    cursor.execute("SELECT r_user, r_pass FROM r_adm WHERE r_user=%s AND r_pass=%s", (username, password))
    r_result = cursor.fetchone()

    if s_result is None and u_result is None and r_result is None:
        print("Noto'g'ri username yoki password")
    else:
        # Connect to the device using SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device_ip, username=username, password=password)

        # Do something with the SSH connection here

        # Close the SSH connection
        ssh.close()

# Close the database connection
cursor.close()
conn.close()