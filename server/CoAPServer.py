
from coapthon.server.coap import CoAP

from resources.BandwidthControllerResource import BandwidthControllerResource
from resources.BandwidthMonitoringResource import BandwidthMonitoringResource
from resources.BandwidthMeasurementResource import BandwidthMeasurementResource

__author__ = 'Cem Akpolat <akpolatcem@gmail.com>'

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.addResources()

    def addResources(self):
        # Bandwidth controller
        self.add_resource('bwController/', BandwidthControllerResource())
        self.add_resource('bwController/clear/', BandwidthControllerResource())
        self.add_resource('bwController/limit/', BandwidthControllerResource())
        # monitoring
        self.add_resource('bwMonitoring/', BandwidthMonitoringResource())
        self.add_resource('bwMonitoring/measure/', BandwidthMonitoringResource())
        self.add_resource('bwMonitoring/read/', BandwidthMonitoringResource())
        # measurement process
        self.add_resource('bwMeasurement/measure/', BandwidthMeasurementResource())
