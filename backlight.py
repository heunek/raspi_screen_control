import socket
from rpi_backlight import Backlight
backlight =  Backlight()

UDP_IP = ''
UDP_PORT = 50007
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data == b'display_on':
        backlight.power = True
    if data == b'display_off':
        backlight.power = False
    if data == b'display_low':
        backlight.brightness = 10 oder 25
    if data == b'display_medium':
        backlight.brightness = 30 oder 50
    if data == b'display_high':
        backlight.brightness = 100 oder 75
