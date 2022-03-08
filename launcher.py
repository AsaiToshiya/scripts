#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import subprocess

PIN = 17
CMD = "/home/pi/bin/ledblink.py" # 実行するプログラム

GPIO.setmode(GPIO.BCM)

# プルアップ抵抗を有効にする
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

p = None

try:
    while True:
        # 立ち下がりエッジが検出されるまで待機する
        GPIO.wait_for_edge(PIN, GPIO.FALLING)

        if p is None:
            # プログラムを実行する
            p = subprocess.Popen("exec " + CMD, shell=True)
        else:
            # プログラムを終了する
            p.kill()
            p = None
except KeyboardInterrupt:
    # Ctrl-C
    GPIO.cleanup()