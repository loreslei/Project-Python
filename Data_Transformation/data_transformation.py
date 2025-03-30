import os
from zipfile import ZipFile
import tabula
import pandas as pd
from PyPDF2 import PdfReader
from IPython.display import display
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DIRETORIO_ANEXO_I = "../Web_Scraping/anexoI.pdf"
NOME_ARQUIVO = "anexoI.csv"
NOME_ZIP = "Teste_Lorenna.zip"

PARTS = []
SUBSTITUICOES = []

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y < 50:
        if text != "" and text != "\n":
            PARTS.append(text.split(": "))

def subst_palavras(pdf, arquivo):

    page = PdfReader(pdf).pages[2]
    page.extract_text(visitor_text=visitor_body)
    # OD: Seg. Odontológica
    SUBSTITUICOES.append(PARTS[0][1])
    # AMB: Seg. Ambulatorial
    SUBSTITUICOES.append(PARTS[1][1])

    df = pd.read_csv(arquivo)
    df["OD"] = df["OD"].str.replace("OD", SUBSTITUICOES[0], regex=True)
    df["AMB"] = df["AMB"].str.replace("AMB", SUBSTITUICOES[1], regex=True)

    df = df.rename(columns={
        "OD": SUBSTITUICOES[0],
        "AMB": SUBSTITUICOES[1]
    })

    df.to_csv(arquivo, index=False)



def extrair_conteudo(pdf):
    lista_tabelas = tabula.read_pdf(pdf, pages='3-181')
    for tabela in lista_tabelas:
        display(tabela)


def transformar_em_csv(pdf, novo_arquivo):
    tabula.convert_into(pdf, novo_arquivo, output_format="csv", pages='3-181')
    subst_palavras(pdf, novo_arquivo)

    #Comprovar Exibição do CSV
    '''  
    data_frame_anexo = pd.read_csv(novo_arquivo)
    print(tabulate(data_frame_anexo, headers='keys'))
    '''

def zipar(arquivo, diretorio_zip):
    with ZipFile(diretorio_zip, "w") as zip_file:
        zip_file.write(arquivo)
        logging.info(f"Arquivo '{NOME_ARQUIVO}' adicionado ao zip.")



if os.path.exists(NOME_ARQUIVO):
    zipar(NOME_ARQUIVO, NOME_ZIP)
else:
    logging.warning(f"Arquivo '{NOME_ARQUIVO}' não encontrado.")
    if os.path.exists(DIRETORIO_ANEXO_I):
        extrair_conteudo(DIRETORIO_ANEXO_I)
        transformar_em_csv(DIRETORIO_ANEXO_I, NOME_ARQUIVO)
        zipar(NOME_ARQUIVO, NOME_ZIP)
    else:
        logging.warning(f"Arquivo '{DIRETORIO_ANEXO_I}' não encontrado.")



