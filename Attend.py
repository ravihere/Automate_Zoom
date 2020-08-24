import pyautogui 
import schedule 
import time 
from datetime import datetime
import calendar
from classes import c1,c2,c3,c4
meettime=3000 #seconds for 50 min
def findDay(): 
    now=datetime.today().strftime('%Y-%m-%d')
    year,month,day=now.split("-")
    dayNumber = calendar.weekday(int(year), int(month), int(day)) 
    days =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return days[dayNumber]
def attendClass(id1,password,clas):
	print("You are Attending "+clas+" Class' Mate")
	time.sleep(0.1)
	pyautogui.press('esc',interval=0.06)
	time.sleep(0.08)
	pyautogui.press('win',interval=0.3)
	pyautogui.write('zoom')
	pyautogui.press('enter',interval=0.5)
	x,y = pyautogui.locateCenterOnScreen('join.png')
	pyautogui.click(x,y)
	pyautogui.press('enter',interval=5)
	pyautogui.write(id1)
	pyautogui.press('enter',interval=5)
	pyautogui.write(password)
	pyautogui.press('enter',interval=10)
	time.sleep(5)
	x,y = pyautogui.locateCenterOnScreen('NoVideo.PNG')
	pyautogui.click(x,y)
	time.sleep(30)
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.press('enter')	
	time.sleep(meettime)
	pyautogui.hotkey('alt','f4')
	time.sleep(1)
	pyautogui.click(1742,82)
	time.sleep(1)
	pyautogui.hotkey('alt','f4')

def Class1():
	day=findDay()
	id1=c1[day][0]
	password=c1[day][1]
	clas=c1[day][2]
	attendClass(str(id1),str(password),clas)
	
def Class2():
	day=findDay()
	id1=c2[day][0]
	password=c2[day][1]
	clas=c2[day][2]
	attendClass(str(id1),str(password),clas)

def Class3():
	day=findDay()
	id1=c3[day][0]
	password=c3[day][1]
	clas=c3[day][2]
	attendClass(str(id1),str(password),clas)

def Class4():
	day=findDay()
	id1=c4[day][0]
	password=c4[day][1]
	clas=c4[day][2]
	attendClass(str(id1),str(password),clas)
schedule.every().day.at("09:05").do(Class1)
schedule.every().day.at("10:05").do(Class2)
schedule.every().day.at("11:05").do(Class3)
schedule.every().day.at("12:05").do(Class4)
while True: 
	schedule.run_pending()
	time.sleep(1)
print("Press Ctrl+C to Abort' Mate")
