const gpio = require('rpi-gpio');

const PIN = 4;

// ピンの状態
let state = true;

gpio.setMode(gpio.MODE_BCM);
gpio.setup(PIN, gpio.DIR_OUT, () => {
  setInterval(() => {
    gpio.write(PIN, state);
    state = !state;
  }, 500);
});
