# Importa las librerías necesarias de Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Importa otras librerías necesarias para el manejo del sistema operativo, variables de entorno y tiempos de espera
import os
from dotenv import load_dotenv, find_dotenv
import time

# URL de la página web a la que se accederá
url = 'https://katalon-demo-cura.herokuapp.com/'

# Inicializa el navegador
driver = webdriver.Chrome()

# Maximiza la ventana del navegador
driver.maximize_window()

# Abre la página web
driver.get(url)

# Espera un tiempo suficiente para que la página se cargue completamente
driver.implicitly_wait(10)

try:
    # Espera hasta que el botón Make Appointment sea visible
    button_make_appoinment = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "btn-make-appointment"))
    )
    # Hace clic en el botón Make Appointment
    button_make_appoinment.click()

    # Carga las variables de entorno para inicio de sesión desde un archivo .env el cual se encuentra en la ruta raíz
    load_dotenv("archivo.env")
    username = os.getenv("USER_LOGIN")
    password = os.getenv("PASSWORD_LOGIN")
    
    # Encuentra los input para los campos username y password
    input_username = driver.find_element(By.ID, "txt-username")
    input_password = driver.find_element(By.ID, "txt-password")
    
    # Ingresa el nombre de usuario y contraseña en los respectivos input
    input_username.send_keys(username)
    input_password.send_keys(password)
    
    # Tiempo de espera para poder visualizar en pantalla las acciones
    time.sleep(5)
    
    # Encuentra y hace clic en el botón Login
    button_login = driver.find_element(By.ID, "btn-login")
    button_login.click()
    
    # Tiempo de espera para poder visualizar en pantalla las acciones
    time.sleep(5)
    
    # Verifica si la URL después del inicio de sesión es la esperada
    url_expected_after_login = 'https://katalon-demo-cura.herokuapp.com/#appointment'
    current_url = driver.current_url
    
    if url_expected_after_login == current_url:
        print(f'El botón login redirecciona correctamente')
    else:
        print(f'El botón login no redirecciona correctamente, se esperaba que redirija a la url: {url_expected_after_login}')
    
    
    #Manejo de excepciones, cuando algún elemento no se encuentra en un tiempo especifico
except TimeoutException:
    print("TimeoutException: No se encontró el elemento dentro del tiempo especificado.")
        
finally:
    # Cierra el navegador
    driver.quit()