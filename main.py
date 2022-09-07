# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:12:17 2022

@author: FactsgeniX
"""

def main():
    response=invokeDevice()
    if(len(response)>1):
        result=implementDB()
        #alexaSpeak(result)
    else:
        output='Sorry, I do not know about this'
        alexaSpeak(output)
        invokeDevice()

main()