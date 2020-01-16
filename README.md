# Smart Iron Wear
___
Smart IronWear es un prototipo inteligente de un dispositivo con sensores y luces LED aplicado a un traje de aluminio ignífugo, 
que recoge información sobre el entorno y sobre el usuario para proporcionar datos del entorno de trabajo y del estado del usuario 
con el fin de aumentar la seguridad laboral en entornos de trabajo peligrosos como puede ser la industria siderúrgica. 
El prototipo lleva 3 LED (los cuales estarían  en el antebrazo del traje) conectadas a los sensores, y que se iluminan 
en caso de que el usuario corra peligro, de esta forma, se mantiene informado tanto al usuario como al resto de trabajadores del estado del propio usuario y de las condiciones del entorno de trabajo (temperatura, humedad y frecuencia cardíaca).

El objetivo de este proyecto es proporcionar seguridad. La seguridad del trabajador es lo más importante, sobre todo cuando se opera en entornos tan peligrosos como lo son los de la industria siderúrgica. Un trabajador rendirá mejor en situaciones en las que se le garantice una seguridad a tiempo completo sin tener que depender de nadie. 

### Aprovisionamiento Hardware

-RaspberryPI3 Modelo B x1

![RaspberryPI3 Modelo B](https://www.raspberrypi.org/homepage-9df4b/static/0ac033e17962a041a898d92057e60def/052d8/67d8fcc5b2796665a45f61a2e8a5bb7f10cdd3f5_raspberry-pi-3-1-1619x1080.jpg)


-Groove Base Hat x1

![Groove Base Hat ](https://media-cdn.seeedstudio.site/media/catalog/product/cache/ab187aaa5f626ad16c8031644cd2de5b/h/t/httpsstatics3.seeedstudio.comseeedfile2018-11bazaar975950_perspective.jpg)


-SD card min 8 GB


![SD card 8 ](https://m.media-amazon.com/images/I/71o2uWmUqAL._AC_UY218_ML3_.jpg)


-Groove Red Led x3

![Groove Red Led ](https://media-cdn.seeedstudio.site/media/catalog/product/cache/aa594c9fc955742a08f5aada927a2ed2/h/t/httpsstatics3.seeedstudio.comseeedfile2018-09bazaar939479_1040300054.jpg)


-Grove Temperature ad Humidity sensor x1

![Grove Temperature ad Humidity sensor](https://media-cdn.seeedstudio.site/media/catalog/product/cache/9d0ce51a71ce6a79dfa2a98d65a0f0bd/g/r/grove-temperature-humidity-sensor-dht11-preview.png)


-Grove Finger-clip Heart Rate Sensor x1

![Grove Finger Clip](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor/raw/master/img/Grove-Finger-clip_Heart_Rate_Sensor.jpg)


-Grove Flame sensor x1

![Grove flame sensor](https://raw.githubusercontent.com/SeeedDocument/Grove-Flame_Sensor/master/img/Flame_Sensor_01.jpg)


-Set de cables

![Wires](https://ae01.alicdn.com/kf/HTB1.j97LpXXXXaVXVXXq6xXFXXXk/20-30cm-Raspberry-Pi-40pcs-Dupont-Line-Cable-Male-to-Female-Jumper-Wire-for-Raspberry-Pi.jpg)


### Conexiones
- LED 1 -> Puerto Digital D5
- LED 2 -> Puerto Digital D16
- LED 3 -> Puerto Digital D18
- Sensor de Temperatura -> PWM
- Sensor de Pulso -> GND(PIN 6), POWER(PIN 2), SDA(PIN 3) y SCL(PIN 5)
- Sensor de Llama -> GND(PIN 9), POWER(PIN 4) y SCLK(PIN 40)

### Instalación
-Instalar las últimas dependencias de grove.py
~~~
curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -
~~~
-Instalar código fuente
~~~
git clone https://github.com/DanielDiazA/IotIronWearG10.git
~~~
-[Ativar Interfaz I2C](https://github.com/tidus747/Utilidades_RaspberryPi/wiki/Instalar-I2C-TOOLS-y-SMBUS)
~~~
sudo apt-get install i2c-tools
~~~
### Puesta en marcha

-En el directorio donde se haya copiado el código fuente
~~~
python3 script.py
~~~
>En caso de no tener Python ejecutar previamente
~~~
sudo apt install python3-pip
~~~




