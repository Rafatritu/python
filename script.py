from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configuração do WebDriver para o Chrome
driver = webdriver.Chrome()

# URL do Habbo
url = "https://www.habbo.com.br/"

# Navega até a página do Habbo
driver.get(url)

# Aguarda alguns segundos para carregar completamente a página
time.sleep(5)

# Localiza o elemento do personagem (pode ser um elemento específico do jogo)
personagem = driver.find_element_by_id("id_do_personagem")

# Enquanto o script estiver em execução, siga o personagem
while True:
    # Movimenta o personagem para a direita
    ActionChains(driver).move_to_element(personagem).perform()
    # Aguarda um curto período para si
