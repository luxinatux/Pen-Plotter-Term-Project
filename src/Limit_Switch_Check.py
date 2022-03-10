# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:13:31 2022

@author: Dylan
"""
import pyb
import time
if __name__ == '__main__':
    
    Limit_switch_Elbow = pyb.Pin(pyb.Pin.cpu.A7,pyb.Pin.IN)
    
    Limit_switch_Belt = pyb.Pin(pyb.Pin.cpu.A5,pyb.Pin.OUT_PP)
    Limit_switch_Belt.low()
    time.sleep(1)
    
    Limit_switch_Belt = pyb.Pin(pyb.Pin.cpu.A5,pyb.Pin.IN)
    
    count = 0
    
    while True:
        #print('{:},{:}'.format(Limit_switch_Belt.value(),Limit_switch_Elbow.value()))
        if Limit_switch_Belt.value() == 1:
            print("belt")
        if Limit_switch_Elbow.value() == 1:
             print("window")
        time.sleep(.1)
        count += 1
        if count == 100:
            break
        