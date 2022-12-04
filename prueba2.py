# Importamos las librerías necesarias
import os
from pickle import FALSE, NONE
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
import pandas as pd
import numpy as np
import seaborn as sb
from os import remove

espacio='-------------'
now = datetime.now()

yesterday=now-timedelta(days=1)
print(yesterday)
hoy0=datetime.strftime(now,'%d').lstrip('0')
meshoy0=datetime.strftime(now,'%m')
añohoy0=datetime.strftime(now,'%y')
fecha_hoy0= hoy0 +"/"+ meshoy0 +"/"+ añohoy0
print("la fecha de hoy con un digito es (hoy0) " + fecha_hoy0)

ayer0=datetime.strftime(yesterday,'%d').lstrip('0')
mesayer0=datetime.strftime(yesterday,'%m')
añoayer0=datetime.strftime(yesterday,'%y')
fecha_ayer0= ayer0 +"/"+ mesayer0 +"/"+ añoayer0
print("la fecha de ayer con un digito es (ayer0) " + fecha_ayer0)


hoy1=datetime.strftime(now,'%d')
meshoy1=datetime.strftime(now,'%m')
añohoy1=datetime.strftime(now,'%y')
fecha_hoy1= hoy1 +"/"+ meshoy1 +"/"+ añohoy1
fecha_hoyc= "," + hoy1 +"/"+ meshoy1 +"/"+ añohoy1
print("la fecha de hoy con dos digitos es " + fecha_hoy1)

ayer1=datetime.strftime(yesterday,'%d')
mesayer1=datetime.strftime(yesterday,'%m')
añoayer1=datetime.strftime(yesterday,'%y')
fecha_ayer1= ayer1 +"/"+ mesayer1 +"/"+ añoayer1
fecha_ayerc=  "," + ayer1 +"/"+ mesayer1 +"/"+ añoayer1
print("la fecha de hoy con dos digitos es " + fecha_ayer1)

espacio='-------------'

print("DIRECTORIOS Y LINKS")

dirtxtFERS=r'C:\Users\jclm1\Downloads\FERS.txt'
dircsvFERS=r'C:\Users\jclm1\Documents\mapas\EMAS\FERS.csv'
urlFERS = 'http://189.254.33.151/stn/azcapotzalco/downld02.txt'

dirtxtSURS=r'C:\Users\jclm1\Downloads\SURS.txt'
dircsvSURS=r'C:\Users\jclm1\Documents\mapas\EMAS\SURS.csv'
urlSURS = 'http://189.254.33.151/stn/coyoacan/downld02.txt'

dirtxtSTFS=r'C:\Users\jclm1\Downloads\STFS.txt'
dircsvSTFS=r'C:\Users\jclm1\Documents\mapas\EMAS\STFS.csv'
urlSTFS = 'http://189.254.33.151/stn/cuajimalpa/downld02.txt'

dirtxtSGIRPC=r'C:\Users\jclm1\Downloads\SGIRPC.txt'
dircsvSGIRPC=r'C:\Users\jclm1\Documents\mapas\EMAS\SGIRPC.csv'
urlSGIRPC = 'http://189.254.33.151/stn/juarez/downld02.txt'

dirtxtCUAUS=r'C:\Users\jclm1\Downloads\CUAUS.txt'
dircsvCUAUS=r'C:\Users\jclm1\Documents\mapas\EMAS\CUAUS.csv'
urlCUAUS = 'http://189.254.33.151/stn/cuautepec/downld02.txt'

dirtxtAGOS=r'C:\Users\jclm1\Downloads\AGOS.txt'
dircsvAGOS=r'C:\Users\jclm1\Documents\mapas\EMAS\AGOS.csv'
urlAGOS = 'http://189.254.33.151/stn/iztacalco/downld02.txt'

dirtxtLOMS=r'C:\Users\jclm1\Downloads\LOMS.txt'
dircsvLOMS=r'C:\Users\jclm1\Documents\mapas\EMAS\LOMS.csv'
urlLOMS = 'http://189.254.33.151/stn/iztapa1/downld02.txt'

