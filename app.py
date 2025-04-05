from flask import Flask, jsonify, make_response
import psycopg2
from dotenv import load_dotenv
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


load_dotenv()

DATABASE_URL = "postgresql://postgres:xDWLNwAgtyRXWWImgrRPCysPVUsdCiPn@gondola.proxy.rlwy.net:26336/railway"
def conectar_db():
    
    try:
        
        return psycopg2.connect(DATABASE_URL, sslmode="require")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def ler_todas_operadoras():
    try:
        conn = conectar_db()
        if conn is None:
            return [] 

        cur = conn.cursor()
        cur.execute("SELECT * FROM DADOS_OPERADORAS_ATIVAS")
        resultados = cur.fetchall()
        colunas = [desc[0] for desc in cur.description]
        operadoras = [dict(zip(colunas, row)) for row in resultados]
        cur.close()
        conn.close()
        return operadoras
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao ler operadoras: {error}")
        return []

def buscar_operadoras(termo_busca):
    
    try:
        conn = conectar_db()
        if conn is None:
            return [] 

        cur = conn.cursor()
        cur.execute("SELECT * FROM DADOS_OPERADORAS_ATIVAS WHERE Razao_Social ILIKE %s", (f'%{termo_busca}%',))
        resultados = cur.fetchall()
        colunas = [desc[0] for desc in cur.description]
        operadoras = [dict(zip(colunas, row)) for row in resultados]
        cur.close()
        conn.close()
        return operadoras
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao buscar operadoras: {error}")
        return []

@app.route('/', methods=['GET'])
@app.route('/operadoras', methods=['GET'])
@cross_origin(origins="https://vue-interface-gamma.vercel.app",
              "https://vue-interface-5nuv06mcs-loresleis-projects.vercel.app"
)
, methods=['GET'], headers=['Content-Type', 'Authorization'])
def listar_operadoras():
    operadoras = ler_todas_operadoras()
    for operadora in operadoras:
        for chave, valor in operadora.items():
            if valor is None:
                operadora[chave] = "Dado não disponível"
    response = make_response(jsonify(operadoras))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/operadoras/<termo>', methods=['GET'])
@cross_origin(origins="https://vue-interface-gamma.vercel.app",
              "https://vue-interface-5nuv06mcs-loresleis-projects.vercel.app", methods=['GET'], headers=['Content-Type', 'Authorization'])
def buscar(termo):
    if not termo:
        return jsonify({'erro': 'Termo de busca não fornecido'}), 400
    resultados = buscar_operadoras(termo)
    for resultado in resultados:
        for chave, valor in resultado.items():
            if valor is None:
                resultado[chave] = "Dado não disponível"
    response = make_response(jsonify(resultados))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))  
    app.run(debug=True, host="0.0.0.0", port=port)
