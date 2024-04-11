import time
import picamera
import numpy as np
#import iso

with picamera.PiCamera() as camera:
    camera.sensor_mode = 7
    camera.sensor_mode = 7
    camera.framerate = 120
    camera.resolution = (640, 480)
    
    #camera.iso = 1600
    camera.exposure_mode = 'off'
    camera.shutter_speed = 5000
    #--------------------------------------------
    time.sleep(2)
    
   
    #camera.sensor_mode = 
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
     
    
    
    # Wait for the automatic gain control to settle
    
    # Now fix the values
    #camera.shutter_speed = camera.exposure_speed
    
    
    
    # Finally, take several photos with the fixed settings
    #camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
    #frames = 100 # number of frames
    output = np.empty((480, 640, 3), dtype=np.uint8)
    timestamp = []
    start = time.time()
    for i in range(100):
        timestamp.append(time.time() - start)
        camera.capture(output, 'rgb')

