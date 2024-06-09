# Generating Koch snowflakes using Python's turtle module
<br>

## Contents of files

- `koch.py` : functions to generate the snowflakes, with options such as toggling animation and alignment
- `main.py` : some code I wrote to demonstrate the functions
<br>

## How to use

Import contents of `koch.py` using either of the following:
```python
from koch import *     # functions can be called directly
import koch            # functions need to be called as attributes to koch
```
<br>

You're ready to use the functions now.
There are 3 functions available for use:
- `koch`
- `draw_segment`
- `draw_flake`

All of them rely on each other. `draw_segment` calls `koch`, and `draw_flake` calls `draw_segment`, thus calling `koch`
<br>

### `koch`

\>>> SYNTAX:
```python
koch(stage, length)
```
<br>

`koch` is the most fundamental of the three functions. It implements recursion to draw a segment (think of a line of a stage-0 flake - an equilateral triangle) of the (total horizontal) length `length` pixels, and levels of recursion equal to `stage`. <br>

During the recursion step, the `length` passed to the function is divided by 3 and passed to another call of `koch` for generating the flake of stage `stage-1`. In some cases, the new `length` passed might be a value less than 1, which will end up doing nothing. This prints a warning to the console. <br>

This might be desired in some cases, so a mere warning is printed, rather than an exception being raised.
<br>

### `draw_segment`

\>>> SYNTAX:
```python
draw_segment(stage, length, align=False, fast=False)
```
<br>

`draw_segment` exists to enable some initialization before handing it over to `koch` to display the actual segment. `align` and `fast` are arguments that are optional to pass, and have default values of `False`. <br>

If the `align` parameter is set to `True`, the displayed segment is "horizontally symmetric about the turtle's current position", horizontal here referring to the direction that the turtle points in. For example, if `turtle.home()` is called to reset the turtle's position and orientation, and then `draw_segment` is called with `align=True`, the segment generated is symmetrical about the "y-axis". After the alignment, the turtle's position is reverted to where it was before `draw_segment`'s call. <br>

If the `fast` parameter is set to `True`, the turtle's tracer is turned off during the duration of the generation, to enable a faster generation. Use this when you don't care about the animation and just want the image.
<br>

### `draw_flake`

\>>> SYNTAX:
```python
draw_flake(stage, length, align=False, fast=False)
```
<br>

`draw_flake` is responsible for generating an actual Koch snowflake. It has the same argument list as `draw_segment` and he parameters mean the same that they did for that function. Only the `align` parameter's functionality has changed. <br>

If `align` is set to `True`, the turtle's current position will be the centroid of the generated flake and post-generation, the turtle will revert back to it's original position.

<br>

## Outputs

<br>

![image](https://github.com/rajdeep-314/koch_snowflake/assets/160480035/69169916-0149-48eb-a213-34c260c48312)
<p align="center"> Stage-1 segment generated using draw_segment </p> <br>

![image](https://github.com/rajdeep-314/koch_snowflake/assets/160480035/736efca3-7b56-4056-86d3-4425a880da8f)
<p align="center"> Stage-2 segment generated using draw_segment </p> <br>

![image](https://github.com/rajdeep-314/koch_snowflake/assets/160480035/87ecd2f4-12e2-43a9-bf4e-92fade99361a)
<p align="center"> Stage-3 segment generated using draw_segment </p> <br>

![image](https://github.com/rajdeep-314/koch_snowflake/assets/160480035/3e2c8e73-73fc-494f-afd4-6a645c62e883)
<p align="center"> Stage-4 segment generated using draw_segment </p> <br>

![Stage-6 snowflake](https://github.com/rajdeep-314/koch_snowflake/assets/160480035/7cd3d8d6-7861-4175-82e4-62e953522ea9)
<p align="center"> Stage-6 snowflake generated using draw_flake </p> <br>
