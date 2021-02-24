from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint, choices
from config import *

#Abre o navegador e entra no site do Instagram
navegador = webdriver.Chrome(executable_path="./chromedriver.exe")
navegador.get(siteInstagram)

#Login
sleep(2)
usuario = navegador.find_element_by_xpath("//input[@name = 'username']")
usuario.click()
usuario.send_keys(usuarioInstagram)
sleep(1)
senha = navegador.find_element_by_xpath("//input[@name = 'password']")
senha.click()
senha.send_keys(senhaInstagram)
senha.send_keys(Keys.ENTER)

#Verificação
sleep(3)
navegador.find_element_by_xpath("//button[@class = 'sqdOP yWX7d    y3zKF     ']").click()

sleep(3)
navegador.find_element_by_xpath("//button[@class = 'aOOlW   HoLwm ']").click()

#Navegação para a página do sorteio
navegador.get(linkSorteio)

#Interação com a página
sleep(3)
caixa_comentario = navegador.find_element_by_class_name('Ypffh')
caixa_comentario.click()

#preparar para digitar
for intervalo in range(300, 900):
    for i in range(0, randint(4, 6)):
        caixa_comentario = navegador.find_element_by_class_name('Ypffh')
        caixa_comentario.send_keys(choices(lista_comentarios)[0])
        caixa_comentario.send_keys(Keys.ENTER)
        sleep(randint(2, 8))

    sleep(randint(120, 180))