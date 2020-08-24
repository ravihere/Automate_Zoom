# Automate_Zoom
Automatically attend your scheduled meetings on time

# Prerequisites
* python3
# For Windows
## Installation
* Download zip file and put your files in these path,
    _C:\Users\username\Desktop\_
    
* Open cmd in windows, follow below procedure

To install PYAUTOGUI:

      pip install pyautogui

To install SCHEDULE:

      pip install schedule
      
To run the code, open cmd and go to the path where source code is located and enter:

    _C:\Users\username\Desktop\Automate_Zoom> python Attend.py
    
*_you have to execute code atleast 1 min before specified time_

That's All!!!
It will automatically join n leave classes by following timetable or schedule

*_Extensions and changes are applicable, if any_

## For Linux

* Create a shortcut icon for zoom and place it on desktop
* In Attend.py, replace the code from 17 line to 21 line as

        x,y = pyautogui.locateOnScreen('zoomicon.png')
	    pyautogui.click(x,y)
       
* Before, that take a snap of zoom icon and save it on folder where source code is located
* Make sure the hotkey functions(keyboard shorcuts) and apply changes, if any at line 37 and 41 in Attend.py accordingly
* That's All!!
