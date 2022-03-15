'''!
   @file                mainpage.py
   @brief               Brief doc for mainpage.py
   @details             Detailed doc for mainpage.py 

   @mainpage

   @section sec_intro   Introduction
                        This doxygen encapsulates our software design
                        for our pen plotter term project.Please view the term project page below
                        for the Software Design and FSM
   
   @author              Lucas Martos-Repath
   @author              Dylan Ruiz

   @copyright           License Info

   @date                February 24, 2022
   

   
   @page page_1         Term Project
   
   @section Sftw_ds     Software Design
   
   @subsection desc     Description of Software
                        This software consists of a files all used within the multitasking main.py file used to execute the pen-plotting protocol. Our software makes use of driver files that are imported into our main file. These driver files are closedloop.py, cotask.py, task_share.py, encoder_Ruiz_Martos.py and motor_Ruiz_Martos.py.
                        These driver files are used to implement closed loop control, shared variables and cooperative task management. These driver files also allow the control of both motors and encoders implemented in our design. A file named filereader.py is a file that is used to parse through hpgl files and convert them
                        into encoder ticks. The contents of that file are used within the main.py file. The rest of the files are demo files used to check the response of all hardware. There are also hpgl files that were used to demo our pen plotter after being modified slightly to help with memory issues. 
   
   @subsection tsk_d    Task Diagram
                        This task diagram below shows our software structure for how to acheive the overall functions of the pen plotter
                        task. There are three main tasks involved in our pen plotter design. The encoder task continuously updates the encoder positions and the solenoid actuation. 
                        It is also responsible for detecting the limit switches and zeroing the position of each encoder when those limit switches are pressed. This task shares the encoder positions with the controller task.
                        The controller task is responsible for calculating the duty cycles for each motor using the target position as reference. The controller task is the highest priority because it is the heart of the multitasking operation. It sends the duty cycles to the motor task
                        and indicates when the execution of the entire system is ready. The motor task is the simplest task. It constantly applies the duty cycle shared from the controller task to each of the motors. It is responsible for enabling and disabling the motors. Before the multitasking
                        is executed, the main file asks for the name of an hpgl file. It parses through the hpgl file and converts the hpgl coordinates to our system's relevant coordinates (encoder positions). After it calculates all the positions, it starts the multitasking operation.
                        
                        ## Task Diagram
                        
   @image html          task_diagram_1.0.png 
                        
   
   @subsection FSM_dr   Encoder Task FSM
                        This Finite State Machine is for the encoder task. The FSM starts out waiting for both limit switches to be pressed. The multitasking operation starts with both motors reaching their home positions, which is where the limit
                        switches are located. Once both limit switches are pressed in, it sets both encoder positions to 0 and moves to state 1. State 1 is where the encoder task will stay until the end of the pen plotter execution. This state updates both encoder positions and writes them to their
                        respective shared variables in order to share it with other tasks. This state also updates the solenoid actuation based on the shared variable being set in the main program. Once the terminate flag gets raised, the encoder FSM changes to state 3 which is the termination
                        state. The encoder releases the solenoid activation at this state. 
                         
   @image html          drawing_task_FSM.png 
                       
   @subsection FSM_c    Controller Task
                        This Finite State Machine is for the Controller task. State 0 sets both motors duty cycles at -50 until the arm and the belt hit the limit switches. If one hits the limit switch, that motor is disabled but the other motor will continue to run until it has also hit the limit switch.
                        If both limit switches are hit, the controller task moves onto state 2. State 2 just initializes the execution protocol by raising the execution flag. Once the execution flag is raised, the controller moves on to state 3. This state is where the controller continuously
                        updates the duty cycles of both motors by implementing a proportional controller. It updates the duty cycle shared variables and raises the next point flag once both encoders reach within a certain threshold of their designated point. This cycle continues once there is no 
                        points left and the terminate flag is raised. Once the terminate flag is raised, controller will move to state 4, which is the terminate state. This state stops both motors and lowers the execute flag.
                        
   @image html          Controller_task_1.0.png  
                        
                                                                
'''
        
        
        


