import psycopg2  # for connecting to PostgreSQL database
import paramiko  # for SSH connection

# establish connection to the NAP database
conn = psycopg2.connect(
    host="localhost",
    database="negmatov1",
    user="postgres",
    password="toor"
)

cur = conn.cursor()

# get IP address of the device
cur.execute("SELECT d_ip_add FROM devices WHERE id_device = 'myswitch'")
ip_address = cur.fetchone()[0]

# check s_adm table for matching credentials
cur.execute("SELECT s_user, s_pass FROM s_adm WHERE id_s_adm = 1")
s_row = cur.fetchone()
if s_row and s_row[0] == "myswitch" and s_row[1] == "mypassword":
    ssh_user = s_row[0]
    ssh_pass = s_row[1]
else:
    ssh_user = None
    ssh_pass = None

# check u_adm table for matching credentials
cur.execute("SELECT u_user, u_pass FROM u_adm WHERE id_u_adm = 1")
u_row = cur.fetchone()
if u_row and u_row[0] == "myswitch" and u_row[1] == "mypassword":
    ssh_user = u_row[0]
    ssh_pass = u_row[1]
else:
    ssh_user = None
    ssh_pass = None

# check r_adm table for matching credentials
cur.execute("SELECT r_user, r_pass FROM r_adm WHERE id_r_adm = 1")
r_row = cur.fetchone()
if r_row and r_row[0] == "myswitch" and r_row[1] == "mypassword":
    ssh_user = r_row[0]
    ssh_pass = r_row[1]
else:
    ssh_user = None
    ssh_pass = None

# close database connection
cur.close()
conn.close()

# establish SSH connection if credentials match
if ssh_user and ssh_pass:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_address, username=ssh_user, password=ssh_pass)
    print("SSH connection successful!")
else:
    print("Could not establish SSH connection.")
