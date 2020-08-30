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


def led_leads(a, b, c, d):
    if a == 1:
        one.on()
    else:
        one.off()

    if b == 1:
        two.on()
    else:
        two.off()

    if c == 1:
        three.on()
    else:
        three.off()

    if d == 1:
        four.on()
    else:
        four.off()


def layer_leads(one, two):
    if one == 0 and two == 1:
        layer1.off()
        layer2.on()
    if one == 1 and two == 0:
        layer2.off()
        layer1.on()
    if one == 0 and two == 0:
        layer1.off()
        layer2.off()
    if one == 1 and two == 1:
        layer1.on()
        layer2.on()


def wall_swing():
    sleepTime = .5
    # CYCLE 1
    layer1.off()
    layer2.off()
    led_leads(1, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 2
    led_leads(0, 1, 0, 1)
    sleep(sleepTime)
    # CYCLE 3
    led_leads(0, 0, 1, 1)
    sleep(sleepTime)
    # CYCLE 4
    led_leads(1, 0, 1, 0)
    sleep(sleepTime)


def moving_pixel():
    sleepTime = .5
    # CYCLE 1
    layer1.off()
    layer2.on()
    led_leads(1, 0, 0, 0)
    sleep(sleepTime)
    # CYCLE 2
    layer1.on()
    layer2.off()
    led_leads(1, 0, 0, 0)
    sleep(sleepTime)
    # CYCLE 3
    led_leads(0, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 4
    layer1.off()
    layer2.on()
    led_leads(0, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 5
    led_leads(0, 0, 0, 1)
    sleep(sleepTime)
    # CYCLE 6
    layer1.on()
    layer2.off()
    led_leads(0, 0, 0, 1)
    sleep(sleepTime)
    # CYCLE 7
    led_leads(0, 0, 1, 0)
    sleep(sleepTime)
    # CYCLE 8
    layer2.on()
    layer1.off()
    led_leads(0, 0, 1, 0)
    sleep(sleepTime)


def diagonal_bounce():
    sleepTime = .5
    # CYCLE 1
    layer1.off()
    layer2.on()
    led_leads(1, 0, 0, 0)
    sleep(sleepTime)
    # CYCLE 2
    layer2.off()
    layer1.on()
    led_leads(0, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 3
    layer1.off()
    layer2.on()
    led_leads(0, 0, 0, 1)
    sleep(sleepTime)
    # CYCLE 4
    layer2.off()
    layer1.on()
    led_leads(0, 0, 1, 0)
    sleep(sleepTime)
    # CYCLE 5
    layer1.off()
    layer2.on()
    led_leads(0, 0, 0, 1)
    sleep(sleepTime)
    # CYCLE 6
    layer2.off()
    layer1.on()
    led_leads(0, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 7
    layer1.off()
    layer2.on()
    led_leads(1, 0, 0, 0)
    sleep(sleepTime)
    # CYCLE 8
    layer2.off()
    layer1.on()
    led_leads(1, 0, 0, 0)
    sleep(sleepTime)
    # CYCLE 9
    layer1.off()
    layer2.on()
    led_leads(0, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 10
    layer2.off()
    layer1.on()
    led_leads(0, 0, 0, 1)
    sleep(sleepTime)
    # CYCLE 11
    layer1.off()
    layer2.on()
    led_leads(0, 0, 1, 0)
    sleep(sleepTime)
    # CYCLE 12
    layer2.off()
    layer1.on()
    led_leads(0, 0, 0, 1)
    sleep(sleepTime)
    # CYCLE 13
    layer1.off()
    layer2.on()
    led_leads(0, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 14
    layer2.off()
    layer1.on()
    led_leads(1, 0, 0, 0)
    sleep(sleepTime)


def wave():
    sleepTime = .5
    # CYCLE 1
    layer_leads(0, 1)
    led_leads(1, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 2
    layer_leads(1, 0)
    led_leads(1, 1, 0, 0)
    sleep(sleepTime)
    # CYCLE 3
    layer_leads(0, 1)
    led_leads(0, 0, 1, 1)
    sleep(sleepTime)
    # CYCLE 4
    layer_leads(1, 0)
    led_leads(0, 0, 1, 1)
    sleep(sleepTime)


while True:
    wave()


