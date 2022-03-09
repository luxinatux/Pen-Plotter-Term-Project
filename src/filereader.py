#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 17:40:23 2022

@author: dylanruiz
"""

file = open("Test_Drawing.hpgl","r")
x_list = []
y_list = []
z_list = []
up = "1"
down = "0"



         
for line in file:

    state = 0
    x=line.split(";")
    print(x)
    
    for i in range(0,len(x)):
        state = 0
        Pen_up = -1
        Pen_down = -1
        try: 
            float(x[i]) 
        except:
            N_1 = False
        else:
            N_1 = True
            
        if N_1 == False:
            Pen_up = x[i].find('PU')
            Pen_down = x[i].find('PD')
            
        if Pen_up != -1:
    
            x_2 = x[i].split(",")
            try:
                test = x_2[1]
            except:
                state = 1
                
            if state == 0:
                
                x_3 = x_2[0].strip('PU')
                x_list.append(x_3)
                y_list.append(x_2[1])
                z_list.append(up)
                for n in range(3,len(x_2),2):
                    x_list.append(x_2[n-1])
                    y_list.append(x_2[n])
                    z_list.append(up)
                
           
            
        if Pen_down != -1:
    
            x_2 = x[i].split(",")
            try:
                test = x_2[1]
            except:
                state = 1
                
            if state == 0:
                
                x_3 = x_2[0].strip('PD')
                x_list.append(x_3)
                y_list.append(x_2[1])
                z_list.append(down)
                for n in range(3,len(x_2),2):
                    x_list.append(x_2[n-1])
                    y_list.append(x_2[n])
                    z_list.append(down)
                
                
    for i in range(len(x_list)):
        print("[{:},{:},{:}]".format(x_list[i],y_list[i],z_list[i]))
            
        
   
