from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',  # Replace with your MySQL host
        database='tablename',  # Replace with your database name
        user='root',  # Replace with your MySQL username
        password=''  # Replace with your MySQL password
    )
    
    if connection.is_connected():
        print('Connected to the database')
        
except Error as e:
    print('Error connecting to the database:', e)


app = FastAPI()

@app.get('/api/data/get')
def get_data():
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM log')
        rows = cursor.fetchall()
        
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'email': row[2]
            })
        
        return data
    
    except Error as e:
        print('Error executing the query:', e)

@app.post('/api/data/post/{id}/{name}/{email}')
def post(id: int, name: str, email: str):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO log (id, name, email) VALUES (%s, %s, %s)"
        values = (id, name, email)
        cursor.execute(query, values)
        connection.commit()

        return {'message': 'Data inserted successfully'}
    
    except Error as e:
        print('Error executing the query:', e)
