# raspi_screen_control
Controls the 7" Touch Screen of a Raspberry Pi with UDP-Packets sent from edomi

Based on a telegram of a motiondetector edomi sends a UDP paket with the content "display_on" for activation and "display_off" for the deactivation of the Touch Screen.
Additionally will edomi send a udp package based on the brightness.

On receipt of the UDP package the python application will control the touch screen with the help of the module "rpi_backlight" (https://pypi.org/project/rpi_backlight/).

Prerequisites:
$ pip3 install rpi-backlight

Install:

copy backlight.service file to /etc/systemd/system/
copy backlight.py to /opt/backlight
chmod +x /opt/backlight.py
systemctl enable backlight
systemctl start backlight

