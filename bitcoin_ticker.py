#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socketio
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import sevensegment

# チャンネル
CHANNEL = "lightning_ticker_BTC_JPY"

# 7 セグメント LED
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
seg = sevensegment(device)

# Socket.IO
sio = socketio.Client()

# 7 セグメント LED の桁数
digits = seg.device.width

@sio.event
def connect():
    sio.emit("subscribe", CHANNEL)

@sio.on(CHANNEL)
def on_subscribe(data):
    # 最終取引価格を表示する
    ltp = str(data["ltp"])
    padding = " " * (digits - len(ltp)) # 右寄せにするためのパディング
    seg.text = padding + ltp

# 7 セグメント LED の明るさを下げる
seg.device.contrast(0)

# bitFlyer に接続する
sio.connect("https://io.lightstream.bitflyer.com", transports=["websocket"])
sio.wait()