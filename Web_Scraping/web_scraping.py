from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from zipfile import ZipFile
import os


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

link_gov = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

navegador.get(link_gov)

navegador.find_element('xpath',
                       '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]').click()


navegador.quit()

# Compactar para Arquivo zip
arquivos_para_zip = ["arquivo1.txt", "arquivo2.txt"]

with ZipFile("arquivo_compactado.zip", "w") as zip_file:
    for arquivo in arquivos_para_zip:
        if os.path.exists(arquivo):
            zip_file.write(arquivo)
        else:
            print(f"Arquivo {arquivo} não encontrado.")

# Extrair Arquivo zip
with ZipFile("arquivo_compactado.zip", "r") as zip_file:
    zip_file.extractall("arquivos_extraidos")

print("Processo concluído.")