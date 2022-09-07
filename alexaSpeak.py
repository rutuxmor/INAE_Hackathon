# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 09:56:54 2022

@author: FactsgeniX
"""

#This function is used to pronounce or to give the output in a speech
def alexaSpeak(response):
     
    #using init() for initializing the engine
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()  