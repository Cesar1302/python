# Librerías
from tkinter import Radiobutton
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd


driver = webdriver.Chrome(executable_path= r'C:\chromedriver\chromedriver.exe')

#driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(0000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('http://www.aire.cdmx.gob.mx')
time.sleep(3)
pestaña = driver.find_element_by_xpath("//*[@id='displayimecahome']/ul/li[9]/a")\
    .click()
time.sleep(3)
interactivo = driver.find_element_by_xpath("//*[@id='displayimecahome']/ul/li[9]/div/div[2]/p[4]/a")\
    .click()
time.sleep(3)

#serie = driver.find_element_by_xpath("/html/body/form/fieldset/div/div/label[1]")\
#    .click()
#time.sleep(3)
input()
