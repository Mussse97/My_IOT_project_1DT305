Welcome to my internet of things project, my name is Mostafa Hussein (mh225qg) and i have chosen to do an alarm system.
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

 Pizo buzzer passive 36kr, link:https://www.electrokit.com/produkt/piezohogtalare-passiv/


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

<h2>Piezzo buzzer passive</h2>

This is the sensor that will emit sound, for this sensor three cables will be connected to the board. We want the connections to be with a ground, 3,3 volt and a GPIO pin. The cables will be connected as following:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/152490f3-4027-4bdb-b314-b9fc5bd67cf2)

<h2>Tiltsensor</h2>

The last sensor that needs to be connected will be the tiltsensor or tiltswitch. three more cables are needed which will be connected to the ground (Negative part of the breadboard), possitive side of the breadboard and a GPIO pin. Follow the connections shown in the picture below.

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/a083aa28-8920-43da-b8fe-95a2e7bf8007)

Now all the sensors all connected and you should have somthing looking like the picture below

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/549df1af-c0f6-478d-b375-0c7c50078d8a)

Better cable management is possible and should maby be considered if the box or drawer isnt big enough

<h1>Platform</h1>

Platform is an important step to configure because we want the data that we gather with the code to go somewhere that can be analysed  and make it more visually presentable. For this project the platform that is used is called Ubidots. Ubidots is an IoT Platform where you can prototype your iot projects to production. You can use Ubidots platform to send data to the cloud from any Internet-enabled device. You can then configure actions and alerts based on your real-time data and unlock the value of your data through visual tools. Ubidots offers a REST API that allows you to read and write data to the resources available: data sources, variables, values, events and insights. The API supports both HTTP and HTTPS and an API Key is required.

There are other platform like Adafruit that can do the same thing. I liked the layout and found it way easier to use Ubidots and thats why its used on this project.

Ubidots isn't a free platform but you are able to create an account with a 30 day free trail. The free trail will be enough time for us to do this project and use it in production for a while, if you want it longer then you might want to pay or find a free alternative.

<h1>The code</h1>

Its time to start coding! We start with the libraries used for this project because that is usually what you put in before functions. These are the libraries we import:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/00d14774-50b1-470f-a284-6290f0ac0cb6)

Next important step is to set a variable name for the different sensors from the pin that was connected, if you have followed this guide then these should be the right pins:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/b105b1ba-49ce-4950-9e3c-0af349d4dd1a)

Instead of pasting all the code in this guide i will go through the most intresting thing which is the alarm sound.

For the buzzer to emit sound we need to define som tones in a list just like this:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/aa55e167-c9b0-4a02-9ed5-9e9510b98d5e)

This is where the fun begins, there is no real right anwser here for which notes to pick. We start with creating a variable that has a couple of notes called "tones_sequence". It should look like this:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/1de19b1c-a73a-4633-89f4-7441eb57e0cb)

In "tones_sequence" we tell the buzzer which notes to emit and when to take pauses and this is done by the "sleep" line and "play_tone". "play_tone" is a def that we created here:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/cbd3c945-4bb3-4423-be7a-c5611369254c)

In this def we also tell it how loud is should be which is done witch "buzzer.duty_u16(5000)".

The code as a whole is actually very simple. Our main sensor is the tiltswitch which has two values (0 and 1). Number 1 being when its moving or sensing change in tilt and 0 when its still.

we start with a while true function where we give a name to the tiltvalue: ![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/e35ed47f-eff1-4c8d-b836-dba024176ede)

After this we put in the main if statement:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/94b62d67-411f-4a14-8d7d-506bf0ea3f6b)

So what this does is checks if the sensor is detecting any movement then the LED light blinks and the play_warning_sound is active. Now a visual warning and a sound warning active for the person that touches your box to see. This should be enough to stop someone from touching your stuff. With this you have a lot of customization options when it comes to the sound and the light. As you can se in the code we only defined three colores:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/58d2e0d8-8ec1-4b8e-b135-b5e2b96e066f)

But having more than one active so for example if you would type :![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/06ff2e1f-a3f9-4251-bf37-0908666d28ea)

