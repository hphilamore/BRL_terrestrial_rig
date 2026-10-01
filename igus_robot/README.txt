Python script XXX.Python

''' Program description + which values to change to personalse the program'''



______________________________________________________________________________________
The D1 motor driver modules can also be accessed via IP address in a web browser
Vertical axis D1 - IP 169.254.246.71
Horizontal axis D1 - IP 169.254.204.71

DO NOT change the D1 motor driver settings before discussing with Hemma Philamore hemma.philamore@bristol.ac.uk!

To update update D1 parameters:
Communication --> Modbus TCP Gateway = OFF
Inputs/outputs --> Enable (DI7) = OFF 
Update any parameters

Then, before controlling the D1 via TCP Gateway (e.g. Python script run over ethernet)
Drive Profile ---> Select Modbus TCP Gateway
Inputs/outputs --> Enable (DI7) = ON
Communication --> Modbus TCP Gateway = ON

