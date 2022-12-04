# Antes de poder quitar el fondo de una imagen, debemos asegurarnos de que esta bien trabajada ña imagen, para eso se le da formarto y se ajusta el tamaño



convert "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_amarillo.png" -resize 800x800 -quality 100 "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_amarillo0.png"

convert "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_amarillo0.png" -fuzz 10% -transparent white "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_amarillo2.png"  


convert "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_verde.png" -resize 500x500 -quality 100 "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_verde0.png"

convert "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_verde0.png" -fuzz 10% -transparent white "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_verde2.png"  


convert "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_rojo.png" -resize 500x400 -quality 100 "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_rojo0.png"

convert "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_rojo0.png" -fuzz 10% -transparent white "C:\Users\jclm1\Documents\Lanot\imagenes\POPOCATEPETL\IR\semaforo_rojo2.png"  

