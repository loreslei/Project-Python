from selenium import webdriver
from time import sleep
from zipfile import ZipFile

navegador = webdriver.Chrome()

navegador.get("""https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-
sociedade/atualizacao-do-rol-de-procedimentos""")

navegador.find_element_by_xpath('//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]').click()
sleep(3)

navegador.quit()


#Compactar para Arquivo zip
with ZipFile("arquivo_compactado.zip", "w") as zip:
    zip.write("arquivo1.txt")
    zip.write("arquivo2.txt")
    
#Extrair Arquivo zip