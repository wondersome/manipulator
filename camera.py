

from picamera import PiCamera
from time import sleep

def scheme():
    camera = PiCamera()
    camera.start_preview()
    camera.capture('scheme.jpg')
    camera.stop_preview()
    camera.close()
def blocks35():
    camera = PiCamera()
    camera.start_preview()
    camera.capture('35.jpg')
    camera.stop_preview()
    camera.close()
def blocks13():
    camera = PiCamera()
    camera.start_preview()
    camera.capture('13.jpg')
    camera.stop_preview()
    camera.close()
