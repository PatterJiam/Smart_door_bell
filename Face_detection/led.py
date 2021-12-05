from gpiozero import PWMLED
from signal import pause
from time import sleep

led = PWMLED(27)

# Turn LED off
def off():
	return led.off()

# Turn LED on
def on():
	return led.pulse(0.5,0.5)
