from coapthon.resources.resource import Resource
from features.BandwidthMonitoring import BandwidthMonitoring

__author__ = 'Cem Akpolat <akpolatcem@gmail.com>'


class BandwidthMonitoringResource(Resource):
    def __init__(self, name="BandwidthMonitoringResource", coap_server=None):
        super(BandwidthMonitoringResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.monitoring = BandwidthMonitoring()
        self.currentBandwidth = 0
        self.payload = "payload" # This is important, since coap client would receive the message in payload

        # commands
        self.READ = "read"
        self.MEASURE = "measure"
        self.BWMonitoring ="bwMonitoring"

        # parameters
        self.netint = "eth0"
        self.waitingTime = "1"
        self.measurementCount = "1"

    def hadleQuery(self, query):
        qlist = query.split("&")
        for i in range(len(qlist)):
            tuple = qlist[i].split("=")
            if len(tuple) == 2:
                if tuple[0].find("netint") !=-1:
                    self.netint = tuple[1]
                elif tuple[0].find("wTime") !=-1:
                    self.waitingTime = tuple[1]
                elif tuple[0].find("mCount") !=-1:
                    self.measurementCount = tuple[1]
                else:
                    print "unknown query parameter is given!" + tuple[1]
            else:
                print "unknown query parameter is given!" + str(tuple)

    def render_GET(self, request):
        requestUriQuery= str(request.uri_query)
        requestUriPath = str(request.uri_path)
        if requestUriPath.find(self.READ) != -1:
            self.payload = self.monitoring.readMeasurements()
        elif requestUriPath.find(self.MEASURE) != -1:
            print "Monitoring is started!"
            self.hadleQuery(requestUriQuery)
            try:
                self.monitoring.startMonitoring(self.netint, self.waitingTime, self.measurementCount)
                self.payload = "bandwidth monitoring is started..." # found a logical response
            except:
                print "Command not found!"
        elif requestUriPath.find("bwMonitoring") != -1:

            self.payload = "URL Usage: <IP>:10001/bwMonitoring/start?netint=eth0&wTime=1&mCount=1"
            self.payload = self.payload + "netint = network interface, wTime = time to be waiter for each measurement, mCount= number of measurement"
            self.payload = self.payload + "Example: <target-IP>:10001/bwMonitoring/start?netint=eth0&wTime=10&mCount=5"
            self.payload = self.payload + "Example: <target-IP>:10001/bwMonitoring/read"

        else:
            print "Unknown Command!"

        return self