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

if __name__=="__main__":
    app.run(debug = True)                                        