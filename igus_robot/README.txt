Python script XXX.Python

''' Program description + which values to change to personalse the program'''



______________________________________________________________________________________
DO NOT change the D1 motor driver settings before discussing with Hemma Philamore hemma.philamore@bristol.ac.uk!

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

