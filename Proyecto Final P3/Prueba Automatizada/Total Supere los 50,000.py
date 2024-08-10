from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/path/to/brave'  
service = Service('/path/to/chromedriver')  
driver = webdriver.Chrome(service=service, options=chrome_options)


if not os.path.exists('capturas_automizadas'):
    os.makedirs('capturas_automizadas')

try:
    
    driver.get("http://127.0.0.1:5500/Proyecto%20final%20p3/carrito.html")
    time.sleep(3)

    num_productos = 10

    for i in range(1, num_productos + 1):

        boton_agregar = driver.find_element(By.ID, f"agregar-producto-{i}")
        boton_agregar.click()
        time.sleep(2)  
        
        
        total_element = driver.find_element(By.ID, "total")  
        total_text = total_element.text
        total_value = float(total_text.replace('$', '').replace(',', ''))

        if total_value > 50000:
            driver.save_screenshot(f'capturas_automizadas/paso_{i}_total_excede_50000.png')

   

finally:
    driver.quit()
