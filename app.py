from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

PATH = './Python_Postgres/dados_operadoras/Relatorio_cadop.csv'

def buscar_operadoras(termo_busca):
    resultados = []
    with open(PATH, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            for valor in linha.values():
                if termo_busca.lower() in str(valor).lower():
                    resultados.append(linha)
                    break
    return resultados

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo')
    if not termo:
        return jsonify({'erro': 'Termo de busca não fornecido'}), 400
    resultados = buscar_operadoras(termo)
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)


# **3. Criação da Interface Vue.js:**
#
# * Desenvolva uma interface web usando Vue.js que consuma a API criada no servidor Python.
# * A interface deve permitir que o usuário insira um termo de busca e exiba os resultados retornados pela API.
# * Você pode usar bibliotecas como Axios para fazer as requisições HTTP para o servidor Python.
#
# **4. Elaboração da Coleção no Postman:**
#
# * **4.3. Demonstração do resultado no Postman:**
#     * O Postman é uma ferramenta excelente para testar APIs. Crie uma coleção no Postman que contenha as requisições para a rota de busca textual do seu servidor Python.
#     * Inclua exemplos de requisições com diferentes termos de busca e mostre os resultados retornados pela API.
#     * Isso ajudará a demonstrar que a API está funcionando corretamente e retornando os dados esperados.



