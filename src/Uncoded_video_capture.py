import picamera
import numpy as np
from picamera.array import PiRGBAnalysis
from PIL import Image
from scipy.ndimage import gaussian_filter1d

class MyColorAnalyzer(PiRGBAnalysis):
    def __init__(self, camera):
        super(MyColorAnalyzer, self).__init__(camera)
        self.n = 0
    def analyze(self, a):
        self.n = self.n + 1
        if self.n == 1:
           img = Image.fromarray(a)
           img.save('test_07.png')
        #Generating a line sensor   
        line = a[50,:,1]
        filteredline = gaussian_filter1d(line, 5)
        print(np.argmin(filteredline))
        #--------------------------------------------
        #s = np.reshape(line,(16,10))
        #print(np.mean(s, axis=1))        
with picamera.PiCamera(resolution='160x96', framerate=200) as camera:
    # Fix the camera's white-balance gains
    camera.awb_mode = 'off'
    camera.awb_gains = (1.4, 1.5)
    # Construct the analysis output and start recording data to it
    with MyColorAnalyzer(camera) as analyzer:
        camera.start_recording(analyzer, 'rgb')
        try:
            #while True:
            camera.wait_recording(10)
        finally:
            camera.stop_recording()
        print(analyzer.n)