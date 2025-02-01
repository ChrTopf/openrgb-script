# OpenRGB Script

This script was written for my system which consists of a RGB motherboard and the Logitech G502 Lightspeed Mouse. The problem which i have been experiencing was, that the mouse was not able to recover its lighting settings set by openrgb on system startup or mouse wakeup from standby mode. Aditionally, my motherboard lighting did not recover after system wakeup from standby as well.

This simple script solves these problems by applying a hardcoded primary color every 10 seconds via the OpenRGB SDK for python.
