import mysql.connector

comercializadora=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce_vargas_benavides"
)

cursor=comercializadora.cursor()
cursor.execute('SHOW DATABASE')

for dbs in cursor:
    print(dbs)
    
print('-----------------')
cursor.execute("SHOW DATABASE")
for n in cursor:
    print(n)
    
cursor.execute(""" INSERT INT users(id,role_id,seller_id,name,email,password) VALUES(5,22,7,'Juanito Alimaña',juanitoali22@gmsil.com','12345')""")
comercializadora.commit()
cursor.execute('select * from users')
for ap in cursor:
    print(ap[0])
    print(ap[1])
    print(ap[2])
    print(ap[3])