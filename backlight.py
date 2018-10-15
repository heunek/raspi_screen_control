import socket
import rpi_backlight as bl

UDP_IP = ''
UDP_PORT = 50007
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    if data == b'display_on':
        bl.set_power(True)
    if data == b'display_off':
        bl.set_power(False)
    if data == b'display_low':
        bl.set_brightness(20)
    if data == b'display_medium':
        bl.set_brightness(50)
    if data == b'display_high':
        bl.set_brightness(100)
