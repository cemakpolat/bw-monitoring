import os
import thread
import time
import utils.Utilities

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


class BandwidthController():
    def __init__(self):
        self.threadId = 0
        print "Bandwidth Controller is started!"

    def measureCurrentBanwidth(self):
        print "Bandwidth is being measured..."

    def changeBandwidthAmount(amount):
        print "Wondershader is called"
        print "Trickle is called..."

    # Rate Limit a Network Interface on Linux
    def wondershaper(self, interface, download, upload):
        # wondershaper <interface> <download-rate> <upload-rate>
        try:
            command = "sudo wondershaper "+ interface +" "+ download +" "+ upload
            os.system(command)
            #os.system  ('sudo wondershaper eth0 8192 1600')
        except:
            print "command not found"

    def wondershaperWithDuration(self, interface, download, upload, duration):
        try:
            start_wonder_shaper = "sudo wondershaper "+ interface +" "+ download +" "+ upload
            clear_wonders_shaper = "sudo wondershaper clear " + interface

            #thread1 = WonderShaperThread(self.threadId + 1, "Thread-" + self.threadId + 1, duration, command)
            #thread1.start()
            delay  = 1
            thread.start_new_thread(execute_command, ("Thread-1",delay, duration,start_wonder_shaper,clear_wonders_shaper))

        except:
            print "Error: unable to start thread"

    def clearWondershaper(self, interface):
        try:
            os.system('sudo wondershaper clear eth0')
            print "clear wondershaper is called"
        except:
            print "command not found"
