# Convention:
# Stage 0 : ____
# Stage 1 : _/\_

import turtle
import math
from colorsys import hsv_to_rgb

# To keep track of whether lengths are being diluted to zero
_dilution_warning = False

# Initializing visual parameters
turtle.bgcolor('black')
turtle.color('white')
turtle.hideturtle()
turtle.speed(10)
turtle.width(2)

# Draws a "segment" of the snowflake
# length : total horizontal length of the final structure
# colour -> 0: no colouring; 1: grayscale colouring; 2: weird HSV-based colouring
def koch(stage, length, colour=0):
    # Base case
    if stage == 0:
        if color == 0:
            turtle.color(0, 0, 0)
        elif colour == 1:     # Grayscale colouring
            k_factor = 0.1
            colour_ = k_factor + (1-k_factor)*abs(turtle.heading() - 180)/180
            turtle.color(*[colour_]*3)
        elif colour == 2:   # HSV-based colouring
            k_factor = 0.1
            hsv_colour = k_factor + (1-k_factor)*abs(turtle.heading() - 180)/180
            rgb_colour = hsv_to_rgb(hsv_colour, 1, 1)
            turtle.color(*rgb_colour)
        turtle.fd(length)
    else:
        prev_stage = stage - 1
        prev_length = length/3

        # Checks for dilution
        global _dilution_warning
        if prev_length < 1 and _dilution_warning == False:
            print("Warning: lengths are being diluted")
            _dilution_warning = True

        # Implementing recursion
        koch(prev_stage, prev_length, colour=colour)
        turtle.lt(60)
        koch(prev_stage, prev_length, colour=colour)
        turtle.rt(120)
        koch(prev_stage, prev_length, colour=colour)
        turtle.lt(60)
        koch(prev_stage, prev_length, colour=colour)


# Helper function to pass some parameters before drawing the segment
# align=True -> The generated structure will be symmetrical about the turtle's current position, along the turtle's current direction
def draw_segment(stage, length, align=False, fast=False, colour=0):
    if fast:
        turtle.tracer(0)
    # Initializing position for alignment
    if align:
        turtle.teleport(x=turtle.pos()[0] - length/2)

    koch(stage, length, colour=colour)
    
    # Returning to original position post-alignment
    if align:
        turtle.teleport(x=turtle.pos()[0] + length/2)
    if fast:
        turtle.tracer(1)


# Draws the koch flake with the given parameters
# align=True -> the current postion becomes the flake's centroid
def draw_flake(stage, length, align=False, fast=False, colour=0):
    # Initializing position for alignment
    if align:
        current_pos = turtle.pos()
        turtle.teleport(current_pos[0] - length/2, current_pos[1] + math.sqrt(3)*length/6)

    # Generating the flake
    for i in range(3):
        draw_segment(stage, length, align=False, fast=fast, colour=colour)
        turtle.rt(120)

    # Returning to original position post-alignment
    if align:
        turtle.teleport(*current_pos)
