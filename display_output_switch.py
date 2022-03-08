#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import subprocess
import time

PIR_PIN = 27
TURN_OFF = ['vcgencmd', 'display_power', '0']
TURN_ON = ['vcgencmd', 'display_power', '1']

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

i = 0

try:
    while True:
        if GPIO.input(PIR_PIN): # 1 (High)
            i = 0
            subprocess.run(TURN_ON, stdout=subprocess.DEVNULL)
    
        if i > 60:
            i = 0
            subprocess.run(TURN_OFF, stdout=subprocess.DEVNULL)

        i += 1
        time.sleep(1)
except KeyboardInterrupt:
    # Ctrl-C
    GPIO.cleanup()