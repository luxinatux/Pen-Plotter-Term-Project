# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:13:31 2022

@author: Dylan
"""
import pyb
import time
if __name__ == '__main__':
    
    Limit_switch_Belt = pyb.Pin(pyb.Pin.cpu.A10,pyb.Pin.IN)
    Limit_switch_Belt.value(1)
    Limit_switch_Elbow = pyb.Pin(pyb.Pin.cpu.C2,pyb.Pin.IN)
    count = 0
    
    while True:
        print(Limit_switch_Belt.value())
        time.sleep(.1)
        count += 1
        if count == 100:
            break
        