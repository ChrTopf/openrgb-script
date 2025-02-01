from time import sleep
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
import signal
import sys

# initialize the interrupt signal handler
def signal_handler(sig, frame):
    print('This routine was interrupted by a system signal!', flush=True)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# wait until open rgb server must be ready
sleep(30)

# define the primary color
primary = RGBColor(255, 0, 0)

# create the openrgb client
client = OpenRGBClient()
# Turns everything off
client.clear()
# set the motherboard to the configured color
motherboard = client.get_devices_by_type(DeviceType.MOTHERBOARD)[0]
motherboard.set_color(primary)
print(f"The motherboard {motherboard.name} was initialized with the primary color.", flush=True)

mouse = client.get_devices_by_type(DeviceType.MOUSE)[0]
print(f"The following mouse is going to be controlled: {mouse.name}", flush=True)

while True:
    mouse.set_mode("static")
    mouse.zones[0].set_color(primary)
    mouse.zones[1].set_color(RGBColor(0, 0, 0))
    sleep(10)

