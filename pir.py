#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

PIR_PIN = 27
LED_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        if GPIO.input(PIR_PIN): # 1 (High)
            # LED を点灯する
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            # LED を消灯する
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(0.1)
except KeyboardInterrupt:
    # Ctrl-C
    GPIO.cleanup()