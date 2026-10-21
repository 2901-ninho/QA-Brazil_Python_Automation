import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cnt-60987c38-a9d9-4abf-bcf7-1b93762eb528.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo DE e o preencha
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Encontre o campo PARA e o preencha
driver.find_element(By.ID, "to").send_keys("1300 1st St")

time.sleep(2)

# Obtenha o texto do modo ativo utilizando o XPath fornecido e a propriedade .text
mode = driver.find_element(By.XPATH, "//div[@class='mode active']").text

time.sleep(2)

# Faça um assert para verificar se o texto da variável mode contém/é "Flash"
assert mode == "Flash", f"Esperado 'Flash', mas obtido '{mode}'"

driver.quit()