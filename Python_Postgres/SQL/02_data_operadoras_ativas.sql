-- Importando Dados de Operadoras Ativas
COPY dados_operadoras_ativas (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS)
FROM 'C:/Project-Python/Python_Postgres/dados_operadoras/Relatorio_cadop.csv'
WITH (FORMAT CSV, HEADER, ENCODING 'UTF8', DELIMITER ';');

SELECT * FROM dados_operadoras_ativas;