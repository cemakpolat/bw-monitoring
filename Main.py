from server.CoAPServer import CoAPServer
from utils.EnvironmentSettings import EnvironmentSettings
import os
__author__ = 'Cem Akpolat <akpolatcem@gmail.com>'

def main():
    # check environment settings
    env = EnvironmentSettings()
    env.checkWonderShaperInstalled()

    # start coap server
    server = CoAPServer("0.0.0.0", 10001)

    try:
        server.listen(10)
    except KeyboardInterrupt:
        print "Server Shutdown"
        server.close()
        print "Exiting..."

if __name__ == '__main__':
    main()
