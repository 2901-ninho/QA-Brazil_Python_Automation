import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get("https://cnt-c7d84699-331d-4a05-ac05-6c0ededa4e13.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Localiza o botão de limpar (X) e clica nele em uma única instrução de código usando XPath
driver.find_element(By.XPATH, "//button[@class='close-button input-close-button']").click()

# Pausa breve para visualizar a mensagem de erro vermelha "Insira o endereço" na tela
time.sleep(2)

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()