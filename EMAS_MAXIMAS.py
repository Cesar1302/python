from distutils import extension
from operator import not_
from os import close, remove, write
import os
import time  
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
fechasmn= time.strftime('%Y-%m-%d')
print(fechasmn)
urlmax = ('https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/consultaMaxMin.php?var=temperatura&valor=maximo&tipo=descarga&area=estado&idestado=9&idmunic=0&fechaInicial='+fechasmn+'%2000:00:50&fechaFinal='+fechasmn+'%2018:10:50')
#https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/consultaMaxMin.php?var=temperatura&valor=maximo&tipo=descarga&area=estado&idestado=9&idmunic=0&fechaInicial=2022-08-05%2000:00:50&fechaFinal=2022-08-05%2018:20:50
print(urlmax)
filemax = 'EMAS_MAXIMAS.csv'
r = urllib.request.urlopen(urlmax)
f = open(filemax,'wb')
f.write(r.read())
f.close()
print('Datos de extremos maximos del SMN obtenidos')

f=  'Periodo del ' + fechasmn + ' 00:00:50 al: ' + fechasmn + ' 18:10:50'
#print(f)
EMAS = open(r'C:\Users\videowall_08\Documents\Mapas\EMAS_MAXIMAS.csv','r')
txt=EMAS.read()
cambio0=txt.replace('"','')
cambio1=cambio0.replace('Servicio Meteorológico Nacional','')
cambio2=cambio1.replace('Valor maximo de la Variable: temperatura','')
cambio3=cambio2.replace(f,'')
#print(cambio3)
txt=open(r'C:\Users\videowall_08\Documents\Mapas\EMAS_MAXIMAS.csv','w')
txt.write(cambio3)
txt.close()

dF = pd.read_csv(r'C:\Users\videowall_08\Documents\Mapas\EMAS_MAXIMAS.csv', index_col=0, header=1, encoding='latin-1', usecols=(0,3))
print(dF)
dF.to_csv(r'C:\Users\videowall_08\Documents\Mapas\EMAS_MAXIMAS.csv')