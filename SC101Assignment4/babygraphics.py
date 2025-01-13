"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_distance = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * x_distance
    return int(x_coordinate)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # 取得 canvas 的寬度和高度
    canvas_width = CANVAS_WIDTH
    canvas_height = CANVAS_HEIGHT

    # 畫頂端的橫線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       canvas_width - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)

    # 畫底端的橫線
    canvas.create_line(GRAPH_MARGIN_SIZE, canvas_height - GRAPH_MARGIN_SIZE,
                       canvas_width - GRAPH_MARGIN_SIZE, canvas_height - GRAPH_MARGIN_SIZE)

    # 針對每個年份畫出一條垂直線，並標記年份
    for i in range(len(YEARS)):
        x = get_x_coordinate(canvas_width, i)
        # 畫垂直線，從頂部到底部
        canvas.create_line(x, 0, x, canvas_height)
        # 在垂直線的右邊標記年份
        canvas.create_text(x + TEXT_DX, canvas_height - GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    canvas_width = CANVAS_WIDTH
    canvas_height = CANVAS_HEIGHT

    # 繪製每個名字的資料
    for name in lookup_names:
        if name in name_data:  # 確保名字存在於資料中
            years_data = name_data[name]
            previous_x = None
            previous_y = None

            # 繪製每年的資料點
            for i, year in enumerate(YEARS):
                x = get_x_coordinate(canvas_width, i)  # 計算 X 座標

                # 檢查該名字在這一年是否有資料，否則顯示 '*'
                if str(year) in years_data:
                    rank = years_data[str(year)]
                    y = (int(rank) / 1000) * (canvas_height - 2 * GRAPH_MARGIN_SIZE) + GRAPH_MARGIN_SIZE
                else:
                    rank = '*'
                    y = canvas_height - GRAPH_MARGIN_SIZE  # 沒有排名的資料顯示在底部

                # 繪製線條
                if previous_x is not None and previous_y is not None:
                    canvas.create_line(previous_x, previous_y, x, y,
                                       fill=COLORS[lookup_names.index(name) % len(COLORS)], width=LINE_WIDTH)

                # 繪製文字
                if rank == '*':
                    canvas.create_text(x + TEXT_DX, y, text=f"{name} *", anchor=tkinter.SW,
                                       fill=COLORS[lookup_names.index(name) % len(COLORS)])
                else:
                    canvas.create_text(x + TEXT_DX, y, text=f"{name} {rank}", anchor=tkinter.SW,
                                       fill=COLORS[lookup_names.index(name) % len(COLORS)])

                # 更新 previous_x 和 previous_y 為下一次的線條連接點
                previous_x, previous_y = x, y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
