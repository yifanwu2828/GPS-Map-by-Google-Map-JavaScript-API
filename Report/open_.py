#This python3 version is deprecated, please use python_v2 now.
#This is a template code. Please save it in a proper .py file.
from rtmaps import*
import webbrowser
# Python class that will be called from RTMaps.
class rtmaps_python:

# Birth() will be called once at diagram execution startup
    def Birth(self):
        print("Python Birth")
        new = 2
        url='file:///home/image_processing/Desktop/rtmaps/web.html'
        webbrowser.open(url, new=new)
# Core() is called everytime you have a new input
    def Core(self):
        self.output_0 = self.input_0

# Death() will be called once at diagram execution shutdown
    def Death(self):
        pass
