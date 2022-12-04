from PIL import Image
import os
import time

fecha = time.strftime("%Y-%m-%d-%H%M")

semaforo= Image.open(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_verde2.png")

chSDWVOLCAN = Image.open(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\SDW.png")


chSDWVOLCAN.paste(semaforo,(2500,700),semaforo)
chSDWVOLCAN.save(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\SDWV.png")


 
semaforo= Image.open(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_amarillo2.png")

chSDWVOLCAN = Image.open(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\SDW.png")


chSDWVOLCAN.paste(semaforo,(2500,700),semaforo)
chSDWVOLCAN.save(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\SDWA.png")

semaforo= Image.open(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_rojo2.png")



chSDWVOLCAN = Image.open(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\SDW.png")


chSDWVOLCAN.paste(semaforo,(2500,700),semaforo)
chSDWVOLCAN.save(r"C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\SDWR.png")

