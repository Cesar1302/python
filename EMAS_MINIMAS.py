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
segmn= time.strftime('%S')
print(fechasmn)
print(segmn)
urlmin = ('https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/consultaMaxMin.php?var=temperatura&valor=minimo&tipo=descarga&area=estado&idestado=9&idmunic=0&fechaInicial='+fechasmn+'%2000:00:'+segmn+'&fechaFinal='+fechasmn+'%2009:30:'+segmn)
#https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/consultaMaxMin.php?var=temperatura&valor=minimo&tipo=descarga&area=estado&idestado=9&idmunic=0&fechaInicial=2022-08-27%2000:00:05&fechaFinal=2022-08-27%2009:30:05
print(urlmin)
filemin = 'EMAS_MINIMAS.csv'
r = urllib.request.urlopen(urlmin)
f = open(filemin,'wb')
f.write(r.read())
f.close()
print('Datos de extremos minimos del SMN obtenidos')

f=  'Periodo del ' + fechasmn + ' 00:00:'+segmn+ 'al: ' + fechasmn + ' 09:30:'+segmn
#print(f)
EMAS = open(r'C:\Users\videowall_08\Documents\Mapas\EMAS_MINIMAS.csv','r')
txt=EMAS.read()
cambio0=txt.replace('"','')
cambio1=cambio0.replace('Servicio Meteorológico Nacional','')
cambio2=cambio1.replace('Valor minimo de la Variable: temperatura','')
cambio3=cambio2.replace(f,'')
#print(cambio3)
txt=open(r'C:\Users\videowall_08\Documents\Mapas\EMAS_MINIMAS.csv','w')
txt.write(cambio3)
txt.close()

dF = pd.read_csv(r'C:\Users\videowall_08\Documents\Mapas\EMAS_MINIMAS.csv', index_col=0, header=1, encoding='latin-1', usecols=(0,3))
print(dF)
dF.to_csv(r'C:\Users\videowall_08\Documents\Mapas\EMAS_MINIMAS.csv')