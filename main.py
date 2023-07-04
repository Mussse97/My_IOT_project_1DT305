
import time
from machine import Pin, PWM
from utime import sleep
import network
import urequests as requests
import random

TOKEN = "BBFF-qpFtFVLCeSkvC3GJ1GoeZgSapYFIor" #Put here your TOKEN
DEVICE_LABEL = "PicoAlarmBoard" # Assign the device label desire to be send
VARIABLE_LABEL = "Sensor"  # Assign the variable label desire to be send
WIFI_SSID = "TP-Link_6D02" # Assign your the SSID of your network
WIFI_PASS = "Hussein123" # Assign your the password of your network
DELAY = 5  # Delay in seconds

LED_Pin_Red = Pin(26, Pin.OUT)
LED_Pin_Green = Pin(27, Pin.OUT)
LED_Pin_Blue = Pin(28, Pin.OUT)
tiltPin = Pin(11, Pin.IN)
buzzer = PWM(Pin(15))
tones = {
    "C4": 262,
    "C#4": 277,
    "Db4": 277,
    "D4": 294,
    "D#4": 311,
    "Eb4": 311,
    "E4": 330,
    "F4": 349,
    "F#4": 370,
    "Gb4": 370,
    "G4": 392,
    "G#4": 415,
    "Ab4": 415,
    "A4": 440,
    "A#4": 466,
    "Bb4": 466,
    "B4": 494,
    "C5": 523,
    "C#5": 554,
    "Db5": 554,
    "D5": 587,
    "D#5": 622,
    "Eb5": 622,
    "E5": 659,
    "F5": 698,
    "F#5": 740,
    "Gb5": 740,
    "G5": 784,
    "G#5": 831,
    "Ab5": 831,
    "A5": 880,
    "A#5": 932,
    "Bb5": 932,
    "B5": 988,
    "C6": 1047,
    "C#6": 1109,
    "Db6": 1109,
    "D6": 1175,
    "D#6": 1245,
    "Eb6": 1245,
    "E6": 1319
}

def play_tone(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(5000)
    time.sleep(duration)
    buzzer.duty_u16(0)

def play_warning_sound():
    tones_sequence = ["C4", "E4", "G4", "B4", "C5"]
    for note in tones_sequence:
        play_tone(tones[note], 0.2)
        time.sleep(0.1)

tilt_value = tiltPin.value()
def connect():
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(WIFI_SSID, WIFI_PASS)  # Your WiFi Credential
        print('Waiting for connection...', end='')
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip

# Builds the json to send the request
def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except:
        return None

# Random number generator
def random_integer(upper_bound):
    return random.getrandbits(32) % upper_bound

# Sending data to Ubidots Restful Webserice
def sendData(device, variable, value):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass


while True:
    tilt_value = tiltPin.value()
    
    if tiltPin.value() == 1:
       
      print("Tilt value:", tilt_value)
      LED_Pin_Blue.value(1)
      play_warning_sound()
      LED_Pin_Blue.value(0)
      time.sleep(1)
      returnValue = sendData(DEVICE_LABEL, VARIABLE_LABEL, 1)
      time.sleep(5)
     
    else:
        returnValue = sendData(DEVICE_LABEL, VARIABLE_LABEL, 0)
        time.sleep(5)



