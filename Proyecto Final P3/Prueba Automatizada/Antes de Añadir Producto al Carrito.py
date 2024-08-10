from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

    
    driver.save_screenshot('capturas_automizadas/antes_anadir_producto.png')

finally:
    driver.quit()
