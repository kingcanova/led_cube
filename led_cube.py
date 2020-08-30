#!/usr/bin/env python3

from gpiozero import LED
from time import sleep

layer1 = LED(5)
layer2 = LED(24)
one = LED(6)
two = LED(26)
three = LED(13)
four = LED(19)
sleepTime = .008

one.off()
two.off()
three.off()
four.off()


def function_one():
    # CYCLE 1
    layer1.off()
    layer2.off()
    one.on()
    two.on()
    sleep(sleepTime)
    # CYCLE 2
    four.on()
    two.on()
    sleep(sleepTime)
    # CYCLE 3
    three.on()
    four.on()
    # CYCLE 4
    one.on()
    three.on()


while True:
    function_one()


