import math
from turtle import *

# Define the parametric mathematical equations for the heart shape
def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# Setup window and drawing parameters
speed(0)                # Set animation speed to maximum
bgcolor("black")        # Set the background color to black
color("#f73487")        # Custom pink hex color seen in the animation
pensize(1)              # Thin lines for a smooth, high-density pattern

# Draw the radiating pattern from the center
for i in range(600):
    goto(0, 0)          # Always return to the center to create radiating lines
    # Calculate the scale factor and position for each step
    x = heart_x(i) * 15
    y = heart_y(i) * 15
    goto(x, y)          # Draw the line out to the calculated heart boundary

hideturtle()            # Hide the cursor after finishing
done()                  # Keep the window open
