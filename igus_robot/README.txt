--------------------------- SAMPLE CODE -------------------------------------------------

Python script xy_gantry_sample_program.py

Dual axis control for point to point movement and 2 axis gantry robot
All movement parameter can be adopted. E.g. speed, acceleration or position.


--------------------------- D1 MOTOR DRIVER SETTINGS --------------------------------------
DO NOT change the D1 motor driver settings before discussing with Hemma Philamore! 
(hemma.philamore@bristol.ac.uk)

To update the D1 motor driver settings: 

1. Access the D1 motor driver module settings page by pasting the IP address of each motor into a web browser
Vertical axis D1 - IP 169.254.246.71
Horizontal axis D1 - IP 169.254.204.71

2. To update D1 settings:
Communication --> Modbus TCP Gateway = OFF
Inputs/outputs --> Enable (DI7) = OFF 
Update settings

3. After changing settings, before reattempting to control the D1 via TCP Gateway (e.g. Python script run over ethernet)
Drive Profile ---> Select Modbus TCP Gateway
Inputs/outputs --> Enable (DI7) = ON
Communication --> Modbus TCP Gateway = ON

