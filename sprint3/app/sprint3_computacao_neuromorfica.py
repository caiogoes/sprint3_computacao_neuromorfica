from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import sqlite3
import pandas as pd

app = Flask(__name__)

# Use o run_with_ngrok para criar um túnel ngrok temporário
run_with_ngrok(app)

@app.route('/')
def hello_world():
    return jsonify({"message": "Sprint 3 - Computacao neuromorfica"})

# Função para criar um dado na tabela
@app.route('/configure', methods=['POST'])
def criar_dado():
    try:
        Confederation = request.json['Confederation']
        Stadium = request.json['Stadium']
        City = request.json['City']
        HomeTeams = request.json['HomeTeams']
        Capacity = request.json['Capacity']
        Country = request.json['Country']
        IOC = request.json['IOC']

        conn = sqlite3.connect('stadiums.db')
        conn.execute('INSERT INTO stadiums VALUES (?, ?, ?, ?, ?, ?, ?)', (Confederation, Stadium, City, HomeTeams, Capacity, Country, IOC))
        conn.commit()
        conn.close()

        return jsonify({"mensagem": "Dado criado com sucesso!"}), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 400

# Função para retornar os dados da tabela
@app.route('/read', methods=['GET'])
def obter_dados():
    try:
        conn = sqlite3.connect('stadiums.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stadiums")
        resultados = cursor.fetchall()
        conn.close()

        dados = []
        for linha in resultados:
            dados.append({"Confederation": linha[0], "Stadium": linha[1], "City": linha[2], "HomeTeams": linha[3], "Capacity": linha[4], "Country": linha[5], "IOC": linha[6]})

        return jsonify(dados), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run()