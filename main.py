import pygame as pg
import sys

pg.init()

# variables
i = 1

# colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# screen resolution
win_width = 1000
win_heigth = 1000

screen = pg.display.set_mode((win_width, win_heigth))
screen.fill(white)
pg.display.set_caption("GridGame")

# font
font = pg.font.SysFont('arial', 25)
number = font.render("1", True, green)
font_x = 25
font_y = 25
font_step_x = 50
font_step_y = 50


# grid
cell_w = 50
cell_h = 50

cell_x = 0
cell_y = 0

step_x = 50
step_y = 50

cell = pg.Rect(cell_x, cell_y, cell_w, cell_h)

while cell_y <= win_heigth:
    pg.draw.rect(screen, black, (cell_x, cell_y, cell_w, cell_h), 1)
    screen.blit(number, (font_x, font_y))
    cell_x += step_x
    font_x += font_step_x

    if cell_x == win_width:
        cell_y += step_y
        cell_x = 0
        font_y += font_step_y
        font_x = 25


# main logic
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    pg.display.flip()

