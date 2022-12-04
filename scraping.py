# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = r'C:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
#driver.set_window_position(0000, 0)
#driver.maximize_window()
#time.sleep(1)

# Inicializamos el navegador
driver.get('http://10.11.11.154/SACMEX/')
current_window = driver.current_window_handle

pagina_inicio = driver.page_source
print(pagina_inicio) 
#driver.find_element(By.CSS_SELECTOR,"#menu > ul > li:nth-child(3) > a")\
#.click()


#driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div[1]/ul/li[7]/a")\
#    .click()

#driver.find_element(By.ID,("form:calendar_input"))\
#    .click()

input()