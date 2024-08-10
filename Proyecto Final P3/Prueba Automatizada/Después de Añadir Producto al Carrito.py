from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)


if not os.path.exists('capturas_automizadas'):
    os.makedirs('capturas_automizadas')

try:
    
    driver.get("http://127.0.0.1:5500/Proyecto%20final%20p3/carrito.html")

  
    time.sleep(3)
    boton_anadir = driver.find_element(By.CSS_SELECTOR, ".boton-anadir")
    boton_anadir.click()
    time.sleep(2)

   
    driver.save_screenshot('capturas_automizadas/anadir_producto.png')

finally:
    driver.quit()
