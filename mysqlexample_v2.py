# Author: Zaheer Khan
# Date: 20 Jan 2022
# Version: 2.0
# Description: This program demonstrates simple
#              CURD operations on STUDENTSREG DB

import mysql.connector
 
""" Connect to MySQL database """
conn = mysql.connector.connect(host='127.0.0.1',                              
                              user='zaheer',
                              password='SecretPassword',
                              db='STUDENTSREG')
                                
print('MySQL Connection is established')

# Now you should write your DB queries here...    
# 1. Create cursor object
# 2. Use execute() method
# 3. Fetch data if peformed SELECT statement

dbcursor = conn.cursor()    #Creating cursor object

def fetch_record(tablename, recordid, idcolname):
    Tablename = tablename
    Recordid = recordid
    IDColumnName = idcolname 
    SQLstatement = 'SELECT * FROM ' + Tablename + ' WHERE ' + IDColumnName + ' = ' + Recordid + ';'
    dbcursor.execute(SQLstatement)
    print('SELECT statement executed successfully.') 
    rows = dbcursor.fetchall()
    print('Total rows: ', dbcursor.rowcount)
    for row in rows:
        print(row) # will print list of values for all columns                                
        #print(row[0], row[1]) # will print values for all column1 and column 2 only

def add_student_record(id, name, email):
    INSERT_statement = 'INSERT INTO STUDENT (\
    SID, SNAME, EMAIL) VALUES (%s, %s, %s);' 
    dataset = (id,name,email)
    dbcursor.execute(INSERT_statement, dataset)
    conn.commit()              
    print('INSERT query executed successfully.')     

def update_student_email(id, newemail):
    UPDATE_statement = 'UPDATE STUDENT SET \
    EMAIL = %s WHERE SID = %s;'
    dataset = (newemail, id)
    dbcursor.execute(UPDATE_statement, dataset)
    conn.commit()              
    print('UPDATE statement executed successfully.') 

def delete_student_record(id):
    DELETE_statement = 'DELETE FROM STUDENT \
    WHERE SID = %s;'    
    dataset = (id,)        
    dbcursor.execute(DELETE_statement, dataset)   
    conn.commit()              
    print('DELETE statement executed successfully.')

print ("**********************************\n")
print ("**********************************\n")
print(" Select one of the following options: \n")
print(" For retrieving student record press 1\n")
print(" For retrieving tutor record press 2\n")
print(" For retrieving module info press 3\n")
print(" For retrieving list of all students press 4\n")
print(" For adding a new student 5\n")
print(" For updating an existing student's email press 6\n")
print(" For deleting a student record 7\n")



print ("**********************************\n")
choice = int(input())

if choice == 1:
    print('You selected Option : ' + str(choice) + ' \n')
    print('Enter Student ID: ')
    id = input()
    fetch_record('STUDENT', id, 'SID')    
elif choice == 2:
    print('You selected Option : ' + str(choice) + ' \n')
    print('Enter Tutor ID: ')
    id = input()
    fetch_record('TUTOR', id, 'Tut_Id')        
elif choice == 3:
    print('You selected Option : ' + str(choice) + ' \n')
    print('Enter Module ID: ')
    id = input()
    fetch_record('MODULES', id, 'MID')    
elif choice == 4:
    print('You selected Option : ' + str(choice) + ' \n')
    print('List of all Students\n')
    SQLstatement = 'SELECT * FROM STUDENT;'
    dbcursor.execute(SQLstatement)
    print('SELECT statement executed successfully.') 
    rows = dbcursor.fetchall()
    print('Total rows: ', dbcursor.rowcount)
    for row in rows:
        #print(row) # will print list of values for all columns                                
        print(row[0], row[1], row[2]) # will print values for all column1 and column 2 only
        #print(str(int(row[0]) * 2), row[1], row[2]) # will print values for all column1 and column 2 only
elif choice == 5:
    print('You selected Option : ' + str(choice) + ' \n')
    print('Enter new student ID: ')
    id = input()
    print('Enter student name: ')
    name = input()
    print('Enter student email: ')
    email = input()
    add_student_record(id, name, email)
elif choice == 6:
    
    print('You selected Option : ' + str(choice) + ' \n')
    print('Enter student ID to update email address: ')
    id = input()
    print('Enter new email address: ')
    newemail = input()
    update_student_email(id, newemail)

elif choice == 7:
    print('You selected Option : ' + str(choice) + ' \n')
    print('Enter student ID to delete student recrod: ')
    id = input()
    delete_student_record(id)

    
else:
    print('Error: Incorrect choice selected! Start again')
    exit()

dbcursor.close()              
conn.close() #Connection must be closed





