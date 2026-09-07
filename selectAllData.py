import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=13306,
    user="root",
    password="pass",
    database="sampledb"
)

cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

if rows:
    for row in rows:
        print(f"ID : {row['id']}")
        print(f"Name : {row['name']}")
        print(f"Email : {row['email']}")
        print(f"Time : {row['created_at']}")
        print(f"-----------------------------")
else:
    print("find no data")

cursor.close()
conn.close()
