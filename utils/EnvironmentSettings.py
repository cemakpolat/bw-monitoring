import os
import platform
import subprocess

class EnvironmentSettings():
    def __init__(self):
        print "Environment preparation is started!"
    def checkWonderShaperInstalled(self):
        output = subprocess.check_output("which wondershaper", shell=True)
        if output.find("wondershaper"):
            print "Wondershaper is already installed"
        else:
            print "Wondershaper does not exist on the platform, it would be installed in seconds..."
            self.installWonderShaper()

    def installWonderShaper(self):
        linuxDistro = str(platform.dist())
        #print "Platform Distribution:" + str(platform.dist()[0])
        if (linuxDistro == 'debian' or linuxDistro == 'ubuntu'):
            os.system("sudo apt-get install wondershaper")
        elif (linuxDistro == 'fedora'):
            os.system("sudo yum install wondershaper")
        else:
            print "OS Distribution could not be detected, you may download the wondershaper script from github"