"""
File: 
Name:James
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Global
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global
window = GWindow(800, 500, title='bouncing_ball.py')
oval = GOval(SIZE, SIZE, x=START_X, y=START_Y)
oval.filled = True
window.add(oval)
dy = 0
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(animation)


def animation(mouse):
    global dy, count
    while True:
        if count == 3:
            break
        oval.move(VX, dy)  # move ball
        dy += GRAVITY  # simulated gravitational acceleration

        # check if ball touch bottom
        if oval.y + oval.height > window.height:
            oval.y = window.height - oval.height  # put the ball at the bottom edge
            dy = -dy * REDUCE  # reverse the vertical velocity and reduce its magnitude

        # check if the ball exceeds the right boundary
        if oval.x > window.width:
            oval.x = START_X
            oval.y = START_Y
            dy = 0  # reset the vertical velocity
            count += 1
            break
        pause(DELAY)


if __name__ == "__main__":
    main()