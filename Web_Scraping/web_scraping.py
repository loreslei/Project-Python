from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from zipfile import ZipFile
import os
import requests
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clicar_elemento(navegador, xpath, timeout=10):
    try:
        elemento = WebDriverWait(navegador, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        elemento.click()
        return True
    except TimeoutException:
        logging.error(f"Elemento com XPath '{xpath}' não estava clicável após {timeout} segundos.")
        return False
    except Exception as e:
        logging.error(f"Erro ao clicar no elemento com XPath '{xpath}': {e}")
        return False

def baixar_arquivo(url, nome_arquivo):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(nome_arquivo, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        logging.info(f"Arquivo '{nome_arquivo}' baixado com sucesso.")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao baixar arquivo '{nome_arquivo}': {e}")
        return False

def baixar_arquivos_web():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": os.getcwd()}
    chrome_options.add_experimental_option("prefs", prefs)

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=chrome_options)

    link_gov = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    navegador.get(link_gov)

    xpath_cookies = '/html/body/div[5]/div/div/div/div/div[2]/button[3]'
    xpath_anexo1 = '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]'
    xpath_anexo2 = '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a'

    if clicar_elemento(navegador, xpath_cookies):
        link_anexo_I = navegador.find_element(By.XPATH, xpath_anexo1).get_attribute('href')
        baixar_arquivo(link_anexo_I, "anexoI.pdf")

        link_anexo_II = navegador.find_element(By.XPATH, xpath_anexo2).get_attribute('href')
        baixar_arquivo(link_anexo_II, "anexoII.pdf")

    navegador.quit()
    logging.info("Download concluído.")

# Compactar para Arquivo zip
arquivos_para_zip = ["anexoI.pdf", "anexoII.pdf"]

while True:
    todos_encontrados = True

    with ZipFile("anexos_gov.zip", "w") as zip_file:
        for arquivo in arquivos_para_zip:
            if os.path.exists(arquivo):
                zip_file.write(arquivo)
                logging.info(f"Arquivo '{arquivo}' adicionado ao zip.")
            else:
                logging.warning(f"Arquivo '{arquivo}' não encontrado. Baixando novamente.")
                baixar_arquivos_web()
                todos_encontrados = False
                break

    if todos_encontrados:
        print("Aquivos zipados com sucesso.")
        break





