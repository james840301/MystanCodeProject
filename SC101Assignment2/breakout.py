"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Players control the position of the paddle using the mouse and must bounce the falling ball back up to the bricks to destroy all of them. Besides the boundary at the bottom of the game window, the ball will bounce off any objects and edges it encounters.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    while True:
        pause(FRAME_RATE)

        # 只有在球開始移動後才更新球的位置
        if graphics.is_moving:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)

            # 碰到左右牆壁反彈
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-dx)  # 修改 dx

            # 碰到上邊界反彈
            if graphics.ball.y <= 0:
                graphics.set_dy(-dy)  # 修改 dy

            # 掉到畫面底部
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.lives -= 1
                graphics.update_lives(graphics.lives)  # 更新生命顯示
                if graphics.lives > 0:
                    graphics.reset_ball()  # 重置球位置，等待下一次點擊
                else:
                    break  # 玩家用完所有生命，遊戲結束

            # 檢查是否已消滅所有磚塊
            if graphics.brick_count == 0:
                break  # 所有磚塊都消滅，遊戲勝利

            # 碰到球拍反彈
            if graphics.ball.y + graphics.ball.height >= graphics.paddle.y:  # 球的底部到達球拍頂部
                if graphics.paddle.x <= graphics.ball.x <= graphics.paddle.x + graphics.paddle.width:  # 球在球拍範圍內
                    if graphics.ball.y + graphics.ball.height <= graphics.paddle.y + graphics.paddle.height:
                        graphics.set_dy(-dy)  # 使用 setter 來確保垂直反彈

                        # 修正穿過問題，讓球的底部與球拍的頂部對齊
                        graphics.ball.y = graphics.paddle.y - graphics.ball.height

            # 碰撞檢測
            obj = graphics.check_collision()
            if obj:
                # 碰到磚塊，移除並反彈
                if obj != graphics.paddle:
                    graphics.window.remove(obj)
                    graphics.update_score(10)  # 每次碰到磚塊加 10 分
                    graphics.brick_count -= 1
                graphics.set_dy(-dy)  # 反彈



if __name__ == '__main__':
    main()
