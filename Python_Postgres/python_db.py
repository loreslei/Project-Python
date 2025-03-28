import psycopg2, csv
PASSWORD = "12345678"
try:
    conexao_db = psycopg2.connect(database="operadoras_ativas",
                                  host="localhost",
                                  user="postgres",
                                  password=PASSWORD,
                                  port="5432")

    print(conexao_db.info)
    print(conexao_db.status)

    dados_operadoras_ativas = ''' CREATE TABLE DADOS_OPERADORAS_ATIVAS (
    Id_Empresa SERIAL,
    Registro_ANS varchar(20) NOT NULL,
    CNPJ varchar(20) NOT NULL,
    Razao_Social varchar(100) NOT NULL,
    Nome_Fantasia varchar(100),
    Modalidade varchar(50) NOT NULL,
    Logradouro varchar(100) NOT NULL,
    Numero varchar(20) NOT NULL,
    Complemento varchar(50),
    Bairro varchar(70) NOT NULL,
    Cidade varchar(100) NOT NULL,
    UF varchar(2) NOT NULL,
    CEP varchar(9) NOT NULL,
    DDD int NOT NULL,
    Telefone varchar(8) NOT NULL,
    Fax varchar(8),
    Endereco_eletronico varchar(255) NOT NULL,
    Representante varchar(80) NOT NULL,
    Cargo_Representante varchar(50) NOT NULL,
    Regiao_de_Comercializacao int NOT NULL,
    Data_Registro_ANS date NOT NULL,
    PRIMARY KEY (Id_Empresa))
    '''

    dados_2023 = ''' CREATE TABLE DADOS_2023 (
        ID SERIAL,
        DATA date NOT NULL,
        REG_ANS varchar(6) NOT NULL,
        CD_CONTA_CONTABIL varchar(100) NOT NULL,
        DESCRICAO varchar(70) NOT NULL,
        VL_SALDO_INICIAL float NOT NULL,
        VL_SALDO_FINAL float NOT NULL,
        PRIMARY KEY (ID))
        '''

    dados_2024 = ''' CREATE TABLE DADOS_2024 (
            ID SERIAL,
            DATA date NOT NULL,
            REG_ANS varchar(6) NOT NULL,
            CD_CONTA_CONTABIL varchar(100) NOT NULL,
            DESCRICAO varchar(70) NOT NULL,
            VL_SALDO_INICIAL float NOT NULL,
            VL_SALDO_FINAL float NOT NULL,
            PRIMARY KEY (ID))
            '''


    deletar_tabela1 = '''
    DROP TABLE DADOS_2023;
    '''

    deletar_tabela2 = '''
    DROP TABLE DADOS_2024;
    '''


    deletar_tabela3 = '''
    DROP TABLE DADOS_OPERADORAS_ATIVAS;
    '''

    cur = conexao_db.cursor()
    cur.execute(dados_operadoras_ativas)
    cur.execute(dados_2023)
    cur.execute(dados_2024)

    #cur.execute(deletar_tabela1)
    #cur.execute(deletar_tabela2)
    #cur.execute(deletar_tabela3)

    cur.close()
    conexao_db.commit()
    conexao_db.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
