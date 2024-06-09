# Demo

from koch import *
import time

# Displays Koch snowflakes of stages 1 to 5, aligned at the window's centre (without animation)
for stage in range(6):
    draw_flake(stage, 729, align=True, fast=True, colour=2)

time.sleep(2)        # Waits for 2 seconds
turtle.clear()       # Clears the screen

# Displays Koch snowflakes of stages 4 to 1, aligned at the window's centre (with animation)
# Also cycles between the various colour modes
for stage in range(4):
    draw_flake(stage, 729, align=True, fast=False, colour=stage%3)
    time.sleep(0.8)
    turtle.clear()

turtle.mainloop()
