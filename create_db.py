import mysql.connector

def create_db():
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Root"
    )
    
    cur = con.cursor()
    
    # Create the 'ims' database
    cur.execute("CREATE DATABASE IF NOT EXISTS ims")
    
    # Switch to the 'ims' database
    cur.execute("USE ims")

    # Create the 'employee' table
    cur.execute("CREATE TABLE IF NOT EXISTS employee (eid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), gender VARCHAR(10), contact VARCHAR(15), dob DATE, doj DATE, password VARCHAR(255), usertype VARCHAR(20), address TEXT, salary DECIMAL(10, 2))")

    # Create Distributor Table
    cur.execute("CREATE TABLE IF NOT EXISTS distributor (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), contact VARCHAR(15), description TEXT)")

    #Create Category Table
    cur.execute("CREATE TABLE IF NOT EXISTS category (cid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    
    # Create Product Table
    cur.execute("CREATE TABLE IF NOT EXISTS product (pid INT AUTO_INCREMENT PRIMARY KEY, distributor VARCHAR(255),category VARCHAR(255), name VARCHAR(255), price DECIMAL(10, 2), qty TEXT,status TEXT )")

    con.commit()
    con.close()

create_db()
