import csv
import sqlite3

conn = sqlite3.connect("aetherAI.db")
cursor = conn.cursor()

# Query for creating the sys_command table
#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

# Query for inserting data into the sys_command table
#query1 = "INSERT INTO sys_command VALUES(null, 'android studio', 'C:/Program Files/Android/Android Studio/bin/studio64.exe')"
#cursor.execute(query1)
#quer2 = "INSERT INTO sys_command VALUES(null, 'ms word', 'C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE')"
#cursor.execute(quer2)
#query3 = "INSERT INTO sys_command VALUES(null, 'ms excel', 'C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE')"
#cursor.execute(query3)

# Query for creating the web_command table
#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

# Query for inserting data into the web_command table
#query = "INSERT INTO web_command VALUES(null, 'canva', 'https://www.canva.com/')"
#cursor.execute(query)
#query1 = "INSERT INTO web_command VALUES(null, 'youtube', 'https://www.youtube.com/')"
#cursor.execute(query1)
#query2 = "INSERT INTO web_command VALUES(null, 'google classroom', 'https://classroom.google.com/')"
#cursor.execute(query2)
#query3 = "INSERT INTO web_command VALUES(null, 'student portal', 'https://charusat.edu.in:912/eGovernance/StudentLogin.aspx')"
#cursor.execute(query3)
query4 = "INSERT INTO web_command VALUES(null, 'LeetCode', 'https://leetcode.com/u/22dit061/')"
cursor.execute(query4)
conn.commit()
conn.close()

# Close the database connection
#conn.close()

# Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
#    id INTEGER PRIMARY KEY,
#    name VARCHAR(200),
#    mobile_no VARCHAR(255),
#    email VARCHAR(255) NULL
#)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 18th columns (First Name and Phone 1 - Value)
#desired_columns_indices = [0, 18]

# Read data from CSV and insert into SQLite table for the desired columns
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#    csvreader = csv.reader(csvfile)
#    next(csvreader)  # Skip the header row
#    for row in csvreader:
#        if len(row) > max(desired_columns_indices):  # Ensure indices are within range
#            selected_data = [row[i] for i in desired_columns_indices]
#            cursor.execute('''INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?);''', tuple(selected_data))
#        else:
#            print(f"Skipping row with insufficient columns: {row}")

#For inserting single data into the contacts table
#query = "INSERT INTO contacts VALUES (null,'Varshil', '6351810074',NULL)"
#cursor.execute(query)
#conn.commit()