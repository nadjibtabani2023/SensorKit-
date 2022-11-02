#!/usr/bin/python
# coding=utf-8
 
# Les modules nécessaires sont importés et mis en place
import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
   
# La broche d'entrée du capteur est déclarée. En outre la résistance de Pull-up est activée.
GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
   
print("Sensor-Test [Appuyez sur Ctrl + C pour terminer le test]")
   
# Cette fonction de sortie est exécutée par détection du signal
def fonctionDeSortie(null):
        print("Signal détecté")
   
# Lors de la détection d'un signal (front descendant du signal) de la fonction de sortie est déclenchée
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=fonctionDeSortie, bouncetime=100) 
   
# Boucle de programme principale
try:
    while True:
        time.sleep(1)
   
# réinitialisation de tous les GPIO en entrées
except KeyboardInterrupt:
    GPIO.cleanup()
