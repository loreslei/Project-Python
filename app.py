from flask import Flask, jsonify, make_response
import psycopg2
import os

app = Flask(__name__)

# URL de conexão fornecida
DATABASE_URL = "postgresql://postgres:xDWLNwAgtyRXWWImgrRPCysPVUsdCiPn@gondola.proxy.rlwy.net:26336/railway"

def conectar_db():
    """Cria e retorna uma conexão com o banco de dados PostgreSQL"""
    try:
        # Conectando-se ao PostgreSQL usando a URL de conexão fornecida
        return psycopg2.connect(DATABASE_URL, sslmode="require")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def ler_todas_operadoras():
    """Lê todos os dados da tabela 'DADOS_OPERADORAS_ATIVAS'"""
    try:
        conn = conectar_db()
        if conn is None:
            return []  # Retorna lista vazia caso a conexão falhe

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
    """Busca operadoras com base em um termo fornecido"""
    try:
        conn = conectar_db()
        if conn is None:
            return []  # Retorna lista vazia caso a conexão falhe

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
def listar_operadoras():
    """Lista todas as operadoras"""
    operadoras = ler_todas_operadoras()
    for operadora in operadoras:
        for chave, valor in operadora.items():
            if valor is None:
                operadora[chave] = "Dado não disponível"
    response = make_response(jsonify(operadoras))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/operadoras/<termo>', methods=['GET'])
def buscar(termo):
    """Busca operadoras com base no termo fornecido"""
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
    port = int(os.getenv("PORT", 5000))  # Usa a porta correta no Railway
    app.run(debug=True, host="0.0.0.0", port=port)
