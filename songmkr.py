# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:16:32 2020

@author: Dhondi Sai Ganesh
"""


from gtts import gTTS
from playsound import playsound 
audio='speech3.mp3'
language='en'
sp=gTTS(text="Mummuy oh my dear mummy murkuluu baanana mummy!",lang=language,slow=False)
sp.save(audio)
playsound(audio) 