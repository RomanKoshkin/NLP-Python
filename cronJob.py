""""This is the cronjob code to copy and paste data multiple times into a website"""

import pyautogui
import time
from tkinter import Tk

pyautogui.size()
symbols = 	(u"ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю",
             u"qwertyuiop[]asdfghjkl;’zxcvbnm,.qwertyuiop[]asdfghjkl;’zxcvbnm,.")


tr = {ord(a):ord(b) for a, b in zip(*symbols)}      # ЭТО КАК ПОНИМАТЬ?

q = []
out = []
count = []

inFile = open('lemmasRus_unique.txt', 'r')
for j in inFile.readlines():
    q.append(j.replace('\n', ''))
inFile.close()



for count in range(1, len(q)):
    r = Tk()

    pyautogui.moveTo(146, 138, duration=0.25)
    pyautogui.click(button='left', clicks=2)

    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('command')
    pyautogui.press('right')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('command')
    pyautogui.press('backspace')

    pyautogui.typewrite((q[count]).translate(tr))
    pyautogui.press('enter')

    time.sleep(10)


    pyautogui.moveTo(147, 319, duration=0.1)
    #pyautogui.click(button='left', clicks=2, interval=0.15)
    pyautogui.dragTo(405, 319, button='left')

    pyautogui.keyDown('command')
    pyautogui.press('c')
    pyautogui.keyUp('command')

    out.append(r.clipboard_get())
    f_out = open('cronOut.txt', 'a')
    f_out.write(str(count) + '\t' + out[-1] + '\n')
    f_out.close()

print('end')