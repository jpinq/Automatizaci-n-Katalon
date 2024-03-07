from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv,find_dotenv
import time


url = 'https://katalon-demo-cura.herokuapp.com/'

# Inicializa el navegador (asegúrate de tener el controlador adecuado instalado, por ejemplo, chromedriver)
driver = webdriver.Chrome()

#Maximiza la ventana del navegador
driver.maximize_window()

# Abre la página web
driver.get(url)

# Espera un tiempo suficiente para que la página se cargue completamente (puedes ajustar el tiempo según sea necesario)
driver.implicitly_wait(10)

try:
    # Espera hasta que el botón esté presente en el DOM y visible
    button_make_appoinment = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "btn-make-appointment"))
    )
    # Hace clic en el botón
    button_make_appoinment.click()

 
    load_dotenv("archivo.env")
    username = os.getenv("USER_LOGIN")
    password = os.getenv("PASSWORD_LOGIN")
    
    input_username = driver.find_element(By.ID,"txt-username")
    input_password = driver.find_element(By.ID,"txt-password")
    
    
    input_username.send_keys(username)
    input_password.send_keys(password)
    
    time.sleep(5)
    
    button_login = driver.find_element(By.ID,"btn-login")
    
    button_login.click()
    
    time.sleep(5)
    
    url_expected_after_login = 'https://katalon-demo-cura.herokuapp.com/#appointment'
    
    current_url = driver.current_url
    
    if url_expected_after_login == current_url:
        print(f'El botón login redirecciona correctamente')
    else:
        print(f'El boton login no redirecciona correctamente se esperaba visualizar la url {url_expected_after_login}')
    
    
except TimeoutException:
    print("TimeoutException: No se encontró el elemento dentro del tiempo especificado.")    
        
finally:
    # Cierra el navegador
    driver.quit()