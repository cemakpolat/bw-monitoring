import time
import os
import json

__author__ = 'Cem Akpolat <akpolatcem@gmail.com>'

class BandwidthMeasurement():
    def __init__(self):
        print "Bandwidth Measurement is started!"

    def startMeasurement(self, ip, port, time):
        os.system("java -jar ../iperf.jar -c -h "+ip+" -p "+port+" -t "+time)
        #os.system("java -jar iperf.jar -c -h 127.0.0.1 -p 10101 -t 1")
