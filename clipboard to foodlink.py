# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:44:42 2020

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
    pyautogui.write(str(val))
    pyautogui.PAUSE = .05
    if k<len(cb):
        pyautogui.press(['tab','tab','tab'], interval = .05)
    
