import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host="localhost",
    database="negmatov1",
    user="postgres",
    password="toor"
)

cur = conn.cursor()

    cur.execute("CREATE TABLE s_adm (id_s_adm SERIAL PRIMARY KEY NOT NULL, s_user VARCHAR(255) UNIQUE NOT NULL, s_pass VARCHAR(255) UNIQUE NOT NULL);")
cur.execute("CREATE TABLE u_adm (id_u_adm SERIAL PRIMARY KEY NOT NULL, u_user VARCHAR(255) UNIQUE NOT NULL, u_pass VARCHAR(255) UNIQUE NOT NULL);")
cur.execute("CREATE TABLE r_adm (id_r_adm SERIAL PRIMARY KEY NOT NULL, r_user VARCHAR(255) UNIQUE NOT NULL, r_pass VARCHAR(255) UNIQUE NOT NULL);")
cur.execute("CREATE TABLE district (id_district SERIAL PRIMARY KEY NOT NULL, d_name VARCHAR(255) UNIQUE NOT NULL);")
cur.execute("CREATE TABLE units (id_units SERIAL PRIMARY KEY NOT NULL, u_name VARCHAR(255) UNIQUE NOT NULL);")
cur.execute("CREATE TABLE models (id_models SERIAL PRIMARY KEY NOT NULL, m_name VARCHAR(255) UNIQUE NOT NULL);")
cur.execute("CREATE TABLE devices (id_device SERIAL PRIMARY KEY NOT NULL, disctr INTEGER REFERENCES district(id_district), unit INTEGER REFERENCES units(id_units), d_hostname VARCHAR(255) UNIQUE NOT NULL, d_ip_add VARCHAR(255) UNIQUE NOT NULL, mac_add VARCHAR(255) NOT NULL, ser_numb VARCHAR(255) NOT NULL, model INTEGER REFERENCES models(id_models));")
cur.execute("CREATE TABLE iptable (id_iptable SERIAL PRIMARY KEY NOT NULL, i_disctr INTEGER REFERENCES district(id_district), i_unit INTEGER REFERENCES units(id_units), i_hostname VARCHAR(255) REFERENCES devices(d_hostname), i_ip_add VARCHAR(255) NOT NULL, gave_time TIMESTAMP NOT NULL, status VARCHAR(255) NOT NULL);")

conn.commit()
cur.close()
conn.close()
