from flask import Flask, jsonify, make_response
import psycopg2
import os

app = Flask(__name__)

def ler_todas_operadoras():
    try:
        conn = psycopg2.connect(database="operadoras_ativas",
                                host="localhost",
                                user="postgres",
                                password="12345678",
                                port="5432",
                                client_encoding='UTF8')  
        cur = conn.cursor()
        cur.execute("SELECT * FROM DADOS_OPERADORAS_ATIVAS")
        resultados = cur.fetchall()
        colunas = [desc[0] for desc in cur.description]  
        operadoras = [dict(zip(colunas, row)) for row in resultados]  
        cur.close()
        conn.close()
        return operadoras
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return []

def buscar_operadoras(termo_busca):
    try:
        conn = psycopg2.connect(database="operadoras_ativas",
                                host="localhost",
                                user="postgres",
                                password="12345678",
                                port="5432",
                                client_encoding='UTF8')  
        cur = conn.cursor()
        cur.execute("SELECT * FROM DADOS_OPERADORAS_ATIVAS WHERE Razao_Social ILIKE %s", (f'%{termo_busca}%',))
        resultados = cur.fetchall()
        colunas = [desc[0] for desc in cur.description]
        operadoras = [dict(zip(colunas, row)) for row in resultados]
        cur.close()
        conn.close()
        return operadoras
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return []

@app.route('/', methods=['GET'])
@app.route('/operadoras', methods=['GET'])
def listar_operadoras():
    operadoras = ler_todas_operadoras()
    for operadora in operadoras:
        for chave, valor in operadora.items():
            if valor is None:
                operadora[chave] = "Dado não disponível"
            elif isinstance(valor, str):
                operadora[chave] = valor.encode('utf-8').decode('utf-8', 'ignore') 
    response = make_response(jsonify(operadoras))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/operadoras/<termo>', methods=['GET'])
def buscar(termo):
    if not termo:
        return jsonify({'erro': 'Termo de busca não fornecido'}), 400
    resultados = buscar_operadoras(termo)
    for resultado in resultados:
        for chave, valor in resultado.items():
            if valor is None:
                resultado[chave] = "Dado não disponível"
            elif isinstance(valor, str):
                resultado[chave] = valor.encode('utf-8').decode('utf-8', 'ignore')  
    response = make_response(jsonify(resultados))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5009)
