import paramiko
import ssh_modul
import time


class show:
    def sh_ver():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"terminal length 0\n")
        ssh_session.send(f"show system-info\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_run():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"terminal length 0\n")
        ssh_session.send(f"show run\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_vlan():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"terminal length 0\n")
        ssh_session.send(f"show vlan\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_mac_vl():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"terminal length 0\n")
        ssh_session.send(f"show mac address-table vlan {vl_id}\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_mac_interf():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"terminal length 0\n")
        ssh_session.send(f"show mac address-table int gig 1/0/{inter_id}\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_log():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"terminal length 0\n")
        ssh_session.send(f"show logging flash\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def sh_interf_stat():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"terminal length 0\n")
        ssh_session.send(f"show int status\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output


class config:
    def c_vl():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password
        vl_id = str(input("VLAN ID: "))
        vl_name = str(input("VLAN name:"))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        #jarayon
        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"configure\n")
        ssh_session.send(f"vlan {vl_id}\n")
        ssh_session.send(f"name {vl_name}\n")
        ssh_session.send(f"end\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def d_vl():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password
        vl_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)


        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"configure\n")
        ssh_session.send(f"no vlan {vl_id}\n")
        ssh_session.send(f"end\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_int_acc():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password
        inter_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"configure\n")
        ssh_session.send(f"int gig 1/0/{inter_id}\n")
        ssh_session.send(f"switchport general allowed vlan 1 untagged\n")
        ssh_session.send(f"end\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_int_trk():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password
        inter_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"configure\n")
        ssh_session.send(f"int eth 1/0/{inter_id}\n")
        ssh_session.send(f"switchport general allowed vlan 1 tagged\n")
        ssh_session.send(f"end\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_int_ac_vl():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password
        inter_id = str(input("VLAN ID: "))
        vl_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"configure\n")
        ssh_session.send(f"int eth 1/0/{inter_id}\n")
        ssh_session.send(f"switchport general allowed vlan {vl_id} untagged\n")
        ssh_session.send(f"switchport pvid {vl_id}\n")
        ssh_session.send(f"end\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_int_trk_vl():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password
        inter_id = str(input("VLAN ID: "))
        vl_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"configure\n")
        ssh_session.send(f"int eth 1/0/{inter_id}\n")
        ssh_session.send(f"switchport general allowed vlan {vl_id} tagged\n")
        ssh_session.send(f"end\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_d_int_trk_vl():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password
        inter_id = str(input("VLAN ID: "))
        vl_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"configure\n")
        ssh_session.send(f"int eth 1/0/{inter_id}\n")
        ssh_session.send(f"no switchport general allowed vlan {vl_id}\n")
        ssh_session.send(f"end\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output

    def w_d_int_ac_vl():
        device_ip = ssh_modul.device_ip
        username = ssh_modul.username
        password = ssh_modul.password
        inter_id = str(input("VLAN ID: "))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=device_ip, username=username, password=password)

        ssh_session = ssh_client.invoke_shell()
        ssh_session.send(f"enable\n")
        ssh_session.send(f"configure\n")
        ssh_session.send(f"int eth 1/0/{inter_id}\n")
        ssh_session.send(f"no switchport general allowed vlan {vl_id}\n")
        ssh_session.send(f"no switchport pvid {vl_id}\n")
        ssh_session.send(f"no description\n")
        ssh_session.send(f"end\n")
        time.sleep(1)
        output = ssh_session.recv(65535).decode()
        print(output)
        return output