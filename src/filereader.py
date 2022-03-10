#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 17:40:23 2022

@author: dylanruiz
"""
import math

x_1 = 10  # x-Length from rotating center to paper origin [in]
y_1 = 10  # y-Length from rotating center to paper origin [in]
# Length from rotating center to paper origin [in]
r = (x_1**2+y_1**2)**(1/2)
Elbow_Ratio = 4192/(2*math.pi)  # Ticks/Radian
Belt_Ratio = 24500/(20*2*0.03937007874)  # Ticks/in
#Initial Draw State
draw_state = 0

my_str = ''


# Initializes Execute Flag to not run until it has calculated all the coordinates.

while True:

     #Initial draw state, Sets up lists and waits for user to insert file name of HPGL code
     if draw_state == 0:
         x_list = []
         y_list = []
         z_list = []
         x_coordinate = []
         y_coordinate = []
         z_coordinate = []
         Arm_angle = []
         Belt_Distance = []
         
         # User inserts characters to insert file name
         my_str = input('Enter File Name:')
         draw_state = 1
           
     
     # Tries to open file, if no file is found returns user back to inserting file name (state 0)
     if draw_state == 1:
         try:
             file = open(my_str,"r")
         except:
             draw_state = 0
             print("File Not Found! Enter Another File Name")
         else: 
             draw_state = 2
             my_str = ''
        
                 
     # Processes file to usable HPGL cartesian coordinates
     if draw_state == 2:
         up = 0
         down = 1
         for line in file:

             state = 0
             x=line.split(";")
             
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
         draw_state = 3
     
         
     # Converts all the string coordinates to floats and appends them in a new list
     if draw_state == 3:
         for i in range(len(x_list)-1):
             x_coordinate.append(float(x_list[i])/1016) #1016 points per inch
             y_coordinate.append(float(y_list[i])/1016) #1016 points per inch
             z_coordinate.append(z_list[i])
         x_list = []
         y_list = []
         z_list = []
         draw_state = 4
        
     
     # Converts cartesian coordinates to our cylindrical coordinates
     if draw_state == 4:
         for i in range(len(x_coordinate)-1):
             Hyp = (x_coordinate[i]**2+y_coordinate[i]**2)**(1/2)
             try:
                 Theta_1 = math.atan(y_coordinate[i]/x_coordinate[i])
             except:
                 Theta_1 = math.pi/2
             try:
                 Theta_2 = math.atan(y_1/x_1)
             except:
                 Theta_2 = math.pi/2
             try:  
                 Theta_3 = math.atan(Hyp*math.sin(Theta_1+Theta_2)/(r-(Hyp*math.cos(Theta_2+Theta_1))))
             except:
                 Theta_3 = math.pi/2
                 
             b = math.sin(Theta_1+Theta_2)/math.sin(Theta_3)
             Arm_angle.append(Theta_3*Elbow_Ratio)
             Belt_Distance.append(b*Belt_Ratio)
         draw_state = 5
         break
     
             
         
         
             