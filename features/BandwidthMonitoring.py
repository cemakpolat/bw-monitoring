import time
import os
import json

__author__ = 'Cem Akpolat <akpolatcem@gmail.com>'

def execute_command(threadName, delay, duration, startcommand, stopcommand):
    os.system(startcommand)  # run the command
    print "execute command:"+duration
    count = 0
    while count < int(duration):
       time.sleep(delay)
       count += 1
       print     "%s: %s" % ( threadName, time.ctime(time.time()) )

    if stopcommand != "":
        os.system(stopcommand)

class BandwidthMonitoring():
    def __init__(self):
        print "Bandwidth Monitoring is started!"

    def startMonitoring(self, interface, waitingTime, measurementCount):
        # ifstat -i etho <timeToBeWaited> <MeasurementCount>
        os.system("ifstat -t -i "+interface+" "+waitingTime+" "+ measurementCount+" > bwmon.log")
        #os.system("ifstat -t -i eth0 1 1 > bwmon.log")


    # Measurement Result
    #Time    eth0
    #HH:MM:SS   KB / s in  KB / sout
    #16:09:44        0.53     0.17
    def readMeasurements(self):
        i = 0
        f = ""
        try:
            f = open("bwmon.log", "r")  # opens file with name of "test.txt"
        except:
            print "file openning exception!"

        data = {}
        data['people'] = []
        data['people'].append({
            'name': 'Scott',
            'website': 'stackabuse.com',
            'from': 'Nebraska'
        })
        data = {}
        myList = []
        for line in f:
            if i > 1 : # first two are header are removed
                myList = line.split() # time, in, out
                data[myList[0]]= {'upload': myList[2], 'download':  myList[1]}
            i = i + 1
        #print(json.dumps(data))
        return json.dumps(data)
