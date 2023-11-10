import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="sampledb", user='admin', password='admin', host='172.30.189.203', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("SELECT * FROM users;")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print(data)

#Closing the connection
conn.close()
