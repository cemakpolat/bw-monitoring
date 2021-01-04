from coapthon.resources.resource import Resource
from features.BandwidthMeasurement import BandwidthMeasurement
__author__ = 'Cem Akpolat <akpolatcem@gmail.com>'

class BandwidthMeasurementResource(Resource):
    def __init__(self, name="BandwidthMeasurementResource", coap_server=None):
        super(BandwidthMeasurementResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.meaurement = BandwidthMeasurement()
        self.payload = "payload"
        # commands
        self.BWMeasurement = "bwMeasurement"
        self.MEASURE = "measure"

        self.ip = "127.0.0.1"
        self.port = "10101"
        self.time = "1"

    def hadle_query(self, query):
        qlist = query.split("&")
        for i in range(len(qlist)):
            tuple = qlist[i].split("=")
            if len(tuple) == 2:
                if tuple[0].find("ip") !=-1:
                    self.ip = tuple[1]
                elif tuple[0].find("port") !=-1:
                    self.port = tuple[1]
                elif tuple[0].find("time") !=-1:
                    self.time = tuple[1]
                else:
                    print "unknown query parameter is given!" + tuple[1]
            else:
                print "unknown query parameter is given!" + str(tuple)

        print self.ip + " " + self.port + " " + self.time

    #coap://<target-IP>:10001/bwMeasurement/measure?ip={ip}0&port={port}&time={ms}

    def render_GET(self, request):
        requestUriQuery= str(request.uri_query) # includes query parameters
        requestUriPath = str(request.uri_path)  # includes url path

        if requestUriPath.find(self.MEASURE) != -1:
            print "MEASURE command is called!"
            self.hadle_query(requestUriQuery)
            # just start the iperf jar
            self.meaurement.startMeasurement(self.ip, self.port, self.time)
        elif requestUriPath.find(self.BWMeasurement) != -1:
            self.payload = "URL Usage: <IP>:10001//bwMeasurement/measure?ip={ip}0&port={port}&time={ms}"
            self.payload = self.payload +"\n" + "ip address = ip, port number = port, time in ms"
            self.payload = self.payload + "\n" + "Example Start with duration: coap://<target-IP>:10001/bwMeasurement/measure?ip=127.0.0.1&port=10101&time=1"
        else:
            print "Unknown Command!"

        return self
