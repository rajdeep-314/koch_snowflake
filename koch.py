# Convention:
# Stage 0 : ____
# Stage 1 : _/\_

import turtle
import math

# To keep track of whether lengths are being diluted to zero
_dilution_warning = False

# Initializing visual parameters
turtle.bgcolor('black')
turtle.color('white')
turtle.hideturtle()
turtle.speed(10)


# Draws a "segment" of the snowflake
# length : total horizontal length of the final structure
def koch(stage, length):
    # Base case
    if stage == 0:
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
        koch(prev_stage, prev_length)
        turtle.lt(60)
        koch(prev_stage, prev_length)
        turtle.rt(120)
        koch(prev_stage, prev_length)
        turtle.lt(60)
        koch(prev_stage, prev_length)


# Helper function to pass some parameters before drawing the segment
# align=True -> The generated structure will be symmetrical about the turtle's current position, along the turtle's current direction
def draw_segment(stage, length, align=False, fast=False):
    if fast:
        turtle.tracer(0)
    # Initializing position for alignment
    if align:
        turtle.teleport(x=turtle.pos()[0] - length/2)

    koch(stage, length)
    
    # Returning to original position post-alignment
    if align:
        turtle.teleport(x=turtle.pos()[0] + length/2)
    if fast:
        turtle.tracer(1)


# Draws the koch flake with the given parameters
# align=True -> the current postion becomes the flake's centroid
def draw_flake(stage, length, align=False, fast=False):
    # Initializing position for alignment
    if align:
        current_pos = turtle.pos()
        turtle.teleport(current_pos[0] - length/2, current_pos[1] + math.sqrt(3)*length/6)

    # Generating the flake
    for i in range(3):
        draw_segment(stage, length, align=False, fast=fast)
        turtle.rt(120)

    # Returning to original position post-alignment
    if align:
        turtle.teleport(*current_pos)
