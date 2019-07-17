# RFID RC522 on Raspberry Pi3 B+

### Device and tool Requirement:

**1. Raspberry Pi3 B+ or Raspberry Pi Zero W**

**2. RFID RC522 module**

**3. Pin header. Ex: RS PRO, 2.54mm Pitch, 8 Way, 1 Row, Straight Pin Header, Through Hole**

**4. Soldering tools: Soldering tin (ex:MBO 1mm Wire Lead solder, +183°C Melting Point), Soldering iron,  Desoldering pump and Soldering braid**

### STEPs about setting up necessary library and packages:

**1. `$sudo raspi-config`  Select "5 Interfacing Options" and then press "Enter"**

**2. Select "P4 SPI" and then press "Enter"**

**3. Select "Yes" and then press "Enter" to proceed.**

**4. Once the SPI interface has been successfully enabled by the raspi-config tool you should see the following text appear on the screen, “The SPI interface is enabled“.**

**5. Type the following Linux command into the terminal on your Raspberry Pi to restart your Raspberry Pi.`$sudo reboot`**

**6. Make sure that it has been enabled. Type the following Linux command into the terminal on your Raspberry Pi to see if spi_bcm2835 is listed.**`$lsmod | grep spi` 

**7. Update Pi to ensure it's running the latest version of all the software  `$sudo apt-get update`  `$sudo apt-get upgrade`**

**8. Install "python3-dev", "python-pip" and "git" packages for this guide on setting up your RFID reader.** `$sudo apt-get install python3-dev python3-pip` 

**9. Install the python library "spidev" which helps handle interactions with the SPI as we need it for Pi to interact with the RFID RC322. `$sudo pip3 install spidev` or `$sudo pip install spidev`**

**10.Install the MFRC522 library using pip as well. `$sudo pip3 install mfrc522` or `$sudo pip install mfrc522`**

### STEPs about writing with the RFID RC522:

**1.** `$mkdir ~/pi-rfid`

**2. `$cd ~/pi-rfid` then type `$sudo nano Write.py`**

**3. The content of the file"Write.py" as below:**
```
#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup() 
```

**4. `$sudo python3 Write.py`**

**5. You can look at our example output below to see what a successful run looks like.**
```
pi@raspberrypi:~/pi-rfid $ sudo python3 Write.py
New data:pimylifeup
Now place your tag to write
Written
```

**6. It shows like this.**![image](picture or gif url)
ex:![image](https://github.com/HLLINN/Pi_RC522/blob/master/Write.gif)

### STEPs about Reading with the RFID RC522:

**1.** `cd ~/pi-rfid` then type `sudo nano Read.py`

**2. The content of the file"Read.py" as below:**
```
#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()

```

**3. `$sudo python3 Read.py`**

**4. An example of what a successful output would look like is displayed below.**
```
pi@raspberrypi:~/pi-rfid $ sudo python3 Read.py
827843705425
pimylifeup
```

**5. It shows like this.**![image](picture or gif url)
ex:![image](https://github.com/HLLINN/Pi_RC522/blob/master/Read.gif)

**7. Remark and explanation:**
`reader = SimpleMFRC522()`
This line is quite important as it calls SimpleMFRC522’s creation function and then stores that
 into our reader variable as an object so we can interact with it later.
```
try:
        id, text = reader.read()
        print(id)
        print(text)
```
This next block of code is contained within a try statement, and we use this so we can catch any 
exceptions that might occur and deal with them nicely. You need to ensure that you use the ‘tabs‘ 
as shown after try: as Python is whitespace sensitive.

The second line in this block of code makes a call to our reader object, in this case, it tells the 
circuit to begin reading any RFID tag that is placed on top of the RC522 reader.


### Reference:

**1.[How to setup a Raspberry Pi RFID RC522 Chip](https://pimylifeup.com/raspberry-pi-rfid-rc522/)**
<br/>
**2.[Raspberry Pi 筆記(25)：RFID 無線射頻辨識控制 LED](https://atceiling.blogspot.com/2017/02/raspberry-pi-rfid.html)**
<br/>