dirtxtLEGS=r'C:\Users\jclm1\Downloads\LEGS.txt'
dircsvLEGS=r'C:\Users\jclm1\Documents\mapas\EMAS\LEGS.csv'
urlLEGS = 'http://189.254.33.151/stn/miguelhidalgo/downld02.txt'

dirtxtMPAS=r'C:\Users\jclm1\Downloads\MPAS.txt'
dircsvMPAS=r'C:\Users\jclm1\Documents\mapas\EMAS\MPAS.csv'
urlMPAS = 'http://189.254.33.151/stn/milpaalta/downld02.txt'

dirtxtTPJS=r'C:\Users\jclm1\Downloads\TPJS.txt'
dircsvTPJS=r'C:\Users\jclm1\Documents\mapas\EMAS\TPJS.csv'
urlTPJS = 'http://189.254.33.151/stn/cuautepec/downld02.txt'

dirtxtTLHS=r'C:\Users\jclm1\Downloads\TLHS.txt'
dircsvTLHS=r'C:\Users\jclm1\Documents\mapas\EMAS\TLHS.csv'
urlTLHS = 'http://189.254.33.151/stn/topilejo/downld02.txt'

print('FERS')
try:
    print(espacio)
    file1 = dirtxtFERS
    r = urllib.request.urlopen(urlFERS)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación FERS obtenidos')

    try:
        with open(dirtxtFERS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtFERS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtFERS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtFERS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    FERS=open(dirtxtFERS)
    texto0=FERS.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    FERS1=open(dirtxtFERS,"w")
    FERS1.write(texto7)
    FERS1.close()

    FERS=open(dirtxtFERS)
    texto=FERS.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    FERS1=open(dirtxtFERS,"w")
    FERS1.write(texto149)
    FERS1.close()
    FERS.close()

    FERS=open(dirtxtFERS)
    texto0=FERS.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    FERS1=open(dircsvFERS,"w")
    FERS1.write(texto2)
    #print(texto2)
    FERS1.close()
    FERS.close()
 
    FERS=pd.read_csv(dircsvFERS, usecols=(1,2,3,6,7,8,9,11,12,16,17), index_col=0, header=0)
    #print(FERS)
    FERS.to_csv(dircsvFERS)
   

    FERS=open(dircsvFERS)
    nombrescol=FERS.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")

    FERS1=open(dircsvFERS,"w")
    FERS1.write(texto9)
    FERS1.close()
    FERS.close()

    FERS=open(dircsvFERS)
    texto=FERS.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    FERS1=open(dircsvFERS,"w")
    FERS1.write(texto12)
    FERS1.close()
    FERS.close()

    FERS=open(dircsvFERS)
    texto=FERS.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    FERS1=open(dircsvFERS,"w")
    FERS1.write(texto4)
    FERS1.close()
    FERS.close()
       
    FERS=pd.read_csv(dircsvFERS, index_col=0, header=0)
    #print(FERS)
    FERS['fechaHora']=FERS['Fecha'].map(str)  + ' ' + FERS['Time'].map(str)
    FERS
    #print(FERS)
    FERS.to_csv(dircsvFERS)


    DF=pd.read_csv(dircsvFERS, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'FERS', ' ', )
    #print(DF)
    DF.to_csv(dircsvFERS)

    FERS=pd.read_csv(dircsvFERS, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(FERS)
    FERS.to_csv(dircsvFERS)


    try:
        FERS=pd.read_csv(dircsvFERS, index_col=0)
        filter= (FERS['fechaHora'] >= fecha_ayer1) & (FERS['fechaHora'] > fecha_ayer1)
        filtrado=FERS.loc[filter]
        #print(filtrado)
        filtrado.to_csv(dircsvFERS)
        print("Filtrado")
    except:
        print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación FERS listos')
except:
     print("No se logro obtener datos de la estación FERS")
     remove(dircsvFERS)


print('SURS')
try:
    print(espacio)
    file1 = dirtxtSURS
    r = urllib.request.urlopen(urlSURS)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación SURS obtenidos')

    try:
        with open(dirtxtSURS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtSURS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtSURS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtSURS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    SURS=open(dirtxtSURS)
    texto0=SURS.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    SURS1=open(dirtxtSURS,"w")
    SURS1.write(texto7)
    SURS1.close()

    SURS=open(dirtxtSURS)
    texto=SURS.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    SURS1=open(dirtxtSURS,"w")
    SURS1.write(texto149)
    SURS1.close()
    SURS.close()

    SURS=open(dirtxtSURS)
    texto0=SURS.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    SURS1=open(dircsvSURS,"w")
    SURS1.write(texto2)
    #print(texto2)
    SURS1.close()
    SURS.close()
 
    SURS=pd.read_csv(dircsvSURS, usecols=(1,2,3,6,7,8,9,11,12,16,17), index_col=0, header=0)
    #print(SURS)
    SURS.to_csv(dircsvSURS)
   

    SURS=open(dircsvSURS)
    nombrescol=SURS.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")

    SURS1=open(dircsvSURS,"w")
    SURS1.write(texto9)
    SURS1.close()
    SURS.close()

    SURS=open(dircsvSURS)
    texto=SURS.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    SURS1=open(dircsvSURS,"w")
    SURS1.write(texto12)
    SURS1.close()
    SURS.close()

    SURS=open(dircsvSURS)
    texto=SURS.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    SURS1=open(dircsvSURS,"w")
    SURS1.write(texto4)
    SURS1.close()
    SURS.close()
       
    SURS=pd.read_csv(dircsvSURS, index_col=0, header=0)
    #print(SURS)
    SURS['fechaHora']=SURS['Fecha'].map(str)  + ' ' + SURS['Time'].map(str)
    SURS
    #print(SURS)
    SURS.to_csv(dircsvSURS)


    DF=pd.read_csv(dircsvSURS, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'SURS', ' ', )
    #print(DF)
    DF.to_csv(dircsvSURS)

    SURS=pd.read_csv(dircsvSURS, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(SURS)
    SURS.to_csv(dircsvSURS)


    try:
        SURS=pd.read_csv(dircsvSURS, index_col=0)
        filter= (SURS['fechaHora'] >= fecha_ayer1) & (SURS['fechaHora'] > fecha_ayer1)
        filtrado=SURS.loc[filter]
        #print(filtrado)
        filtrado.to_csv(dircsvSURS)
        print("Filtrado")
    except:
        print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación SURS listos')
except:
     print("No se logro obtener datos de la estación SURS")
     remove(dircsvSURS)


print('SGIRPC')
try:
    print(espacio)
    file1 = dirtxtSGIRPC
    r = urllib.request.urlopen(urlSGIRPC)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación SGIRPC obtenidos')

    try:
        with open(dirtxtSGIRPC, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtSGIRPC, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtSGIRPC, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtSGIRPC, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    SGIRPC=open(dirtxtSGIRPC)
    texto0=SGIRPC.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    SGIRPC1=open(dirtxtSGIRPC,"w")
    SGIRPC1.write(texto7)
    SGIRPC1.close()

    SGIRPC=open(dirtxtSGIRPC)
    texto=SGIRPC.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    SGIRPC1=open(dirtxtSGIRPC,"w")
    SGIRPC1.write(texto149)
    SGIRPC1.close()
    SGIRPC.close()

    SGIRPC=open(dirtxtSGIRPC)
    texto0=SGIRPC.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    SGIRPC1=open(dircsvSGIRPC,"w")
    SGIRPC1.write(texto2)
    #print(texto2)
    SGIRPC1.close()
    SGIRPC.close()
 
    SGIRPC=pd.read_csv(dircsvSGIRPC, usecols=(1,2,3,6,7,8,9,11,12,16,17), index_col=0, header=0)
    #print(SGIRPC)
    SGIRPC.to_csv(dircsvSGIRPC)
   

    SGIRPC=open(dircsvSGIRPC)
    nombrescol=SGIRPC.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")

    SGIRPC1=open(dircsvSGIRPC,"w")
    SGIRPC1.write(texto9)
    SGIRPC1.close()
    SGIRPC.close()

    SGIRPC=open(dircsvSGIRPC)
    texto=SGIRPC.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    SGIRPC1=open(dircsvSGIRPC,"w")
    SGIRPC1.write(texto12)
    SGIRPC1.close()
    SGIRPC.close()

    SGIRPC=open(dircsvSGIRPC)
    texto=SGIRPC.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    SGIRPC1=open(dircsvSGIRPC,"w")
    SGIRPC1.write(texto4)
    SGIRPC1.close()
    SGIRPC.close()
       
    SGIRPC=pd.read_csv(dircsvSGIRPC, index_col=0, header=0)
    #print(SGIRPC)
    SGIRPC['fechaHora']=SGIRPC['Fecha'].map(str)  + ' ' + SGIRPC['Time'].map(str)
    SGIRPC
    #print(SGIRPC)
    SGIRPC.to_csv(dircsvSGIRPC)


    DF=pd.read_csv(dircsvSGIRPC, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'SGIRPC', ' ', )
    #print(DF)
    DF.to_csv(dircsvSGIRPC)

    SGIRPC=pd.read_csv(dircsvSGIRPC, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(SGIRPC)
    SGIRPC.to_csv(dircsvSGIRPC)


    try:
        SGIRPC=pd.read_csv(dircsvSGIRPC, index_col=0)
        filter= (SGIRPC['fechaHora'] >= fecha_ayer1) & (SGIRPC['fechaHora'] > fecha_ayer1)
        filtrado=SGIRPC.loc[filter]
        #print(filtrado)
        filtrado.to_csv(dircsvSGIRPC)
        print("Filtrado")
    except:
        print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación SGIRPC listos')
except:
     print("No se logro obtener datos de la estación SGIRPC")
     remove(dircsvSGIRPC)


print('CUAUS')
try:
    print(espacio)
    file1 = dirtxtCUAUS
    r = urllib.request.urlopen(urlCUAUS)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación CUAUS obtenidos')

    try:
        with open(dirtxtCUAUS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtCUAUS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtCUAUS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtCUAUS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    CUAUS=open(dirtxtCUAUS)
    texto0=CUAUS.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    CUAUS1=open(dirtxtCUAUS,"w")
    CUAUS1.write(texto7)
    CUAUS1.close()

    CUAUS=open(dirtxtCUAUS)
    texto=CUAUS.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    CUAUS1=open(dirtxtCUAUS,"w")
    CUAUS1.write(texto149)
    CUAUS1.close()
    CUAUS.close()

    CUAUS=open(dirtxtCUAUS)
    texto0=CUAUS.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    CUAUS1=open(dircsvCUAUS,"w")
    CUAUS1.write(texto2)
    #print(texto2)
    CUAUS1.close()
    CUAUS.close()
 
    CUAUS=pd.read_csv(dircsvCUAUS, usecols=(1,2,3,6,7,8,9,11,12,16,17), index_col=0, header=0)
    #print(CUAUS)
    CUAUS.to_csv(dircsvCUAUS)
   

    CUAUS=open(dircsvCUAUS)
    nombrescol=CUAUS.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")

    CUAUS1=open(dircsvCUAUS,"w")
    CUAUS1.write(texto9)
    CUAUS1.close()
    CUAUS.close()

    CUAUS=open(dircsvCUAUS)
    texto=CUAUS.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    CUAUS1=open(dircsvCUAUS,"w")
    CUAUS1.write(texto12)
    CUAUS1.close()
    CUAUS.close()

    CUAUS=open(dircsvCUAUS)
    texto=CUAUS.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    CUAUS1=open(dircsvCUAUS,"w")
    CUAUS1.write(texto4)
    CUAUS1.close()
    CUAUS.close()
       
    CUAUS=pd.read_csv(dircsvCUAUS, index_col=0, header=0)
    #print(CUAUS)
    CUAUS['fechaHora']=CUAUS['Fecha'].map(str)  + ' ' + CUAUS['Time'].map(str)
    CUAUS
    #print(CUAUS)
    CUAUS.to_csv(dircsvCUAUS)


    DF=pd.read_csv(dircsvCUAUS, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'CUAUS', ' ', )
    #print(DF)
    DF.to_csv(dircsvCUAUS)

    CUAUS=pd.read_csv(dircsvCUAUS, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(CUAUS)
    CUAUS.to_csv(dircsvCUAUS)


    try:
        CUAUS=pd.read_csv(dircsvCUAUS, index_col=0)
        filter= (CUAUS['fechaHora'] >= fecha_ayer1) & (CUAUS['fechaHora'] > fecha_ayer1)
        filtrado=CUAUS.loc[filter]
        #print(filtrado)
        filtrado.to_csv(dircsvCUAUS)
        print("Filtrado")
    except:
        print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación CUAUS listos')
except:
     print("No se logro obtener datos de la estación CUAUS")
     remove(dircsvCUAUS)


print('AGOS')
try:
    print(espacio)
    file1 = dirtxtAGOS
    r = urllib.request.urlopen(urlAGOS)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación AGOS obtenidos')

    try:
        with open(dirtxtAGOS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtAGOS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtAGOS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtAGOS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    AGOS=open(dirtxtAGOS)
    texto0=AGOS.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    AGOS1=open(dirtxtAGOS,"w")
    AGOS1.write(texto7)
    AGOS1.close()

    AGOS=open(dirtxtAGOS)
    texto=AGOS.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    AGOS1=open(dirtxtAGOS,"w")
    AGOS1.write(texto149)
    AGOS1.close()
    AGOS.close()

    AGOS=open(dirtxtAGOS)
    texto0=AGOS.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    AGOS1=open(dircsvAGOS,"w")
    AGOS1.write(texto2)
    #print(texto2)
    AGOS1.close()
    AGOS.close()
 
    AGOS=pd.read_csv(dircsvAGOS, usecols=(1,2,3,6,7,8,9,11,12,16,17), index_col=0, header=0)
    #print(AGOS)
    AGOS.to_csv(dircsvAGOS)
   

    AGOS=open(dircsvAGOS)
    nombrescol=AGOS.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")

    AGOS1=open(dircsvAGOS,"w")
    AGOS1.write(texto9)
    AGOS1.close()
    AGOS.close()

    AGOS=open(dircsvAGOS)
    texto=AGOS.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    AGOS1=open(dircsvAGOS,"w")
    AGOS1.write(texto12)
    AGOS1.close()
    AGOS.close()

    AGOS=open(dircsvAGOS)
    texto=AGOS.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    AGOS1=open(dircsvAGOS,"w")
    AGOS1.write(texto4)
    AGOS1.close()
    AGOS.close()
       
    AGOS=pd.read_csv(dircsvAGOS, index_col=0, header=0)
    #print(AGOS)
    AGOS['fechaHora']=AGOS['Fecha'].map(str)  + ' ' + AGOS['Time'].map(str)
    AGOS
    #print(AGOS)
    AGOS.to_csv(dircsvAGOS)


    DF=pd.read_csv(dircsvAGOS, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'AGOS', ' ', )
    #print(DF)
    DF.to_csv(dircsvAGOS)

    AGOS=pd.read_csv(dircsvAGOS, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(AGOS)
    AGOS.to_csv(dircsvAGOS)


    try:
        AGOS=pd.read_csv(dircsvAGOS, index_col=0)
        filter= (AGOS['fechaHora'] >= fecha_ayer1) & (AGOS['fechaHora'] > fecha_ayer1)
        filtrado=AGOS.loc[filter]
        #print(filtrado)
        filtrado.to_csv(dircsvAGOS)
        print("Filtrado")
    except:
        print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación AGOS listos')
except:
     print("No se logro obtener datos de la estación AGOS")
     remove(dircsvAGOS)




print('LEGS')
try:
    print(espacio)
    file1 = dirtxtLEGS
    r = urllib.request.urlopen(urlLEGS)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación LEGS obtenidos')

    try:
        with open(dirtxtLEGS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtLEGS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtLEGS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtLEGS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    LEGS=open(dirtxtLEGS)
    texto0=LEGS.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    LEGS1=open(dirtxtLEGS,"w")
    LEGS1.write(texto7)
    LEGS1.close()

    LEGS=open(dirtxtLEGS)
    texto=LEGS.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    LEGS1=open(dirtxtLEGS,"w")
    LEGS1.write(texto149)
    LEGS1.close()
    LEGS.close()

    LEGS=open(dirtxtLEGS)
    texto0=LEGS.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    LEGS1=open(dircsvLEGS,"w")
    LEGS1.write(texto2)
    #print(texto2)
    LEGS1.close()
    LEGS.close()
 
    LEGS=pd.read_csv(dircsvLEGS, usecols=(1,2,3,6,7,8,9,11,12,16,17), index_col=0, header=0)
    #print(LEGS)
    LEGS.to_csv(dircsvLEGS)
   

    LEGS=open(dircsvLEGS)
    nombrescol=LEGS.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")

    LEGS1=open(dircsvLEGS,"w")
    LEGS1.write(texto9)
    LEGS1.close()
    LEGS.close()

    LEGS=open(dircsvLEGS)
    texto=LEGS.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    LEGS1=open(dircsvLEGS,"w")
    LEGS1.write(texto12)
    LEGS1.close()
    LEGS.close()

    LEGS=open(dircsvLEGS)
    texto=LEGS.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    LEGS1=open(dircsvLEGS,"w")
    LEGS1.write(texto4)
    LEGS1.close()
    LEGS.close()
       
    LEGS=pd.read_csv(dircsvLEGS, index_col=0, header=0)
    #print(LEGS)
    LEGS['fechaHora']=LEGS['Fecha'].map(str)  + ' ' + LEGS['Time'].map(str)
    LEGS
    #print(LEGS)
    LEGS.to_csv(dircsvLEGS)


    DF=pd.read_csv(dircsvLEGS, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'LEGS', ' ', )
    #print(DF)
    DF.to_csv(dircsvLEGS)

    LEGS=pd.read_csv(dircsvLEGS, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(LEGS)
    LEGS.to_csv(dircsvLEGS)


    try:
        LEGS=pd.read_csv(dircsvLEGS, index_col=0)
        filter= (LEGS['fechaHora'] >= fecha_ayer1) & (LEGS['fechaHora'] > fecha_ayer1)
        filtrado=LEGS.loc[filter]
        #print(filtrado)
        filtrado.to_csv(dircsvLEGS)
        print("Filtrado")
    except:
        print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación LEGS listos')
except:
     print("No se logro obtener datos de la estación LEGS")
     remove(dircsvLEGS)


print('MPAS')
try:
    print(espacio)
    file1 = dirtxtMPAS
    r = urllib.request.urlopen(urlMPAS)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación MPAS obtenidos')

    try:
        with open(dirtxtMPAS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtMPAS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtMPAS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtMPAS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    MPAS=open(dirtxtMPAS)
    texto0=MPAS.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    MPAS1=open(dirtxtMPAS,"w")
    MPAS1.write(texto7)
    MPAS1.close()

    MPAS=open(dirtxtMPAS)
    texto=MPAS.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    MPAS1=open(dirtxtMPAS,"w")
    MPAS1.write(texto149)
    MPAS1.close()
    MPAS.close()

    MPAS=open(dirtxtMPAS)
    texto0=MPAS.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    MPAS1=open(dircsvMPAS,"w")
    MPAS1.write(texto2)
    #print(texto2)
    MPAS1.close()
    MPAS.close()
 
    MPAS=pd.read_csv(dircsvMPAS, usecols=(1,2,3,6,7,8,9,11,12,16,17), index_col=0, header=0)
    #print(MPAS)
    MPAS.to_csv(dircsvMPAS)
   

    MPAS=open(dircsvMPAS)
    nombrescol=MPAS.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")

    MPAS1=open(dircsvMPAS,"w")
    MPAS1.write(texto9)
    MPAS1.close()
    MPAS.close()

    MPAS=open(dircsvMPAS)
    texto=MPAS.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    MPAS1=open(dircsvMPAS,"w")
    MPAS1.write(texto12)
    MPAS1.close()
    MPAS.close()

    MPAS=open(dircsvMPAS)
    texto=MPAS.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    MPAS1=open(dircsvMPAS,"w")
    MPAS1.write(texto4)
    MPAS1.close()
    MPAS.close()
       
    MPAS=pd.read_csv(dircsvMPAS, index_col=0, header=0)
    #print(MPAS)
    MPAS['fechaHora']=MPAS['Fecha'].map(str)  + ' ' + MPAS['Time'].map(str)
    MPAS
    #print(MPAS)
    MPAS.to_csv(dircsvMPAS)


    DF=pd.read_csv(dircsvMPAS, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'MPAS', ' ', )
    #print(DF)
    DF.to_csv(dircsvMPAS)

    MPAS=pd.read_csv(dircsvMPAS, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(MPAS)
    MPAS.to_csv(dircsvMPAS)


    try:
        MPAS=pd.read_csv(dircsvMPAS, index_col=0)
        filter= (MPAS['fechaHora'] >= fecha_ayer1) & (MPAS['fechaHora'] > fecha_ayer1)
        filtrado=MPAS.loc[filter]
        #print(filtrado)
        filtrado.to_csv(dircsvMPAS)
        print("Filtrado")
    except:
        print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación MPAS listos')
except:
     print("No se logro obtener datos de la estación MPAS")
     remove(dircsvMPAS)

print('TPJS')
try:
    print(espacio)
    file1 = dirtxtTPJS
    r = urllib.request.urlopen(urlTPJS)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación TPJS obtenidos')

    try:
        with open(dirtxtTPJS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtTPJS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtTPJS, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtTPJS, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    TPJS=open(dirtxtTPJS)
    texto0=TPJS.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    TPJS1=open(dirtxtTPJS,"w")
    TPJS1.write(texto7)
    TPJS1.close()

    TPJS=open(dirtxtTPJS)
    texto=TPJS.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    TPJS1=open(dirtxtTPJS,"w")
    TPJS1.write(texto149)
    TPJS1.close()
    TPJS.close()

    TPJS=open(dirtxtTPJS)
    texto0=TPJS.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    TPJS1=open(dircsvTPJS,"w")
    TPJS1.write(texto2)
    #print(texto2)
    TPJS1.close()
    TPJS.close()
 
    TPJS=pd.read_csv(dircsvTPJS, usecols=(1,2,3,6,7,8,9,11,12,16,17), index_col=0, header=0)
    #print(TPJS)
    TPJS.to_csv(dircsvTPJS)
   

    TPJS=open(dircsvTPJS)
    nombrescol=TPJS.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")

    TPJS1=open(dircsvTPJS,"w")
    TPJS1.write(texto9)
    TPJS1.close()
    TPJS.close()

    TPJS=open(dircsvTPJS)
    texto=TPJS.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    TPJS1=open(dircsvTPJS,"w")
    TPJS1.write(texto12)
    TPJS1.close()
    TPJS.close()

    TPJS=open(dircsvTPJS)
    texto=TPJS.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    TPJS1=open(dircsvTPJS,"w")
    TPJS1.write(texto4)
    TPJS1.close()
    TPJS.close()
       
    TPJS=pd.read_csv(dircsvTPJS, index_col=0, header=0)
    #print(TPJS)
    TPJS['fechaHora']=TPJS['Fecha'].map(str)  + ' ' + TPJS['Time'].map(str)
    TPJS
    #print(TPJS)
    TPJS.to_csv(dircsvTPJS)


    DF=pd.read_csv(dircsvTPJS, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'TPJS', ' ', )
    #print(DF)
    DF.to_csv(dircsvTPJS)

    TPJS=pd.read_csv(dircsvTPJS, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(TPJS)
    TPJS.to_csv(dircsvTPJS)


    try:
        TPJS=pd.read_csv(dircsvTPJS, index_col=0)
        filter= (TPJS['fechaHora'] >= fecha_ayer1) & (TPJS['fechaHora'] > fecha_ayer1)
        filtrado=TPJS.loc[filter]
        #print(filtrado)
        filtrado.to_csv(dircsvTPJS)
        print("Filtrado")
    except:
        print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación TPJS listos')
except:
     print("No se logro obtener datos de la estación TPJS")
     remove(dircsvTPJS)

