from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route('/users',methods=['POST'])
def create_user():
    data = request.jsonify
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users(name,email,age)VALUES(%s,%s,%s)""",(data['name'], data['email'],data['age']))
    conn.commit()
    return jsonify({"menssage":"User created successfully"}),201