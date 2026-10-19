import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
# Substitua nosso link pelo link do seu próprio servidor aqui
driver.get("https://cnt-7af15b2d-d9e4-40e1-8694-f0e95127e575.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(5)

# Encontre o elemento de logotipo usando seu seletor de CSS
element = driver.find_element(By.CSS_SELECTOR, "img.logo-image")

# Imprima o elemento encontrado no console
print(element)

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()