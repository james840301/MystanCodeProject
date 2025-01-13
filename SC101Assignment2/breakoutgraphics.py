"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Players control the position of the paddle using the mouse and must bounce the falling ball back up to the bricks to destroy all of them. Besides the boundary at the bottom of the game window, the ball will bounce off any objects and edges it encounters.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)//2,
                        y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) // 2,
                        y=(self.window.height - self.ball.height)//2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        self.is_moving = False
        onmouseclicked(self.move_ball)
        # Draw bricks
        self.draw()
        # Count bricks
        self.brick_count = BRICK_ROWS * BRICK_COLS

        # 設置顯示得分和生命的標籤
        self.score = 0  # 初始得分
        self.lives = NUM_LIVES  # 初始生命數量
        self.score_label = GLabel(f"Score: {self.score}")
        self.score_label.font = 'Arial-16'
        self.window.add(self.score_label, x=10, y=20)

        self.lives_label = GLabel(f"Lives: {self.lives}")
        self.lives_label.font = 'Arial-16'
        self.window.add(self.lives_label, x=self.window.width - 100, y=20)

    def draw(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = col * (BRICK_WIDTH + BRICK_SPACING)
                y = BRICK_OFFSET + row * (BRICK_HEIGHT + BRICK_SPACING)
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True
                color = colors[row // 2 % len(colors)]
                brick.fill_color = color
                self.window.add(brick, x=x, y=y)

    def move_paddle(self, event):
        new_x = event.x - self.paddle.width/2
        # 計算 paddle 的合法位置範圍
        min_x = 0
        max_x = self.window.width - self.paddle.width
        # 限制 paddle 的位置在合法範圍內
        if new_x < min_x:
            new_x = min_x
        elif new_x > max_x:
            new_x = max_x
        self.paddle.x = new_x

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

    def move_ball(self, event):
        if not self.is_moving:
            self.is_moving = True  # 點擊開始讓球移動
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:  # 讓球一開始可以隨機產生往左或往右
                self.__dx = -self.__dx

    def reset_ball(self):
        self.is_moving = False
        self.ball.x = (self.window.width - self.ball.width) // 2
        self.ball.y = (self.window.height - self.ball.height) // 2
        self.__dx = 0
        self.__dy = 0
        self.update_lives(self.lives)  # 更新生命顯示

    def check_collision(self):
        # 球的四個頂點
        ball_top_left = (self.ball.x, self.ball.y)
        ball_top_right = (self.ball.x + self.ball.width, self.ball.y)
        ball_bottom_left = (self.ball.x, self.ball.y + self.ball.height)
        ball_bottom_right = (self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        # 逐一檢查頂點
        for point in [ball_top_left, ball_top_right, ball_bottom_left, ball_bottom_right]:
            obj = self.window.get_object_at(point[0], point[1])
            if obj is not None:
                return obj

        # 如果所有角點都沒有碰到物件
        return None

    def update_score(self, points):
        self.score += points
        self.score_label.text = f"Score: {self.score}"

    def update_lives(self, lives):
        self.lives = lives
        self.lives_label.text = f"Lives: {self.lives}"