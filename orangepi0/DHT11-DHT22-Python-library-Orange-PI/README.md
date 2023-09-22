DHT22 Python library
This simple class can be used for reading temperature and humidity values from DHT22 sensor on Orange PI.

Fork with some patches from
https://forum.armbian.com/topic/5718-need-help-with-dht11-temp-sensor-and-python-code/
+ Home made to ensure read is available even if there is not exactly the expected data lenght AM2301 usage
+ Usage with Python3
+ Usage with pyA20 for OPi Zero https://github.com/nvl1109/orangepi_zero_gpio

## My Case of usage

* Used with a Orange Pi Zero H2+
* Used with a AM2301 setup as DHT22
* Used with a DHT11
* Used within a display SSD 1306 with [https://github.com/jingl3s/OrangePiZero_OLED_Dht_display](https://github.com/jingl3s/OrangePiZero_OLED_Dht_display)
## Usage

Example:
```python
from pyA20.gpio import gpio
from pyA20.gpio import port
 
import dht
import time
import datetime
 
# initialize GPIO
PIN2 = port.PA6
gpio.init()
 
# read data using pin
instance = dht.DHT(pin=PIN2)
 
while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %.2f C" % result.temperature)
        print("Humidity: %.2f %%" % result.humidity)
 
    time.sleep(1)
```    
Please see tutorial:
http://www.piprojects.xyz/temperature-sensor-orange-pi-python-code/


Source project
https://github.com/ionutpi/DHT22-Python-library-Orange-PI