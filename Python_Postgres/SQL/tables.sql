
CREATE TABLE DADOS_OPERADORAS_ATIVAS (
    Id_Empresa SERIAL PRIMARY KEY,
    Registro_ANS varchar(50) NOT NULL,
    CNPJ varchar(20) NOT NULL,
    Razao_Social varchar(300) NOT NULL,
    Nome_Fantasia varchar(100),
    Modalidade varchar(50) NOT NULL,
    Logradouro varchar(100) NOT NULL,
    Numero varchar(50) NOT NULL,
    Complemento varchar(50),
    Bairro varchar(70) NOT NULL,
    Cidade varchar(100) NOT NULL,
    UF varchar(2) NOT NULL,
    CEP varchar(9) NOT NULL,
    DDD int,
    Telefone varchar(50),
    Fax varchar(15),
    Endereco_eletronico varchar(255),
    Representante varchar(80) NOT NULL,
    Cargo_Representante varchar(50) NOT NULL,
    Regiao_de_Comercializacao int,
    Data_Registro_ANS date NOT NULL
);

CREATE TABLE DADOS_2023 (
	ID_EMP SERIAL PRIMARY KEY,
	DATAS date NOT NULL,
	REG_ANS varchar(6) NOT NULL,
	CD_CONTA_CONTABIL varchar(100) NOT NULL,
	DESCRICAO varchar(300) NOT NULL,
	VL_SALDO_INICIAL varchar(30) NOT NULL,
	VL_SALDO_FINAL varchar(30) NOT NULL
);

CREATE TABLE DADOS_2024 (
		ID_EMP SERIAL PRIMARY KEY,
		DATAS date NOT NULL,
		REG_ANS varchar(6) NOT NULL,
		CD_CONTA_CONTABIL varchar(100) NOT NULL,
		DESCRICAO varchar(300) NOT NULL,
		VL_SALDO_INICIAL varchar(30) NOT NULL,
		VL_SALDO_FINAL varchar(30) NOT NULL
);


	