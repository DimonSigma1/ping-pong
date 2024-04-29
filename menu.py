import pygame as pg
from button import Button

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.play_with_bot = Button(
            30, 30, 100, 30, "Игарть с ботом",
            (180, 0, 0), (140, 0, 0), (100, 0, 0),
            (255, 255, 255))
        self.play_with_friend = Button(
            200, 30, 100, 30, "Играть с дургом",
            (180, 0, 0), (140, 0, 0), (100, 0, 0),
            (255, 255, 255))
        self.settings = Button(
            400, 30, 100, 30, "Настройки",
            (180, 0, 0), (140, 0, 0), (100, 0, 0),
            (255, 255, 255))
        self.exit = Button(
            600, 30, 100, 30, "Выход",
            (180, 0, 0), (140, 0, 0), (100, 0, 0),
            (255, 255, 255))
        self.clock = pg.time.Clock()
        self.FPS = 30


    def update(self):
        self.play_with_bot.update()
        self.play_with_friend.update()
        self.settings.update()
        self.exit.update()

        self.play_with_bot.draw(self.surface)
        self.play_with_friend.draw(self.surface)
        self.settings.draw(self.surface)
        self.exit.draw(self.surface)

class MenuBall():
    def __init__(self, surface):
        self.surface = surface
        self.image = pg.transform.scale(pg.image.load('ball.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = surface.get_rect().width // 2
        self.rect.y = surface.get_rect().height // 2
        self.speed_x = 5
        self.speed_y = 5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.x + self.rect.width > self.surface.gat_rect().width:
            self.speed_x *= -1
        if self.rect.x < 0:
            self.rect_y *= -1
        if self.rect.x + self.rect.height > self.surface.gat_rect().height:
            self.speed_y *= -1


if __name__ == '__main__':
    pg.init()

    mw = pg.display.set_mode((700, 500))

    menu = Menu(mw)

    game = True
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False

        menu.update()

        pg.display.flip()
        pg.time.Clock().tick(30)
    
    