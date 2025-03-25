import os
from zipfile import ZipFile
import tabula
import pandas as pd
from PyPDF2 import PdfReader
from tabulate import tabulate
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DIRETORIO_ANEXO_I = "../Web_Scraping/anexoI.pdf"
NOME_ARQUIVO = "anexoI.csv"
NOME_ZIP = "Teste_Lorenna.zip"

# 2.4.
# Substitua as abreviações das colunas OD e AMB pelas descrições completas, conforme a legenda no rodapé.

PARTS = []

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y < 50:
        if text != "" and text != "\n":
            PARTS.append(text)

def extrair_conteudo(arquivo):
    reader = PdfReader(arquivo)
    page = reader.pages[2]
    page.extract_text(visitor_text=visitor_body)
    text_body = "".join(PARTS)
    # OD: Seg. Odontológica
    # AMB: Seg. Ambulatorial
    print(PARTS)

def transformar_em_csv(diretorio, arquivo):
    tabula.convert_into(diretorio, arquivo, output_format="csv", pages='3-181')
    data_frame_anexo = pd.read_csv(arquivo)
    print(tabulate(data_frame_anexo, headers='keys'))

def zipar(arquivo, diretorio_zip):
    with ZipFile(diretorio_zip, "w") as zip_file:
        zip_file.write(arquivo)
        logging.info(f"Arquivo '{NOME_ARQUIVO}' adicionado ao zip.")


#
# if os.path.exists(NOME_ARQUIVO):
#     zipar(NOME_ARQUIVO, NOME_ZIP)
# else:
#     logging.warning(f"Arquivo '{NOME_ARQUIVO}' não encontrado.")
#     if os.path.exists(DIRETORIO_ANEXO_I):
#         extrair_conteudo(NOME_ARQUIVO)
#         transformar_em_csv(DIRETORIO_ANEXO_I, NOME_ARQUIVO)
#         zipar(NOME_ARQUIVO, NOME_ZIP)
#     else:
#         logging.warning(f"Arquivo '{DIRETORIO_ANEXO_I}' não encontrado.")




extrair_conteudo(DIRETORIO_ANEXO_I)
