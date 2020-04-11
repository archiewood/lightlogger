#!/usr/bin/env python
# coding: utf-8

# In[90]:


# CamJam EduKit 2 - Sensors
# Worksheet 4 - Light

# Import Libraries
import time
import RPi.GPIO as GPIO
import datetime
import csv


# In[141]:


# Set the GPIO Mode and set the pin to use for the
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# A variable with the LDR reading pin number
pinldr = 27


def readldr():
    ldrcount = 0  # Sets the count to 0
    GPIO.setup(pinldr, GPIO.OUT)
    GPIO.output(pinldr, GPIO.LOW)
    time.sleep(0.1)  # Drains all charge from the capacitor

    GPIO.setup(pinldr, GPIO.IN)  # Sets the pin to be input
    # While the input pin reads 'off' or Low, count
    while (GPIO.input(pinldr) == GPIO.LOW):
        ldrcount += 1  # Add one to the counter
    
    entry = [datetime.datetime.now(),1000/ldrcount]
    
    return entry


# In[111]:


#entry = [datetime.datetime.now(),1000/readldr()]

#print(entry)


# In[149]:


file = open('lightlog.csv', 'a')


with file:
    writer = csv.writer(file)
    
    writer.writerow(readldr())
    

