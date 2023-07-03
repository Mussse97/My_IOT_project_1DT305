Welcome to my internet of things project, my name is Mostafa Hussein and i have chosen to do an alarm system.
For this project we want somthing that tells us when a box/drawer has been opened by someone els other than yourself.
This project took me a bit longer than a week to complete. That said it was a lot of testing and experimenting done. With this guide it should be possible to do within a couple of days or even a day if you really spend the time.

<h1>Objective</h1>

I live with two siblings and sometimes personal drawers and boxes isnt considerd personal to them, this project is made so that i always know if somone is going thru my personal stuff.
This will give me the insite and information about if my peronal stuff stays personal.

<h1>Material</h1>

The materials needed to do this project is as listed:

 Raspberry Pi Pico WH 65kr,  link: https://www.electrokit.com/produkt/raspberry-pi-pico/

 Breadboard 840 connections 69kr, link: https://www.electrokit.com/produkt/kopplingsdack-840-anslutningar/

 USB 2.0. USB A to USB micro B 39kr, link: https://www.electrokit.com/produkt/usb-kabel-a-hane-micro-b-5p-hane-1-8m/

 14 Labcables hane/hane  49kr, link: https://www.electrokit.com/produkt/labbsladd-40-pin-30cm-hane-hane/

 Tiltsensor 29kr, link: https://www.electrokit.com/produkt/tiltsensor/

 LED-modul RGB 19kr, link: https://www.electrokit.com/produkt/led-modul-rgb/

 Pizo speaker passive 36kr, link:https://www.electrokit.com/produkt/piezohogtalare-passiv/


Total cost of everything is 306Kr which is about 25.89 Euro


<h1>Computer setup</h1>

For the computer setup free programs are used to do all the coding and addons for the pico.
We are using visual studio code which you can download here: https://code.visualstudio.com/download.

You also need node.js downloaded on your computer here: https://nodejs.org/en/download/current

To check that everything has installed correctly, you can run these commands in your terminal:

npm --version

node --version

When visual studio code is downloaded you need pymakr

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/eba11533-51d2-452a-bdbf-5d4a931c285f)

Now the you have eveything needed on the computer, next step is Firmware update

<h1>Firmware update </h1>

Download and update the board micropython firmware, this is done so that the pico understand python.

Follow these steps:

Step 1: Download the micropython firmware from this website https://micropython.org/download/rp2-pico-w/. You will get a uf2 file, be sure to download the latest one from the Releases category and not Nightly Builds.

Step 2: Connect the micro-usb end of your cable (the small side) into the Raspberry Pi Pico, be sure to firmly hold the back of the USB slot so that by pushing you will not bend it. The USB won’t have to be entered fully, it’s normal that a small gap will be left out from the slot.

Step 3: While holding the BOOTSEL key down on the board, connect the USB type A end of your cable (the big side) into your computer’s USB port. If you want to be extra safe avoid using a USB hub and prefer the ports on 
your desktop/laptop computer. You can release the BOOTSEL after connecting it to your computer.

Step 4: You will see a new drive open in your file system named RPI-RP2 which is the Raspbbery Pi Pico storage. You can copy/paste the uf2 in this storage.

Before adding code we will start with creating a folder with all the files needed. When clicking on pymakr there will be an option to create a new project.

Name the folder and when template option appears choose "empty".

Your folder layout shold look like this ![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/34463c8e-1113-43ba-ae55-84c65db63f81)

The library folder isnt being used for this project but if you deside to use other sensors that might need a library thats where the files goes.


Now you are ready to start opening up vsCode and start with some easy code to check that everything is working.

Before puting in some code you need to make sure you connect the pico and start developer mode.

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/f3cb8cd8-433f-4f34-bcb6-766d1232099f)

On the picture above we see a lightning symbol which means connecting to the pico, the sign to the right of the lightning is developer mode which means the code will update the pico everytime new code is added.

To check that the pico is connected and that developer mode is on, we can start with an easy input 

In the main.py we can start with this line: Print("testing")

Always open up the console which you can do by clikcing a box icon ![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/04cd29bb-970f-4f18-9723-671f1cc78d7b)

You should be getting reply in the console looking like this ![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/4ee4c647-4940-4df5-8b0d-b0ff1621d26c)

If you got the reply then everything is working!

<h1>Putting everything together</h1>

Here we will go thru how to connect all the sensors and where the cables needs to go
We will start with putting the pico on the breadboard and connect VBUS to the + area and ground to - area like on the picture below.


![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/ec8a0de3-2ea3-4026-b7ad-8b0539512f64)

After doing this connect the usb and make the print code line again to see that everything is working. <p>ALWAYS DISCONNECT THE USB FROM POWERSOURCE WHEN REMOVING OR ADDING SENSORS OR CABLES</p>
<h2>LED_RGB</h2>
Now for our first sensor which will be the LED_RGB, for this one four cables is needed and you will connect them like the picture below. A tip when before connecting the wires is to look at the charachters on the sensor, very often there will be markers for where the pin should be connected too, in this case with the LED there is a (-) sign which means that it needs to be connected to ground. Ground being negative marked places on the breadboard or ground pins on the pico if a breadboard is not used.

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/d68f56d7-df17-4bce-96e1-34ecde65de70)

