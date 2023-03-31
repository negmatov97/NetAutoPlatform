import paramiko
import connecting.ssh_modul
import time


class show:
    def sh_ver():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"terminal length 0\r")
        ssh_session.send(f"show version\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_run():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"terminal length 0\r")
        ssh_session.send(f"show run\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_vlan():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"terminal length 0\r")
        ssh_session.send(f"show vlan\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_mac_vl():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"terminal length 0\r")
        ssh_session.send(f"show mac-address-table vlan {vl_id}\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_mac_interf():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"terminal length 0\r")
        ssh_session.send(f"show mac-address-table int eth 1/0/{inter_id}\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_log():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"terminal length 0\r")
        ssh_session.send(f"show logging flash\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_interf_stat():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"terminal length 0\r")
        ssh_session.send(f"show int eth status\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output


class config:
    def c_vl():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password
        vl_id = str(input("VLAN ID: "))
        vl_name = str(input("VLAN name:"))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        #jarayon
        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"config terminal\r")
        ssh_session.send(f"vlan {vl_id}\r")
        ssh_session.send(f"name {vl_name}\r")
        ssh_session.send(f"end\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def d_vl():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password
        vl_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)


        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"config terminal\r")
        ssh_session.send(f"no vlan {vl_id}\r")
        ssh_session.send(f"end\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_int_acc():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password
        inter_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"config terminal\r")
        ssh_session.send(f"int eth 1/0/{inter_id}\r")
        ssh_session.send(f"switchport mode access\r")
        ssh_session.send(f"end\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_int_trk():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password
        inter_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"config terminal\r")
        ssh_session.send(f"int eth 1/0/{inter_id}\r")
        ssh_session.send(f"switchport mode trunk\r")
        ssh_session.send(f"end\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_int_ac_vl():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password
        inter_id = str(input("VLAN ID: "))
        vl_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"config terminal\r")
        ssh_session.send(f"int eth 1/0/{inter_id}\r")
        ssh_session.send(f"switchport access vlan {vl_id}\r")
        ssh_session.send(f"end\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_int_trk_vl():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password
        inter_id = str(input("VLAN ID: "))
        vl_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"config terminal\r")
        ssh_session.send(f"int eth 1/0/{inter_id}\r")
        ssh_session.send(f"switchport trunk allowed vlan add {vl_id}\r")
        ssh_session.send(f"end\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_d_int_trk_vl():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password
        inter_id = str(input("VLAN ID: "))
        vl_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"config terminal\r")
        ssh_session.send(f"int eth 1/0/{inter_id}\r")
        ssh_session.send(f"switchport trunk allowed vlan remove {vl_id}\r")
        ssh_session.send(f"end\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_d_int_ac_vl():
        device_ip = connecting.ssh_modul.device_ip
        username = connecting.ssh_modul.username
        password = connecting.ssh_modul.password
        inter_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\r")
        ssh_session.send(f"config terminal\r")
        ssh_session.send(f"int eth 1/0/{inter_id}\r")
        ssh_session.send(f"switchport access vlan 1\r")
        ssh_session.send(f"no description\r")
        ssh_session.send(f"end\r")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output
        return output