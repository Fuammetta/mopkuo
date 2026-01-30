import mysql.connector
 
""" Connect to MySQL database """
conn = mysql.connector.connect(host='127.0.0.1',                              
                              user='zaheer',
                              password='SecretPassword')
                                
print('MySQL Connection is established')
# Now you should write your DB queries here...    
# 1. Create cursor object
# 2. Use execute() method
# 3. Fetch data if peformed SELECT statement
                
conn.close() #Connection must be closed



