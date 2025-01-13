"""
Name:James
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GOval
SIZE = 10

# Global
window = GWindow()
circle = None
first_click_point = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(mouse_click_motion)


def mouse_click_motion(event):
    global circle, first_click_point

    # If this is the first click, draw the circle
    if first_click_point is None:
        first_click_point = [event.x, event.y]
        circle = GOval(SIZE, SIZE, x=event.x, y=event.y)
        window.add(circle)

    # If this is the second click, remove the circle and draw the line
    else:
        window.remove(circle)
        line = GLine(first_click_point[0], first_click_point[1], event.x, event.y)
        window.add(line)
        # Reset for the next pair of clicks
        first_click_point = None


if __name__ == "__main__":
    main()
