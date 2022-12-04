from distutils import extension
from operator import not_
from os import close, remove, write
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import shutil 
from shutil import copy2, copytree
from shutil import copy
from shutil import move
import glob
from os import remove
import urllib.request
from PIL import Image
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

espacio='-------------'

print(espacio)
url1 = 'https://www.oh-iiunam.mx/geojson/datospaginadia.txt'
file1 = r'C:\Users\videowall_08\Documents\Mapas\DATOSOH.csv'
#file1 = 'DATOSOH.csv'
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
print('Datos de OH obtenidos')


OH = pd.read_csv(r'C:\Users\videowall_08\Documents\Mapas\DATOSOH.csv', index_col=0, header=None , sep = ' ', usecols=(1,2))
#print(OH)
roundplaces = np.round(OH,decimals=2)
roundplaces.to_csv(r'C:\Users\videowall_08\Documents\Mapas\DATOSOH.csv')

dF = pd.read_csv(r'C:\Users\videowall_08\Documents\Mapas\DATOSOH.csv', index_col=0, header=1)
print(dF)
dF.to_csv(r'C:\Users\videowall_08\Documents\Mapas\DATOSOH.csv')

fecha= date.today()
fecha_lluvias=fecha - timedelta(days=1)
fecha_ayer=fecha_lluvias.strftime("%d/%m/%Y") 
print(fecha_ayer)  

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('http://10.11.11.154/SACMEX/')
driver.implicitly_wait(5)

#click en informes
driver.find_element(By.CSS_SELECTOR, "#menu > ul > li:nth-child(3) > a")\
    .click()
#click en isoyetas
driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div[1]/ul/li[7]/a")\
    .click()


span=driver.find_element(By.CSS_SELECTOR, "#tab4_7 > iframe")

driver.switch_to.frame(span)

driver.find_element(By.XPATH,"//*[@id='form:calendar_input']")\
    .clear()\

driver.find_element(By.XPATH,"//*[@id='form:calendar_input']")\
   .send_keys(fecha_ayer)

driver.find_element(By.CSS_SELECTOR,"#form\:j_idt20 > span")\
    .click()

time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='formDownload:j_idt31']/span")\
    .click()
time.sleep(10)
driver.close()

espacio="-------------"
now = datetime.now()
fecha= date.today()
print(espacio)
"""date"""
fecha_temperaturas=fecha
#print(fecha_temperaturas)
print(espacio)
fecha_lluvias=fecha - timedelta(days=1)
print(espacio)
#print(fecha_lluvias)


fecha= date.today()
fecha_lluvias=fecha - timedelta(days=1)
fecha_ayer=fecha_lluvias.strftime("%d/%m/%Y") 
print(fecha_ayer)  


format_lluvia = fecha_lluvias.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format_lluvia)

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.strftime("%d")
    month = months[date.month - 1]
    year = date.year
    messsage = "{}{}{}".format(day, month, year)

    return messsage

fecha_lluvias=fecha - timedelta(days=1)
fecha_final_lluvia=(current_date_format(fecha_lluvias))
print(fecha_final_lluvia)

archivo = 'C:/Users/videowall_08/Downloads/'+fecha_final_lluvia+'_A.dat'
print(archivo)
sacmex = open(archivo, 'r')
txt = sacmex.read()
txt1=open(r'C:\Users\videowall_08\Documents\Mapas\SACMEX.csv','w')
txt1.write(txt)
txt1.close()

DSACMEX= OH = pd.read_csv(r'C:\Users\videowall_08\Documents\Mapas\SACMEX.csv', index_col=0, header=1 , usecols=(0,1))
print(DSACMEX)
roundplaces = np.round(OH,decimals=2)
roundplaces.to_csv(r'C:\Users\videowall_08\Documents\Mapas\SACMEX.csv')
print('Datos de SACMEX obtenidos')
exit()
