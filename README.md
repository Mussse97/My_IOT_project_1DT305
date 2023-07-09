<h1>Alarm system with piezo buzzer</h1>
Welcome to my Internet of Things (IoT) project! My name is Mostafa Hussein (mh225qg), and I have chosen to build an alarm system. The objective of this project is to create a device that notifies me when a box or drawer has been opened by someone other than myself. It took me a bit longer than a week to complete this project due to extensive testing and experimentation. However, with this guide, you should be able to complete it within a couple of days or even a day if you dedicate enough time.

<h1>Objective</h1>

I live with two siblings, and sometimes they consider my personal drawers and boxes as accessible to them. This project is designed to ensure that I always know if someone is going through my personal belongings. It provides insight and information about the security of my personal stuff.

<h1>Material</h1>

The following materials are needed for this project:

 Raspberry Pi Pico WH 109r,  link: https://www.electrokit.com/produkt/raspberry-pi-pico-wh/

 Breadboard 840 connections 69kr, link: https://www.electrokit.com/produkt/kopplingsdack-840-anslutningar/

 USB 2.0. USB A to USB micro B 39kr, link: https://www.electrokit.com/produkt/usb-kabel-a-hane-micro-b-5p-hane-1-8m/

 14 Jumper cable Male/Male  49kr, link: https://www.electrokit.com/produkt/labbsladd-40-pin-30cm-hane-hane/

 Tiltsensor 29kr, link: https://www.electrokit.com/produkt/tiltsensor/

 LED-modul RGB 19kr, link: https://www.electrokit.com/produkt/led-modul-rgb/

 Piezo buzzer passive 36kr, link:https://www.electrokit.com/produkt/piezohogtalare-passiv/


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

In this section, we will go through connecting all the sensors and where the cables need to be placed. We will start by placing the Pico on the breadboard and connecting VBUS to the "+" area and ground to the "-" area, as shown in the image.


![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/ec8a0de3-2ea3-4026-b7ad-8b0539512f64)

After doing this connect the usb and make the print code line again to see that everything is working. <b>Note: Always disconnect the USB from the power source when adding or removing sensors or cables.</b>
<h2>LED_RGB</h2>
Now let's connect our first object, the LED_RGB. This sensor requires four cables to be connected as shown in the image. Before connecting the wires, check the characters on the sensor; they often indicate where the pins should be connected. In the case of the LED, there is a "-" sign, which means it needs to be connected to the ground. If you're not using a breadboard, connect it to the negative-marked areas on the board or the ground pins on the Pico.

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/d68f56d7-df17-4bce-96e1-34ecde65de70)

<h2>Piezzo buzzer passive</h2>

This sensor emits sound. To connect the piezo buzzer, three cables need to be connected to the board. We want the connections to be as follows: ground, 3.3 volts, and a GPIO pin. Connect the cables as shown in the image.

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/152490f3-4027-4bdb-b314-b9fc5bd67cf2)

<h2>Tiltsensor</h2>

The last sensor to be connected is the tiltsensor or tilt switch. It requires three more cables connected to the ground (negative part of the breadboard), positive side of the breadboard, and a GPIO pin. Follow the connections shown in the image.

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/a083aa28-8920-43da-b8fe-95a2e7bf8007)

Now all the sensors all connected and you should have somthing looking like the picture below

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/549df1af-c0f6-478d-b375-0c7c50078d8a)

Better cable management is possible and should maby be considered if the box or drawer isnt big enough

<h1>Platform</h1>

Configuring the platform is an important step because we want the data we gather with the code to be analyzed and presented visually. For this project, we will be using a platform called Ubidots. Ubidots is an IoT platform that allows you to prototype and produce your IoT projects. You can use Ubidots to send data to the cloudfrom any internet-enabled device and configure actions and alerts based on real-time data. It offers a REST API for reading and writing data to resources such as data sources, variables, values, events, and insights. The API supports both HTTP and HTTPS, and an API Key is required.

While there are other platforms like Adafruit that can achieve similar results, I found Ubidots to have a more user-friendly layout and ease of use, which is why I chose it for this project.

Ubidots is not a free platform, but you can create an account with a 30-day free trial. This trial period should be sufficient for us to complete this project and use it in production for a while. If you need more time, you may consider paying for a subscription or exploring free alternatives.

<h1>The code</h1>

Now let's dive into coding! We will start with the libraries used for this project, as they are usually placed before the functions. The following libraries are imported:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/00d14774-50b1-470f-a284-6290f0ac0cb6)

The next important step is to assign variable names to the different sensors based on the connected pins. If you have followed this guide, the correct pins should be as follows:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/b105b1ba-49ce-4950-9e3c-0af349d4dd1a)

Instead of pasting all the code into this guide, I will focus on the most interesting aspect, which is the alarm sound.

To make the buzzer emit sound, we need to define some tones in a list. Here's an example:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/aa55e167-c9b0-4a02-9ed5-9e9510b98d5e)

This is where the fun begins. There is no definitive answer for which notes to choose. We start by creating a variable called "tones_sequence" that includes a sequence of notes and pauses, defined by the "sleep" and "play_tone" lines. We can define the "play_tone" function as follows:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/1de19b1c-a73a-4633-89f4-7441eb57e0cb)

