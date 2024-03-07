# Automatizacion-Katalon
Este proyecto tiene como objetivo automatizar la interacción con un formulario web utilizando Selenium WebDriver. En este caso, se utiliza una página de demostración disponible en https://katalon-demo-cura.herokuapp.com/.

## Requisitos
Antes de ejecutar el script de automatización, asegúrate de tener instalado lo siguiente:

- Python 3.11.0
- Selenium WebDriver
- Chromedriver (o el controlador adecuado para tu navegador)
- Python Dotenv

Puedes instalar las dependencias necesarias utilizando pip:

Copy code
pip install selenium python-dotenv

Uso
Clona este repositorio en tu máquina local:
bash
Copy code
git clone https://github.com/tu-usuario/nombre-repositorio.git
Ve al directorio del proyecto:
bash
Copy code
cd nombre-repositorio
Crea un archivo .env en el directorio raíz del proyecto y configura las variables de entorno USER_LOGIN y PASSWORD_LOGIN con tus credenciales de inicio de sesión.
makefile
Copy code
USER_LOGIN=usuario
PASSWORD_LOGIN=contraseña
Ejecuta el script de automatización:
Copy code
python script.py
El script abrirá un navegador, iniciará sesión en la página de demostración y verificará si la redirección después del inicio de sesión es la esperada.

Notas
Asegúrate de que el controlador del navegador esté instalado y configurado correctamente en tu sistema.
Es posible que necesites ajustar las esperas (time.sleep()) según la velocidad de carga de la página y la latencia de la red.
