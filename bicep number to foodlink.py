# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:42:12 2020

@author: JWeiz
"""

import pyautogui
from pandas import read_clipboard

cb = read_clipboard(header = None)

pyautogui.PAUSE = .05
pyautogui.hotkey('alt', 'tab')

for k in range(0,len(cb)):
    #print(k)
    val = cb.iloc[k][0]
    
    leadzeronum = 0
    
    if len(str(val))<6:
        leadzeronum = 6-len(str(val))
     
    val = str('0'*leadzeronum) + str(val)
    
    pyautogui.write(val)
    pyautogui.PAUSE = .05
    if k<len(cb):
        pyautogui.press(['tab','tab','tab'], interval = .05)
    
