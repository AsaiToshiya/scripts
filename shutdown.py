#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import os
import time

PIN = 3

GPIO.setmode(GPIO.BCM)

# プルアップ抵抗を有効にする
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    # 立ち下がりエッジが検出されるまで待機する
    GPIO.wait_for_edge(PIN, GPIO.FALLING)

    # 3 秒の長押し
    i = 0
    while GPIO.input(PIN) == GPIO.LOW:
        i += 1
        if i > 30:
            os.system("shutdown -h now")
            break

        time.sleep(0.1)