import pandas as pd # dados

from selenium import webdriver # interação com a página web
from selenium.webdriver.support.select import Select # selecionar
from selenium.webdriver.common.by import By # procurar
from selenium.webdriver.common.keys import Keys # simular cliques e digitação

# Iniciando o Browser
path_driver = './driver/'
url = 'https://03felipesampaio.github.io/'
driver = webdriver.Firefox(path_driver) 
driver.get(url)

driver.maximize_window()

usuario = 'giuli@gmail.com'
xpath_usuario = r'//*[@id="usuario"]'
login_box = driver.find_element("xpath", xpath_usuario)
login_box.click()

login_box.send_keys(usuario)

xpath_senha = r'//*[@id="senha"]'
password_box = driver.find_element("xpath", xpath_senha)
password_box.click()
password_box.send_keys("senha")

xpath_enter = r'//*[@id="btn-entrar"]'
password_box = driver.find_element("xpath", xpath_enter)
password_box.click()