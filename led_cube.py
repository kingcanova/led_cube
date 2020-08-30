#!/usr/bin/env python3

from gpiozero import LED
from time import sleep

layer1 = LED(5)
layer2 = LED(24)
one = LED(6)
two = LED(26)
three = LED(13)
four = LED(19)
sleepTime = .01

one.off()
two.off()
three.off()
four.off()


def wall_swing():
    sleepTime = .5
    # CYCLE 1
    layer1.off()
    layer2.off()
    one.on()
    two.on()
    three.off()
    four.off()
    sleep(sleepTime)
    # CYCLE 2
    four.on()
    two.on()
    one.off()
    three.off()
    sleep(sleepTime)
    # CYCLE 3
    three.on()
    four.on()
    one.off()
    two.off()
    sleep(sleepTime)
    # CYCLE 4
    one.on()
    three.on()
    two.off()
    four.off()
    sleep(sleepTime)


def function_two():
    sleepTime = .5
    # CYCLE 1
    layer1.off()
    layer2.on()
    one.on()
    two.off()
    three.off()
    four.off()
    sleep(sleepTime)
    # CYCLE 2
    layer1.on()
    layer2.off()
    sleep(sleepTime)
    # CYCLE 3
    two.on()
    one.off()
    three.off()
    four.off()
    sleep(sleepTime)
    # CYCLE 4
    layer1.off()
    layer2.on()
    sleep(sleepTime)
    # CYCLE 7
    four.on()
    one.off()
    two.off()
    three.off()
    sleep(sleepTime)
    # CYCLE 8
    layer1.off()
    layer2.on()
    sleep(sleepTime)
    # CYCLE 5
    three.on()
    two.off()
    one.off()
    four.off()
    sleep(sleepTime)
    # CYCLE 6
    layer1.on()
    layer2.off()
    sleep(sleepTime)


while True:
    function_two()