In "tones_sequence" we tell the buzzer which notes to emit and when to take pauses and this is done by the "sleep" line and "play_tone". "play_tone" is a def that we created here:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/cbd3c945-4bb3-4423-be7a-c5611369254c)

In this function, we also control the volume using "buzzer.duty_u16(5000)".

The code as a whole is relatively simple. The main sensor is the tilt switch, which has two values: 0 and 1. The value 1 indicates movement or a change in tilt, while 0 indicates no movement.

We start with a while loop where we assign a name to the tilt value: ![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/e35ed47f-eff1-4c8d-b836-dba024176ede)

Next, we add the main if statement:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/94b62d67-411f-4a14-8d7d-506bf0ea3f6b)

This code checks if the sensor is detecting any movement. If it is, the LED blinks, and the warning sound is activated. Now we have both visual and auditory warnings for anyone who touches the box. This should be sufficient to deter someone from tampering with your belongings. You have many customization options for the sound and light. In the provided code, three colors are defined:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/58d2e0d8-8ec1-4b8e-b135-b5e2b96e066f)

But you can activate multiple colors simultaneously. For example: ![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/06ff2e1f-a3f9-4251-bf37-0908666d28ea)

This would result in a purple light. I encourage you to experiment with different tones and mix colors to achieve the desired effect.

<h1>Transmitting the data / connectivity </h1>

For data transmission, we are using Wi-Fi and MQTT protocol for connectivity. Wi-Fi is not the best option as it may consume more battery life. An ideal option would be LoRaWAN if you have a reliable connection to Helium or The Things Network (TTN). Unfortunately, in my case, I didn't have a nearby connection to TTN, although there were several Helium servers around. Connecting via LoRaWAN would have required adding a modem to the breadboard, which would make the setup larger. My box couldn't accommodate the additional modem.

We want to send the data values from the tilt switch (1 or 0). The transmission is triggered by changes in the sensor and not something done manually.

Connecting to Wi-Fi is straightforward. You need to provide your home Wi-Fi name (SSID) and password. Create a file called boot.py and add the following code for connectivity. You can find this code uploaded to this GitHub repository.

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/9ea240e4-c7fc-4ae3-85a2-5b46e2bfc5d1)

The image above shows the code necessary for data transmission. The code above the "else" statement is inside the if statement. We send the data with the number 1, indicating that the box was opened. We add a sleep command to avoid sending too many requests. Sending data too frequently can result in a ban where you are no longer allowed to send data. Therefore, we introduce a 5-second delay. This means that every 5 seconds, the system will reset and send the new value.


<h1>Presenting the data </h1>

Now, let's move on to the final part of this project: displaying the data we sent to Ubidots. We start by creating two events:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/b5e3b03f-f277-4248-8f54-bccc4c1d6809)

Ubidots will now respond to data that is 0 or 1. For the visual representation, we only need basic widgets. We want to know if the value changes and display a nice switch with a color that represents whether the box is in danger or not.

![Off](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/2df3100b-4bfe-478e-96fe-481108886af7)

As we can see on the picture above we are only using two widgets which is a "Guage" and a "indicator" widget. On the picture we see that the value is 0 and the indicator is green with a message that says "off".

This is a good visual representation of the box not being opened.

![On](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/008abb8e-9db2-498a-a9db-90ca141fb49f)

When the value changes to 1, indicating that someone has opened the box, the gauge turns to 1, and the indicator turns red with the message "ON". This indicates that the box has been opened.

When examining the data in more detail, which can be done by clicking "Explore Data" in Ubidots, we are presented with a layout like the one below:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/bd7c4ff8-c1cc-472e-bb35-084aca170c05)

Here we can see the timestamps and corresponding values sent by the sensor. The timestamps may appear inconsistent in this image because I unplugged the Pico multiple times while experimenting with other things. However, if the Pico is continuously connected to a power source, you should have consistent updates every 5 seconds.

<h1>Finalizing the design </h1>

Overall, this project was a lot of fun to build and experiment with. I achieved the goal I had in mind, and I am very satisfied with the result. Here are some pictures of the sensor in different modes:

Not active:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/15c549b6-7db0-4dc1-97ff-e5d7baa382f6)

Active:

![image](https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/24636eee-0f99-4750-8868-a4357ce42626)

This is how I would attach it to my box at home. I would need to find something to hold it securely to the roof of the box.

https://github.com/Mussse97/My_IOT_project_1DT305/assets/89797827/d2ba5194-307e-4bcd-af03-2ede998da6d7

This is not the best way of showinbg the alarm, i didn't have a good enough way of securing the alarm on the top of the roof without it falling down. This video is only when the roof is up.

<h2>Potential Additions</h2>

I had some interesting ideas for additions, but I came up with them at the last minute, making them a bit challenging to implement. The thought was that it might be annoying if the alarm goes off even when I open the box myself. So, my plan was to differentiate between myself and others.

My first idea was to check if my phone was connected to the home Wi-Fi, and if I was present at home, the alarm wouldn't go off. Unfortunately, I couldn't access the MAC address through the Pico, which can usually be found on your router's website.

The other plan was to utilize Bluetooth and apply the same concept. However, I later discovered that I would need a Bluetooth modem, which I didn't have at the time. I believe adding this feature would greatly enhance the project, and it's something I plan to incorporate in the near future.


