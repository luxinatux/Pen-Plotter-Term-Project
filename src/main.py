#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:00:23 2022

@author: dylanruiz
"""
import gc
import pyb
import cotask
import time
import task_share
import closedloop
import encoder_Ruiz_Martos
import motor_Ruiz_Martos
import math


def task_Encoder():
    """!
    Task which initializes and updates encoder 1. 
    Continuously writes the encoder position to the shared variable.
    """

    # Initializes Enc 1 Timer and Channels
    in1_enc_A = pyb.Pin(pyb.Pin.cpu.B6)
    in2_enc_A = pyb.Pin(pyb.Pin.cpu.B7)
    encoder1 = encoder_Ruiz_Martos.Encoder(in1_enc_A, in2_enc_A, 4)

    # Initializes Enc 2 Timer and Channels
    in1_enc_B = pyb.Pin(pyb.Pin.cpu.C6)
    in2_enc_B = pyb.Pin(pyb.Pin.cpu.C7)
    encoder2 = encoder_Ruiz_Martos.Encoder(in1_enc_B, in2_enc_B, 8)

    # Initializes limit switches as a pin input
    Limit_switch_Belt = pyb.Pin(pyb.Pin.cpu.A7, pyb.Pin.IN)
    Limit_switch_Elbow = pyb.Pin(pyb.Pin.cpu.A5, pyb.Pin.IN)

    # Initial encoder state
    enc_state = 0
  
    count = 0
    while True:

        # If Limit Switch is activated, initializes zeroing process for Belt.
        if Limit_switch_Belt.value() == 1:
            Zero_Flag_Belt.put(1)
            encoder2.set_position(0)

        # If Limit Switch is activated, initializes zeroing process for Elbow.
        if Limit_switch_Elbow.value() == 1:
            Zero_Flag_Elbow.put(1)
            encoder1.set_position(0)
            
        # Only run at beginning of program, when running to home position
        if Execute_Flag.get() == 0:
            if Zero_Flag_Belt.get() == 1 and Zero_Flag_Elbow.get() == 1:
                enc_state = 1
        if Terminate_Flag.get() != 1:
            # General Encoder state, constantly updates and activates/deactivates solenoid
            if enc_state == 0:
                if count == 0:
                    encoder1.set_position(0)
                    encoder2.set_position(0)
                count +=1
                encoder1.update()
                encoder2.update()
                Belt_position.put(encoder1.get_position())
                Elbow_position.put(encoder2.get_position())
                if Solenoid_activation.get() == 1:
                    pinC1 = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OUT_PP)
                    pinC1.low()
                elif Solenoid_activation.get() == 0:
                    pinC1 = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OPEN_DRAIN, value=1)
                yield (0)
    
            # Encoder state used to zero system, sets encoder positions to zero when limit switches activate
            elif enc_state == 1:
                encoder2.set_position(0)
                #Elbow_position.put(encoder2.get_position())
                encoder1.set_position(0)
                #Belt_position.put(encoder1.get_position())
                enc_state = 0
                yield(0)
        elif Terminate_Flag.get() == 1:
            pinC1 = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OUT_PP)
            pinC1.low()

        else:
            yield(0)


def task_controller():
    """!
    Task which initializes motor 1. 
    Controller object updates the duty cycle to the motor and allows closed loop proportional control.
    Continuously prints the position and time for the data to be processed.
    """

    # Sets Gain Value of Proportional Controller
    Gain_Elbow = 0.7
    Gain_Belt = 0.15

    # Initializes Closed Loop Object
    Closed_loop_Elbow = closedloop.ClosedLoop(Gain_Elbow, 0)
    Closed_loop_Belt = closedloop.ClosedLoop(Gain_Belt, 0)

    # Initial Controller State
    controller_state = 0
   
    while True:
        
        # Only Runs in the beginning of the program
        if Execute_Flag.get() == 0:

            # Stops Elbow motor once limit switch is acivated
            if Zero_Flag_Elbow.get() == 1:
                controller_state = 2

             # Stops Elbow motor once limit switch is acivated
            if Zero_Flag_Belt.get() == 1:
                controller_state = 1

            # Stops both motors if both limit switches activated
            if Zero_Flag_Belt.get() == 1 and Zero_Flag_Belt.get() == 1:
          
                controller_state = 3

        # Sets controller state when system is ready to run
        if Execute_Flag.get() == 1:
            controller_state = 4

        # Runs both motors to run at a certain speed until it hits the limit switches
        if controller_state == 0:
            Duty_cycle_elbow.put(-50)
            Duty_cycle_belt.put(-50)
            yield(0)

        # Stops Belt motor once limit switch is acivated
        elif controller_state == 1:
          
            Duty_cycle_belt.put(0)
            yield(0)

        # Stops Elbow motor once limit switch is activated
        elif controller_state == 2:
            Duty_cycle_elbow.put(0)
            yield(0)
        # Stops both motors if both limit switches activated, Initializes program execution
        elif controller_state == 3:
        
            Duty_cycle_elbow.put(0)
            Duty_cycle_belt.put(0)

            if Terminate_Flag != 1:
                Execute_Flag.put(1)
            yield(0)

        # General state of controller, Constant updates duty cycles of controller based on position
        elif controller_state == 4:
     
            if Terminate_Flag.get() != 1:
                Duty_cycle_elbow.put(int(Closed_loop_Elbow.update(
                    int(Elbow_position_target.get()), int(Elbow_position.get()))))
                Duty_cycle_belt.put(int(Closed_loop_Belt.update(
                    int(Belt_position_target.get()), int(Belt_position.get()))))

                # Once position is within threshold for target, flags next point activation
                if abs(Elbow_position_target.get()-Elbow_position.get()) <= 20 and abs(Belt_position_target.get()-Belt_position.get()) <= 600:
                    Next_Point_Flag.put(1)
                yield(0)
            # Terminates program, model will run back to home position
            if Terminate_Flag.get() == 1:
                Execute_Flag.put(0)
                controller_state = 0
                Duty_cycle_belt.put(0)
                Duty_cycle_elbow.put(0)
            yield(0)
        yield(0)


def task_motor():
    # initialize both Motors
    enableA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
    in1_mot = pyb.Pin(pyb.Pin.cpu.B4)
    in2_mot = pyb.Pin(pyb.Pin.cpu.B5)
    motor_belt = motor_Ruiz_Martos.Motor(
        enableA, in1_mot, in2_mot, 3)  # motor in A
    motor_belt.enable()

    enableB = pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_PP)
    in1_motB = pyb.Pin(pyb.Pin.cpu.A0)
    in2_motB = pyb.Pin(pyb.Pin.cpu.A1)
    motor_elbow = motor_Ruiz_Martos.Motor(
        enableB, in1_motB, in2_motB, 5)  # motor in B
    motor_elbow.enable()

    while True:
        if Terminate_Flag.get() != 1:
            # Constantly updates motor duty cycles based on Controller direction
            motor_belt.set_duty(Duty_cycle_belt.get())
            motor_elbow.set_duty(Duty_cycle_elbow.get())
            print(Duty_cycle_belt.get())
        if Terminate_Flag.get() == 1:
            motor_belt.set_duty(0)
            motor_elbow.set_duty(0)
        yield(0)
        
        


# def task_Drawing():
#         draw_state = 0
#         # Cycles through points and adds them to the shared variables once the Next_Point_Flag is raised
#         if draw_state == 0:


#             if Next_Point_Flag.get() == 1:

#                 if Elbow_position_target.any():
#                     Elbow_position_target.put(Elbow_position_queue.get())
#                     Belt_position_target.put(Belt_position_queue.get())
#                     Solenoid_activation.put(Solenoid_position_queue.get())
#                     Next_Point_Flag.put(0)
#                     yield(0)
#                 else:
#                     Terminate_Flag.put(1)
#                     draw_state = 0

#             yield(0)


if __name__ == "__main__":

    # instantiate shared and queued objects
    Elbow_position = task_share.Share(
        'i', thread_protect=False, name="Elbow Position")
    Belt_position = task_share.Share(
        'i', thread_protect=False, name="Belt Position")

    Elbow_position_target = task_share.Share(
        'i', thread_protect=False, name="Elbow Target Position")
    Belt_position_target = task_share.Share(
        'i', thread_protect=False, name="Belt Target Position")
    Solenoid_activation = task_share.Share(
        'i', thread_protect=False, name="Solenoid Activation")

    Terminate_Flag = task_share.Share(
        'i', thread_protect=False, name="Terminate Flag")
    Next_Point_Flag = task_share.Share(
        'i', thread_protect=False, name="Next Point Flag")

    Duty_cycle_elbow = task_share.Share(
        'i', thread_protect=False, name="Duty Cycle Elbow")
    Duty_cycle_belt = task_share.Share(
        'i', thread_protect=False, name="Duty Cycle Belt")

    Zero_Flag_Elbow = task_share.Share(
        'i', thread_protect=False, name="Set Elbow zero flag")
    Zero_Flag_Belt = task_share.Share(
        'i', thread_protect=False, name="Set Belt zero flag")

    Execute_Flag = task_share.Share(
        'i', thread_protect=False, name="Execute Flag")

    # Elbow_position_queue = task_share.Queue('i', 2500, thread_protect = False, overwrite = False,
    #                        name = "Elbow Positions Queue")
    # Belt_position_queue = task_share.Queue('i', 2500, thread_protect = False, overwrite = False,
    #                        name = "Belt Positions Queue")
    # Solenoid_position_queue = task_share.Queue('i', 2500, thread_protect = False, overwrite = False,
    #                        name = "Belt Positions Queue")

    # Create Task Objects
    # task_Draw_calc = cotask.Task(task_Drawing, name = 'Task_Drawing_Calcs', priority = 0,
    #                     period = 50, profile = True, trace = False)

    task_controller = cotask.Task(task_controller, name='Task_Controller', priority=2,
                                  period=15, profile=True, trace=False)

    task_motor = cotask.Task(task_motor, name='Task_motor', priority=1,
                             period=15, profile=True, trace=False)

    task_encoder = cotask.Task(task_Encoder, name='Task_Encoder', priority=1,
                               period=5, profile=True, trace=False)

    # cotask.task_list.append(task_Draw_calc)
    cotask.task_list.append(task_controller)
    cotask.task_list.append(task_motor)
    cotask.task_list.append(task_encoder)

    # Run the memory garbage collector to ensure memory is as defragmented as
    # possible before the real-time scheduler is started
    gc.collect()

    x_1 = 2.5  # x-Length from rotating center to paper origin [in]
    y_1 = 4.5  # y-Length from rotating center to paper origin [in]
    # Length from rotating center to paper origin [in]
    r = (x_1**2+y_1**2)**(1/2)
    Elbow_Ratio = 4192/(2*math.pi)  # Ticks/Radian
    Belt_Ratio = 24500/(20*2*0.03937007874)  # Ticks/in
    # Initial Draw State
    draw_state = 0
    # Sets up serial port communication
    ser = pyb.USB_VCP()
    my_str = ''
    print("Enter File Name")

    # Initializes Execute Flag to not run until it has calculated all the coordinates.
    Execute_Flag.put(0)


    # Initializes Execute Flag to not run until it has calculated all the coordinates.
    while True:

        # Initial draw state, Sets up lists and waits for user to insert file name of HPGL code
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
            if ser.any():
                char_in = ser.read(1).decode()

                if char_in == '\x7F':
                    if my_str == '':
                        my_str = my_str
                        ser.write(char_in)

                    else:
                        a = len(my_str)
                        b = a-1
                        my_str = my_str[:b]
                        ser.write(char_in)

                elif char_in == '\r' or char_in == '\n':
                    draw_state = 1

                else:
                    my_str += char_in
                    ser.write(char_in)
        # Tries to open file, if no file is found returns user back to inserting file name (state 0)
        if draw_state == 1:
            try:
                file = open(my_str, "r")
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
             print('State 2')
             for line in file:
    
                 state = 0
                 x=line.split(";")
                 
                 for i in range(0,len(x)):
                     state = 0
                     Pen_up = -1
                     Pen_down = -1
                     x_2 = x[i].split(",")
                     z_value = 0
                     for n in range(0,len(x_2),2):
                         
                         try: 
                             float(x_2[n]) 
                         except:
                             N_1 = False
                         else:
                             N_1 = True
                             
                         if N_1 == False:
                             Pen_up = x_2[n].find('PU')
                             Pen_down = x_2[n].find('PD')
                             
                             if Pen_up != -1:
                         
            
                                  try:
                                      test = x_2[1]
                                  except:
                                      state = 1
                                    
                                  if state == 0:
                                    
                                        x_3 = x_2[0].strip('PU')
                                        x_list.append(x_3)
                                        y_list.append(x_2[1])
                                        z_list.append(up)
                                  
                            
                             
                             if Pen_down != -1:
                         
                    
                                  try:
                                      test = x_2[1]
                                  except:
                                      state = 1
                                     
                                  if state == 0:
                                     
                                     x_3 = x_2[0].strip('PD')
                                     x_list.append(x_3)
                                     y_list.append(x_2[1])
                                     z_list.append(down)
                                  
                                     
                         if N_1 == True:
                            z_value = z_list[len(z_list)-1]
                            # try:
                            #     test = x_2[1]
                            # except:
                            #     state = 1
                                
                            if state == 0:
                                x_list.append(x_2[n])
                                y_list.append(x_2[n+1])
                                z_list.append(z_value)
                              
                            
                        
                        
                        
             draw_state = 3
         
             
         # Converts all the string coordinates to floats and appends them in a new list
        if draw_state == 3:
             print('State_3')
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
             print('State_4')
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
                     
                 b = Hyp*math.sin(Theta_1+Theta_2)/math.sin(Theta_3)
                 Arm_angle.append(Theta_3*Elbow_Ratio)
                 Belt_Distance.append((b-(r-1))*Belt_Ratio)
             
                 
         
             for i in range(len(Arm_angle)-1):
                print('{:},{:},{:}'.format(Arm_angle[i],Belt_Distance[i],z_coordinate[i]))
                 
             
        
            
             point = 0
             up = 0
             down = 1
           
             break
                # Run the scheduler with the chosen scheduling algorithm. Quit if any
        # character is received through the serial port
    while True:
        cotask.task_list.pri_sched()

        if Next_Point_Flag.get() == 1:
          
            try:
                Elbow_position_target.put(int(Arm_angle[point]))
                Belt_position_target.put(int(Belt_Distance[point]))
                Solenoid_activation.put(int(z_coordinate[point]))
                Next_Point_Flag.put(0)
                print('Next_point')
                point += 1

            except:
                print('Terminate')
                Terminate_Flag.put(1)
