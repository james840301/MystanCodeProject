"""
File: lemon.png
Name: James
----------------------
Title: Mr. Lemon

This is my friend Mr. Lemon!

He is incredibly hospitable and passionate about fitness, so I aspire to open a store inspired by his persona someday
"""

from campy.graphics.gobjects import GOval, GRect, GArc
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=540, height=540, title='Mr. lemon')
    face = GOval(150, 170)
    face.filled = True
    face.color = 'Dark Sea Green'
    face.fill_color = 'Dark Sea Green'
    window.add(face, x=195, y=185)

    top = GOval(40, 80)
    top.filled = True
    top.color = 'Dark Sea Green'
    top.fill_color = 'Dark Sea Green'
    window.add(top, x=255, y=175)

    bottom = GOval(40, 80)
    bottom.filled = True
    bottom.color = 'Dark Sea Green'
    bottom.fill_color = 'Dark Sea Green'
    window.add(bottom, x=255, y=285)

    eyebrow_l = GOval(10, 3)
    eyebrow_l.filled = True
    eyebrow_r = GOval(10, 3)
    eyebrow_r.filled = True
    window.add(eyebrow_l, x=265, y=230)
    window.add(eyebrow_r, x=300, y=230)

    eye_l = GOval(10, 10)
    eye_l.filled = True
    eye_r = GOval(10, 10)
    eye_r.filled = True
    window.add(eye_l, x=265, y=240)
    window.add(eye_r, x=300, y=240)

    nose = GOval(3, 3)
    nose.filled = True
    window.add(nose, x=290, y=255)

    mouth = GArc(25, 10, -135, 100)
    # mouth.filled = True
    window.add(mouth, x=280, y=265)

    mole_1 = GOval(2, 2)
    mole_1.filled = True
    window.add(mole_1, x=250, y=300)

    mole_2 = GOval(2, 2)
    mole_2.filled = True
    window.add(mole_2, x=245, y=310)

    mole_3 = GOval(2, 2)
    mole_3.filled = True
    window.add(mole_3, x=255, y=315)

    leaf = GOval(80, 30)
    leaf.filled = True
    leaf.color = 'Dark Green'
    leaf.fill_color = 'Dark Green'
    window.add(leaf, x=190, y=180)


if __name__ == '__main__':
    main()
