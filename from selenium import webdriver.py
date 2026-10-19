from selenium import webdriver

# Inicializa o navegador (ex: Chrome)
driver = webdriver.Chrome()

try:
    # 1. Abre a página inicial do Urban Routes
    driver.get("https://cnt-3e86aff3-3c71-4735-9456-1a4c064588d5.containerhub.tripleten-services.com?lng=pt")

    # 2. Verifica se a URL atual contém 'tripleten-services.com' usando assert
    assert 'tripleten-services.com' in driver.current_url, f"Erro: A URL atual é '{driver.current_url}'"

    print("Sucesso! A página foi aberta e a verificação da URL passou.")

finally:
    # 3. Fecha o navegador após o teste (garante que fechará mesmo se houver falha no assert)
    driver.quit()