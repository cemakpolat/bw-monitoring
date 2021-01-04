
# Bandwidth Controller

The purpose of this program is to measure the bandwidth usage of the platform on which it is installed and dynamically decrease/increase the bandwidth usage of the network interfaces.
The taken measurement are transferred via the Python CoAP Server. In order to test the functionalities a firefox coap plugin is actively used. This plugin is not supported by the new firefox versions, please install firefox 55.0.3 or lower versions.   

## How to use

Start wondershaper with initial parameters

    coap://<target-IP>:10001/bwController/limit?netint=eth0&upload=1000&download=1000
    
- netint = network interface
- upload = KB/s
- download = KB/s

Start wondershaper with initial parameters with a specific duration, after 3 seconds wondershaper configuration will be removed
 
    coap://<target-IP>:10001/bwController/limit?netint=eth0&upload=1000&download=1000&duration=3
    
- duration = seconds   
 
Clear the wondershaper configuration written for the given interface

    coap://<target-IP>:10001/bwController/clear?netint=eth0
    
- netint = network interface

Start Bandwidth Monitoring using ifstat linux command  

    coap://<target-IP>:10001/bwMonitoring/measure?netint=eth0&wTime=1&mCount=2
    
- netint = network interface
- wTime = waiting Time for each taken measurement
- mCount = the number of the measurement to be taken

Read the  bandwidth monitorign measurement

    coap://<target-IP>:10001/bwMonitoring/read


## Environment
 
Test Environment: Linux Ubuntu
Required Tools: wondershaper, ifstat

    sudo apt-get install wondershaper trickle ifstat

## Used Libraries
 
### CoAP Python Library 

- https://github.com/Tanganelli/CoAPthon

### wondshaper

Rate Limit a Network Interface on Linux

- http://kb.bodhost.com/how-to-control-bandwidth-in-linux/

Usage:
    
    wondershaper <interface> <download-rate> <upload-rate>

Source Code: 

- https://github.com/magnific0/wondershaper

### ifstat:

Network bandwidth monitoring

Link:

    $ man ifstat

Usage:

    # ifstat -i etho <timeToBeWaited> <MeasurementCount>
    $ ifstat -t -i eth0 1 1 > bwmon.log

    Output:
    #Time    eth0
    #HH:MM:SS   KB / s IN  KB / s OUT
    #16:09:44        0.53     0.17

How to test:

    $ python BandwidthController.py

Open Firefox Coap Client and search for the published services:

    coap://<target-IP>:10001/bwController
    coap://<BandwidthController-IP Address>:10001/bwController 
  
### iperf.jar rest

TCP based bandwidth monitoring. It might be replaced with the original iperf command. The `iperf.jar` has nothing to do with `iperf` command. 
        coap://<target-IP>:10001/bwMeasurement
        
### iperf rest api


### d-itg rest api


