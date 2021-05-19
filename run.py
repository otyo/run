import pyxel
import random


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="run")
        pyxel.load("assets/pic.pyxres")

        self.dx = 0
        # 0 = タイトル
        # 1 = ゲーム画面
        # 2 = 結果

        self.player_x = 30
        self.player_y = 92
        self.life = 3
        self.point = 0
        self.RL = 0
        self.time = 20
        self.time2 = 0
        self.item_1 = [140 + random.randint(0, 20), random.randint(8, 100), 1, random.randint(1, 100)]
        self.item_2 = [180 + random.randint(0, 20), random.randint(8, 100), 1, random.randint(1, 100)]
        self.item_3 = [230 + random.randint(0, 20), random.randint(8, 100), 1, random.randint(1, 100)]
        self.item_4 = [280 + random.randint(0, 20), random.randint(8, 100), 1, random.randint(1, 100)]

        pyxel.run(self.update, self.draw)

    def update(self):

        self.time += 2
        self.time2 += 2

        if self.time <= 20:
            self.player_y -= 3
        else:
            self.player_y += 2

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if self.dx == 1:
                if self.RL == 1:
                    self.RL = 0
                elif self.RL == 0:
                    self.RL = 1
                self.time = 0
            elif self.dx == 0 and 60 <= pyxel.mouse_x and pyxel.mouse_x <= 80 and 60 <= pyxel.mouse_y and pyxel.mouse_y <= 65:
                self.dx = 1
            elif self.dx == 0 and 60 <= pyxel.mouse_x and pyxel.mouse_x <= 80 and 66 <= pyxel.mouse_y and pyxel.mouse_y <= 70:
                pyxel.quit()
            elif self.dx == 2 and 60 <= pyxel.mouse_x and pyxel.mouse_x <= 80 and 60 <= pyxel.mouse_y and pyxel.mouse_y <= 65:
                self.dx = 1
                self.point = 0
            elif self.dx == 2 and 60 <= pyxel.mouse_x and pyxel.mouse_x <= 80 and 66 <= pyxel.mouse_y and pyxel.mouse_y <= 70:
                pyxel.quit()

        self.item_1[0] -= 2
        self.item_2[0] -= 2
        self.item_3[0] -= 2
        self.item_4[0] -= 2

        if self.item_1[0] <= -10:
            self.item_1[1] = random.randint(8, 100)
            self.item_1[0] = 200 + random.randint(0, 20)
            self.item_1[2] = 1
            self.item_1[3] = random.randint(1, 100)
        if self.item_2[0] <= -10:
            self.item_2[1] = random.randint(8, 100)
            self.item_2[0] = 200 + random.randint(0, 20)
            self.item_2[2] = 1
            self.item_2[3] = random.randint(1, 100)
        if self.item_3[0] <= -10:
            self.item_3[1] = random.randint(8, 100)
            self.item_3[0] = 200 + random.randint(0, 20)
            self.item_3[2] = 1
            self.item_3[3] = random.randint(1, 100)
        if self.item_4[0] <= -10:
            self.item_4[1] = random.randint(8, 100)
            self.item_4[0] = 200 + random.randint(0, 20)
            self.item_4[2] = 1
            self.item_4[3] = random.randint(1, 100)
        if self.dx == 1:
            if self.item_1[2] == 1:
                if self.item_1[0] <= 36 and self.item_1[0] >= 30:
                    if self.item_1[1] >= self.player_y and self.item_1[1] + 8 <= self.player_y + 20:
                        self.item_1[2] = 0
                        if self.item_1[3] <= 75:
                            self.point += 1
                        else:
                            self.life -= 1

            if self.item_2[2] == 1:
                if self.item_2[0] <= 36 and self.item_2[0] >= 30:
                    if self.item_2[1] >= self.player_y and self.item_2[1] + 8 <= self.player_y + 20:
                        self.item_2[2] = 0
                        if self.item_2[3] <= 75:
                            self.point += 1
                        else:
                            self.life -= 1
            if self.item_3[2] == 1:
                if self.item_3[0] <= 36 and self.item_3[0] >= 30:
                    if self.item_3[1] >= self.player_y and self.item_3[1] + 8 <= self.player_y + 20:
                        self.item_3[2] = 0
                        if self.item_3[3] <= 75:
                            self.point += 1
                        else:
                            self.life -= 1
            if self.item_4[2] == 1:
                if self.item_4[0] <= 36 and self.item_4[0] >= 30:
                    if self.item_4[1] >= self.player_y and self.item_4[1] + 8 <= self.player_y + 20:
                        self.item_4[2] = 0
                        if self.item_4[3] <= 75:
                            self.point += 1
                        else:
                            self.life -= 1
        if self.life == 0:
            self.dx = 2
            self.life = 3

        pyxel.mouse(True)

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(12)
        if self.dx == 0:
            self.point = 0
            pyxel.text(60, 60, "GAMESTRAT", 7)
            pyxel.text(60, 70, "EXIT", 7)

        if self.dx == 2:
            pyxel.text(60, 50, str(self.point) + "POINT!", 7)
            pyxel.text(60, 60, "RETRY", 7)
            pyxel.text(60, 70, "EXIT", 7)

        pyxel.text(4, 4, "SCORE:" + str(self.point), 7)
        pyxel.text(4, 15, "life:" + str(self.life), 7)
        if self.time2 % 8 == 0:
            self.time2 = 0
        for x in range(22):
            pyxel.blt(x * 8 - (self.time2 % 8), 112, 1, 0, 0, 8, 8, 0)

        if self.player_y >= 92:
            self.player_y = 92
            if self.time % 3 == 0 and self.RL == 0:
                self.RL = 1
            elif self.time % 3 == 0 and self.RL == 1:
                self.RL = 0

        if self.item_1[2] == 1:
            if self.item_1[3] <= 75:
                pyxel.blt(self.item_1[0], self.item_1[1], 1, 8, 0, 8, 8, 0)
            else:
                pyxel.blt(self.item_1[0], self.item_1[1], 1, 8, 8, 8, 8, 0)
        if self.item_2[2] == 1:
            if self.item_2[3] <= 75:
                pyxel.blt(self.item_2[0], self.item_2[1], 1, 8, 0, 8, 8, 0)
            else:
                pyxel.blt(self.item_2[0], self.item_2[1], 1, 8, 8, 8, 8, 0)
        if self.item_3[2] == 1:
            if self.item_3[3] <= 75:
                pyxel.blt(self.item_3[0], self.item_3[1], 1, 8, 0, 8, 8, 0)
            else:
                pyxel.blt(self.item_3[0], self.item_3[1], 1, 8, 8, 8, 8, 0)
        if self.item_4[2] == 1:
            if self.item_4[3] <= 75:
                pyxel.blt(self.item_4[0], self.item_4[1], 1, 8, 0, 8, 8, 0)
            else:
                pyxel.blt(self.item_4[0], self.item_4[1], 1, 8, 8, 8, 8, 0)

        if self.RL == 0:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 12, 20, 0)
        elif self.RL == 1:
            pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 12, 20, 0)


App()
