# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:18:26 2022

@author: FactsgeniX
"""

def invokeDevice():
    while True:
        # Exception handling to handle
        # exceptions at the runtime
        try:
         
            # use the microphone as source for input.
            with sr.Microphone() as input_source:
             
                # we are waiting for minimum time(only for a second) to let the recognizer
                # adjust the energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise(input_source, duration=0.2)
                 
                #listens for the user's input
                audio_captured = r.listen(input_source)
             
                # Using google to recognize audio
                invoking_Text = r.recognize_google(audio_captured, language="hi-In")
                invoking_Text = invoking_Text.lower()
                #print(invoking_Text)
 
                #calling the alexSpeak function
                if(invoking_Text=='namaste' or invoking_Text=='hello'):
                    print(invoking_Text)
                    result='Welcome to the voice assistant, Chessi'
                    alexaSpeak(result)
                    break
            break
        
        except sr.RequestError as e:
            output="Sorry, an unknown error occured, try again"
            alexaSpeak(output)
            invokeDevice()
         
        except sr.UnknownValueError:
            output="Sorry, an unknown error occured, try again"
            alexaSpeak(output)
            invokeDevice()
            
    return invoking_Text