Then a purple light would appear. I encourage to try out with different tones and mixing the colors to get it just how you like it.

<h1>Transmitting the data / connectivity </h1>

For the transmition of the data we are using wifi as our connectivity. Wifi isnt the best option because it will eat into the battery life, a great option is LoRaWan if you have great connection to helium or ttn (the things network). In my case i had no connection near me with ttn. Even tho i had server all around me with helium it would take a long time to connect and i made the desition in the end to go with somtihing a bit easier like wifi. LoRaWAN also requires to connect a modem to the breadborard that will make it bigger. My box didnt suppert the extra modem.

The data we want to send is the values that comes from the tiltswitch that is 1 and 2. This transmition is "triggerd" which means a change in the sensor and not somting we do manually.

Connecting to the wifi is very simple and requires you to type in the home wifi name_SSID and password. Then in a file you would call boot.py you put in the code for connectiviy. You can find this uploaded to this Github repository.

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/9ea240e4-c7fc-4ae3-85a2-5b46e2bfc5d1)

The picture above shows the code added to make this transmition work. The code above the "else" is in the if statement, we are sending the data with the number 1 which means the box was opened and we put a sleep because we dont want to send to many request. If we send to much and fast data it could result in a ban where you are not alowed to send more. For this we make it sleep for five secounds. This means that every five second it starts over and sends the new value.



<h1>Presenting the data </h1>

Now for the last part of this project, showing the data that we sent to Ubidots. We start of with creating two events:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/b5e3b03f-f277-4248-8f54-bccc4c1d6809)

Ubidots will not listen for data thats 0 or 1. For the visual part nothing fancy is needed, the only thing we want to know is if the value change and a nice switch with a color that represent if the box is in danger or not.

![Off](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/2df3100b-4bfe-478e-96fe-481108886af7)

As we can see on the picture above we are only using two widgets which is a "Guage" and a "indicator" widget. On the picture we see that the value is 0 and the indicator is green with a message that says "off".

This is a good visual representation of the box not being opened.

![On](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/008abb8e-9db2-498a-a9db-90ca141fb49f)

With the other event being 1, meaning somone is opening the box. We see the guage turning to 1 and the indicator turning the color red with the message being "ON". Now we know that the box has been opened.

When looking at the data more indepth which we can do if we enter "explore data" in ubidots. We are greeted with a layout like this: 

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/bd7c4ff8-c1cc-472e-bb35-084aca170c05)

Here we can se what time the sensor sent data and what value it gave. The times in this picture is a bit inconsistent because the pico was unplugged multiple times when experimenting with other stuff. If connected and not removed from power you should have a consistent update every 5 seconds.

<h1>Finalizing the design </h1>

Overall this project was a lot of fun to make and experiment with. The goal i had with this was achieved and im very happy with the result. Here are some pictures of the sensor in its different modes.

Not active:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/15c549b6-7db0-4dc1-97ff-e5d7baa382f6)

Active:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/24636eee-0f99-4750-8868-a4357ce42626)

This is how i would attach it to my box at home, i would need to buy somthing to hold it to the roof of the box:


https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/d2ba5194-307e-4bcd-af03-2ede998da6d7

This is not the best way of showinbg the alarm, i didn't have a good enough way of securing the alarm on the top of the roof without it falling down. This video is only when the roof is up.
<h2>What could have been added</h2>
I had some really interesting ideas to add but came up with them last second and was a bit hard to do. The thought was that it might get a bit annoying if the alarm goes off even if its me that openes it. The plan was to input code so that it would be able to differentiate me from others. My first idea was that it would check if my phone was connected to the home wifi and if i was mening om home, the alarm wouldnt go off. If om not connected then somone els would be opening it. This didnt work because i would need the mac-adress and i couldnt make the pico access that information which you could find on yout router website.

the other plan was to connect to bluetooth and apply the same idea but that wasnt possible and later found out i could do it but i would need to have a blutooth modem. I think that this addition to the project would make it a lot better and is 100% somthing im going to add in the near future. 



