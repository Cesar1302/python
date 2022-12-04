from asyncore import read
from os import close, remove, write
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
import pandas as pd
import numpy as np
import threading

def timer():
    while True:
        try:
            espacio='-------------'
            now=datetime.now()
            fecha=(now.strftime("%d/%m/%y %H:%M"))
            print(fecha)


            print("OH")
            print(espacio)
            urlOH='https://www.oh-iiunam.mx/geojson/datospaginadia.txt'
            fileOH = r'C:\Users\jclm1\Documents\mapas\EMAS\DATOSOH.csv'
            try:  
                r = urllib.request.urlopen(urlOH)
                f = open(fileOH,'wb')
                f.write(r.read())
                f.close()
                print('Datos de OH obtenidos')
            except:
                print("Se produjo un error al momento de descargar los datos")

            oh=open(fileOH)
            texto=oh.read()
            texto1=texto.replace(" ", ",")
            #print(texto1)
            oh1=open(fileOH,"w")
            oh1.write(texto1)
            oh.close()
            oh1.close()

            oh=pd.read_csv(fileOH, index_col=False, header=None)
            oh.to_csv(fileOH)

            oh=pd.read_csv(fileOH, index_col=0, header=0)
            texto1=oh.rename({'2': 'idEstacion'}, axis=1)
            texto2=texto1.rename({'3': 'lluvia'}, axis=1)
            #print(texto2)
            texto2.to_csv(fileOH)

            oh=pd.read_csv(fileOH, index_col=0)
            oh['fechaHora']=np.where(oh['lluvia'] !='[]', fecha, ' ', )
            #print(oh)
            oh.to_csv(fileOH)

            oh=pd.read_csv(fileOH, usecols=(3, 4, 5), index_col=0, header=0) 
            print(oh)
            oh.to_csv(fileOH)
        except:
            print("No se logro obtener datos de OH")
        time.sleep(60)
T=threading.Thread(target=timer)
T.start