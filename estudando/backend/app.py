from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/users",methods = ["POST"])

def add_user():
    dados = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users(nome) values(%s)
    """,(dados["nome"],))

    conn.commit()
    return jsonify({"Menssage":"Cadastrado com sucesso"}),201

# Listar usuarios

@app.route("/users",methods = ["GET"])
def pegarUsuario():
    
    # Faça uma ligação com o banco de dados
    conn = get_connection()
    # Criando um tradutor de codigo sql
    cursor = conn.cursor(dictonary=True)
    # Mandando um codigo sql atraves de uma string
    cursor.execute("""
    SELECT * FROM users;
    """)
    # Buscando todos os usuarios do banco de dados e salvando em uma tupla chamada users
    users=cursor.fetchall()
    # Transformando a tupla em um json
    return jsonify(users),200

if __name__=="__main__":
    app.run(debug = True)                                        