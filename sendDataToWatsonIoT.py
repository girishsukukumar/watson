import time
import sys
import uuid
import argparse
import ibmiotf.device
import random
def myOnPublishCallback():
                print("Confirmed event %s received by IoTF\n" % x)
# org ID : o0gnpk

if  __name__  == "__main__":
   deviceOptions = {"org": "myOrg345678",  # Take this value from Watson Console (top right corener)
                    "type": "TestType"
                    "id": "TestDevice"
                    "auth-method": "token",
                    "auth-token": "mytoken123"} # Take this value from Device

   print(deviceOptions)
   deviceCli = ibmiotf.device.Client(deviceOptions)
   print(deviceCli)
   deviceCli.connect()
   x = 2.3
   for i in  range(100):

     x = x + random.random()

     data = { 'simpledev' : 'ok', 'x' : x}
     print x
     success = deviceCli.publishEvent("turb", "json", data, qos=0, on_publish=myOnPublishCallback)
     if not success:
                print("Not connected to IoTF")

     time.sleep(1)


   # Disconnect the device and application from the cloud
   deviceCli.disconnect()
