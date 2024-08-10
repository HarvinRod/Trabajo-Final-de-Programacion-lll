from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

# Configuración del WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)


if not os.path.exists('capturas_automizadas'):
    os.makedirs('capturas_automizadas')

try:
    
    driver.get("http://127.0.0.1:5500/Proyecto%20final%20p3/carrito.html")

    
    time.sleep(3)

    
    boton_comprar = driver.find_element(By.ID, "carrito-acciones-comprar")
    boton_comprar.click()
    time.sleep(2)

    
    driver.save_screenshot('capturas_automizadas/estado_post_compra.png')

finally:
    driver.quit()
