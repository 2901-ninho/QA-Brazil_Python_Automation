import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get("https://cnt-33ad9f32-8ed3-4dae-998e-f465cd677ccb.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre todos os elementos na página usando um seletor de XPath
elements = driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']")

# Verifique se o número de elementos encontrados é maior que 1 usando len()
assert len(elements) > 1, f"Esperado mais de 1 elemento, mas foram encontrados: {len(elements)}"

print(f"Sucesso! Foram encontrados {len(elements)} elementos com a classe 'dst-picker-marker'.")

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()