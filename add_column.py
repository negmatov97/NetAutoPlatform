import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="negmatov1",
    user="postgres",
    password="toor"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Add the column to each table
#tables = ["s_adm", "u_adm", "r_adm"]
#for table in tables:
#    cur.execute(f"ALTER TABLE {table} ADD COLUMN function VARCHAR(255) UNIQUE NOT NULL")

# insert data into the s_adm table
#cur.execute("""
#    INSERT INTO s_adm (id_u_adm, s_user, s_pass, function)
#    VALUES (1, 'negmatov', 'negmatov', 'c_vl(), d_vl(), int_acc_vl_sht_des(), int_trk_vl_sht_des(),
#            int_vlan_ip_sht_des(), hostname(), user_pass(), ntp(), snmpv2_snmpv3(), show_int_stat(),
#            show_run(), show_mac(), show_mac_int(), show_mac_vl(), logging()')
#""")

#cur.execute("""
#    INSERT INTO u_adm (id_u_adm, u_user, u_pass, function)
#    VALUES (1, 'komilov', 'komilov', 'show_int_stat(), show_mac(), show_mac_int(), show_mac_vl(), show_run(), show_vers(), show_logging(), show_vl()')
#""")
#cur.execute(""" INSERT INTO district (id_district, d_name)
#    VALUES (1, 'MA') """)

#cur.execute("""
#    INSERT INTO units (id_units, u_name)
#    VALUES (1, '000/hq')
            
#""")

cur.execute("""
    INSERT INTO devices (id_device, disctr, unit, d_hostname, d_ip_add, mac_add, ser_numb, model)
    VALUES (1, 1, 1, 'sw1', '192.168.202.208', '00;11;22;33;44;55;', '123456789', '1')
""")
# commit the changes to the database
conn.commit()

# close the cursor and connection
cur.close()
conn.close()