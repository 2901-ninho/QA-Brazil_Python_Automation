import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# Insira a URL atual do seu container do Urban Routes
driver.get("https://cnt-c7d84699-331d-4a05-ac05-6c0ededa4e13.containerhub.tripleten-services.com/")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo DE e o preencha
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Encontre o campo PARA e o preencha
driver.find_element(By.ID, "to").send_keys("1300 1st St")

time.sleep(2)

# Encontre o botão "Chamar um táxi" e clique nele
driver.find_element(By.XPATH, "//button[@class='button round']").click()

# Adicione uma espera explícita para que o campo de comentário carregue
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "comment")))

# Escreva um comentário para o motorista
comment_text = "Compre um café, por favor"
driver.find_element(By.ID, "comment").send_keys(comment_text)

time.sleep(2)

# Verifique se o seu comentário é o esperado usando assert e get_attribute("value")
assert driver.find_element(By.ID, "comment").get_attribute("value") == comment_text

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()