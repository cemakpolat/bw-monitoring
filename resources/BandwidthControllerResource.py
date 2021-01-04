from coapthon.resources.resource import Resource
from features.BandwidthController import BandwidthController

__author__ = 'Cem Akpolat <akpolatcem@gmail.com>'

class BandwidthControllerResource(Resource):
    def __init__(self, name="BandwidthControllerResource", coap_server=None):
        super(BandwidthControllerResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.controller = BandwidthController()
        self.currentBandwidth = 0
        self.payload = "payload" # This is important, since coap client would receive the message in payload
        #self.resource_type = "rt1"
        #self.content_type = "text/plain"
        #self.interface_type = "if1"

        # commands
        self.BWController = "bwController"
        self.CLEAR = "clear"
        self.LIMIT = "limit"
        # parameters
        self.netint = ""
        self.upload = ""
        self.download = ""
        self.duration = 0

    def hadle_query(self, query):
        qlist = query.split("&")
        print qlist
        for i in range(len(qlist)):
            tuple = qlist[i].split("=")
            print tuple
            if len(tuple) == 2:
                if tuple[0].find("netint") !=-1:
                    self.netint = tuple[1]
                elif tuple[0].find("upload") !=-1:
                    self.upload = tuple[1]
                elif tuple[0].find("download") !=-1:
                    self.download = tuple[1]
                elif tuple[0].find("duration") !=-1:
                    self.duration = tuple[1]
                else:
                    print "unknown query parameter is given!" + tuple[1]
            else:
                print "unknown query parameter is given!" + str(tuple)

        print self.netint + " " + self.upload + " " + self.download

    #coap://<target-IP>:10001/bwController/limit?netint=eth0&upload=1000&download=1000&duration=1s
    # coap://<target-IP>:10001/bwController/limit?netint=eth0&upload=1000&download=1000

    def render_GET(self, request):
        requestUriQuery= str(request.uri_query) # includes query parameters
        requestUriPath = str(request.uri_path)  # includes url path
        if requestUriPath.find(self.CLEAR) != -1:
            print "CLEAR command is called!"
            self.hadle_query(requestUriQuery)
            self.controller.clearWondershaper(self.netint)
        elif requestUriPath.find(self.LIMIT) != -1:
            print "LIMIT command is called!"
            self.hadle_query(requestUriQuery)
            if self.duration > 0:
                # calling with duration or without duration
                try:
                    self.controller.wondershaperWithDuration(self.netint,self.upload, self.download, self.duration)
                    self.payload = "wondershaper tread is started, and it will stop in " + self.duration +"s"
                except:
                    print "Command not found!"
            else:
                try:
                    self.controller.wondershaper(self.netint, self.upload, self.download)
                    self.payload = "wondershaper is started"
                except:
                   print "Command not found!"
        elif requestUriPath.find(self.BWController) != -1:
            self.payload = "URL Usage: <IP>:10001/bwController/limit?netint=eth0&upload=<KB>&download=<KB>&duration=<s>"
            self.payload = self.payload +"\n" + "network interface = netint, upload in KB, download in KB, duration in seconds"
            self.payload = self.payload + "\n" + "Example Start with duration: coap://<target-IP>:10001/bwController/limit?netint=eth0&upload=1000&download=1000&duration=1s"
            self.payload = self.payload + "\n" + "Example Start: coap://<target-IP>:10001/bwController/limit?netint=eth0&upload=1000&download=1000"
            self.payload = self.payload + "\n" + "Example Clear: coap://<target-IP>:10001/bwController/clear?netint=eth0"
        else:
            print "Unknown Command!"

        return self
