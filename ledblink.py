#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
    while True:
        # 点灯
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(0.5)

        # 消灯
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    # Ctrl-C
    GPIO.cleanup()