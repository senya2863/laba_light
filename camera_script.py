from time import sleep
from picamera import PiCamera

camera=PiCamera()
camera.brightness=53

camera.start_preview()
sleep(2)
camera.capture("green.png")

camera.resolution=(1280,720
)
camera.contrast=10
