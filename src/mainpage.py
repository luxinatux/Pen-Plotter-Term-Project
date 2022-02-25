'''!
   @file                mainpage.py
   @brief               Brief doc for mainpage.py
   @details             Detailed doc for mainpage.py 

   @mainpage

   @section sec_intro   Introduction
                        This online portfolio encapsulates the totality of my 
                        work for ME 305 throuoght the quarter of Fall 2021
   
   @author              Lucas Martos-Repath
   @author              Dylan Ruiz

   @copyright           License Info

   @date                December 1, 2021
   

   
   @page page_L1        LAB 0x01
   
   @section sum_1       1.OVERVIEW
   
   @section FSM_1       2.FINITE STATE MACHINES
                        ![](State_Diagram.png)
                        
   @section vid_1       3.LED VIDEO
                        https://cpslo-my.sharepoint.com/:v:/g/personal/cvsantan_calpoly_edu/EV7XIjkioD9BppIICQ9KQdMBM13YV8a966G2egEc5d8akQ?e=hH06dX
                        
   @section code_1      4.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Lab%201%20code/

   @page page_L2        LAB 0x02
    
   @section sum_2       1.OVERVIEW
    
   @section FSM_2       2.FINITE STATE MACHINES
                        ##ENCODER FSM
                        ![](Encoder_Diagram.png)
                        
                        ##USER FSM
                        ![](User_Diagram.png)
                        
   @section task_2      3.TASK DIAGRAM
                        ![](Task_Diagram.png)
                        
                        
   @section code_2      4.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Lab%202%20code/
                        
   @page Page_L3        LAB 0x03
   
   @section sum_3       1.OVERVIEW
                        In this lab, our goal was to build onto our existing
                        code by implimenting spinning motors. This was 
                        achieved by creating a motor driver, and then creating
                        a motor task that would run the driver when called upon.
                        Flag variables were used to impiments the motor task 
                        into the user task.
                        
   @section FSM_3       2.FINITE STATE MACHINES
                        Since lab 3 builds off of lab 2, this FSM only shows
                        the newest states added since then.
                        
                        ##MOTOR FSM
                        ![](MOTFSM_3.png)
                        
                        ##USER FSM
                        ![](USERFSM_3.png)
                        
   @section task_3      3.TASK DIAGRAM
                        Since lab 3 builds off of lab 2, this task diagram 
                        only shows the newest shared variables that have been 
                        added since then.
                        ![](Task_3.png)
                        
   @section code_3      4.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Lab%203%20code/
    
      
   @page page_L4        LAB 0x04
   
   @section sec_sum4    1.OVERVIEW
                        In this lab, our goal was to impliment closed loop feedback
                        into our existing code in order to achieve speed control.
                        This was achieved by creating a closed loop driver class
                        and then implimenting the functions of this driver into
                        our existing tasks. We then tuned our controller by
                        performing multiple step responses with various gain
                        values and seeeingcwhich value provided the best response.
                        
   @section sec_test    2.TEST RESULTS
                        We decided to only impliment proportional gain in our
                        controller as it was the simplest to configure. In our
                        tests, we used a setpoint velocity of 30 rad/s and
                        used a range of gain values from 2-5. We found that at
                        Kp = 2, the motor was moving to slow to produce 
                        accurate data, and at Kp = 5 the motor was beging to 
                        oscillate to much. The best response was produced
                        at Kp = 4, as it settled very quicly and orovided a 
                        consistent steady state
                        
                        ![](KP2.png)
                        ![](KP3.png)
                        ![](KP4.png)
                        ![](KP5.png)
                        
   @section FSM_4       3.FINITE STATE MACHINES
                        Since lab 4 builds off of the previous two labs, this FSM
                        only contains the newest states that have been added since
                        then.
                        
                        ##USER FSM
                        ![](FSM_4.png)
                        
   @section task_4      4.TASK DIAGRAM
                        ![](Task_4.png)
    
   @section blcok_4     5.BLOCK DIAGRAM
                        We implimented our controller as was recommended by the block
                        shown below.
                        ![](Block_4.png)
                        
   @section code_4      6.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Lab%204%20code/
                        
   @page page_HW2       HW 0x02
   
   @section sec_1       1.SYSTEM LINKAGE KINEMATICS
                        In order to perform a dynamics analysis of the system, we first had to "unfurl"
                        the system by creating a 2D representation of the 3D system. The resulting schematic
                        is shown below, along with the assumptions that were made for our analysis.
                        
                        ![](TP_Linkage.jpg)
                        
                        This schematic was then used to develop a kinematic relationship 
                        between the motion of the motor about point A and the motion of 
                        the platform about point O as shown below.
                        
                        ![](TP_LKinematics.jpg)
                                          
   @section sec_2       2.BALL KINEMATICS
                        For this analysis, it was also essential that we be able to find
                        and expression for the motion of the ball. This was done by assuming
                        that the ball rolled without slip, and considering the motion caused
                        by the ball and platform moving together, as well as the motion of
                        the ball relative to the platform. The following calculations show the
                        derived expressions for the velocity and acceleration of the ball.
                        
                        ![](TP_BKinematics.jpg)
                        
   @section sec_3       3.LINKAGE KINETICS
                        A relationship between the motor torque for the first motor and the
                        corresponding effective moment applied to the platform was also 
                        derived for later use in the analysis. This was done by using the
                        method of virtual work in which we assumed that the system couldn't
                        store any energy due to its lack of mass. The calculations for this
                        analysis are shown below.
                        
                        ![](TP_LKinetics.jpg)

'''
        
        
        


