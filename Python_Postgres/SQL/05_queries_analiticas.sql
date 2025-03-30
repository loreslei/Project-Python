-- Queries Analíticas

-- Consulta 1

SELECT
    dados_operadoras_ativas.razao_social as operadoras,
    dados_2023.descricao AS descricao,
	dados_2023.datas AS datas,
    dados_2023.vl_saldo_final::NUMERIC AS despesas
FROM
    dados_operadoras_ativas
INNER JOIN
    dados_2023 ON dados_operadoras_ativas.registro_ans = dados_2023.reg_ans
WHERE descricao ILIKE 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE' AND EXTRACT(MONTH FROM datas) BETWEEN 10 AND 12
ORDER BY despesas ASC
LIMIT 10;

SELECT
    dados_operadoras_ativas.razao_social as operadoras,
    dados_2024.descricao AS descricao,
	dados_2024.datas AS datas,
    dados_2024.vl_saldo_final::NUMERIC AS despesas
FROM
    dados_operadoras_ativas
INNER JOIN
    dados_2024 ON dados_operadoras_ativas.registro_ans = dados_2024.reg_ans
WHERE descricao ILIKE 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE' AND EXTRACT(MONTH FROM datas) BETWEEN 10 AND 12
ORDER BY despesas ASC
LIMIT 10;

-- Consulta 2

SELECT
    dados_operadoras_ativas.razao_social as operadoras,
    SUM(dados_2024.vl_saldo_final::NUMERIC) AS total_despesas
FROM
    dados_operadoras_ativas
INNER JOIN
    dados_2024 ON dados_operadoras_ativas.registro_ans = dados_2024.reg_ans
WHERE descricao ILIKE 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE'
GROUP BY dados_operadoras_ativas.razao_social
ORDER BY total_despesas ASC
LIMIT 10;

SELECT
    dados_operadoras_ativas.razao_social as operadoras,
    SUM(dados_2023.vl_saldo_final::NUMERIC) AS total_despesas
FROM
    dados_operadoras_ativas
INNER JOIN
    dados_2023 ON dados_operadoras_ativas.registro_ans = dados_2023.reg_ans
WHERE descricao ILIKE 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE'
GROUP BY dados_operadoras_ativas.razao_social
ORDER BY total_despesas ASC
LIMIT 10;



