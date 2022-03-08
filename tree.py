#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import RPi.GPIO as GPIO
import time

BOTTOM_LEFT = 26
BOTTOM_RIGHT = 5
MIDDLE_LEFT = 13
MIDDLE_RIGHT = 19
TOP = 6

# GPIO の設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(BOTTOM_LEFT, GPIO.OUT)
GPIO.setup(BOTTOM_RIGHT, GPIO.OUT)
GPIO.setup(MIDDLE_LEFT, GPIO.OUT)
GPIO.setup(MIDDLE_RIGHT, GPIO.OUT)
GPIO.setup(TOP, GPIO.OUT)

try:
    while True:
        # ランダムに LED を点灯する
        GPIO.output(BOTTOM_LEFT, random.randint(0, 1))
        GPIO.output(BOTTOM_RIGHT, random.randint(0, 1))
        GPIO.output(MIDDLE_LEFT, random.randint(0, 1))
        GPIO.output(MIDDLE_RIGHT, random.randint(0, 1))
        GPIO.output(TOP, random.randint(0, 1))

        time.sleep(0.5)

        # LED を消灯する
        GPIO.output(BOTTOM_LEFT, GPIO.LOW)
        GPIO.output(BOTTOM_RIGHT, GPIO.LOW)
        GPIO.output(MIDDLE_LEFT, GPIO.LOW)
        GPIO.output(MIDDLE_RIGHT, GPIO.LOW)
        GPIO.output(TOP, GPIO.LOW)

        time.sleep(0.5)
except KeyboardInterrupt:
    # Ctrl-C
    GPIO.cleanup()