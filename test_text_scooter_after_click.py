import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM

def test_personal_scooter_option():
    # Etapa 1: Abra o aplicativo
    driver = webdriver.Chrome()
    driver.get('https://cnt-1863d56f-c0c9-450f-82bc-339649cb62dc.containerhub.tripleten-services.com?lng=pt')

    # Etapa 2: Aguarde a página carregar por completo (evita o erro de elemento não encontrado)
    time.sleep(3)

    # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)

    # Etapa 3: use métodos POM para executar ações na página
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    # Selecione a opção "Personal".
    urban_routes_page.click_personal_option()
    time.sleep(1)

    # Clique no ícone "Scooter".
    urban_routes_page.click_scooter_icon()
    time.sleep(1)

    # Etapa 4: Verifique se o texto Scooter é exibido corretamente
    actual_value = urban_routes_page.get_scooter_text()
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"

    # Fecha o navegador ao finalizar com sucesso
    driver.quit()