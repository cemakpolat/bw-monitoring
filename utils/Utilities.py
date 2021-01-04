import os
import time

__author__ = 'Cem Akpolat <cem.akpolat@gt-arc.com>'

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

