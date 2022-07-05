import pygame as pg

# colors
white = (255, 255, 255)
green = (0, 255, 0)

# screen
w_width = 1000
w_height = 1000

window = pg.display.set_mode((w_width, w_height))
pg.display.set_caption('Рисовалка треугольников')

'''
для рисования треугольника:
1)выбрать начальную точку левого края треугольника (x1, y1) P.S значения одинаковые
2)выбрать вторую точку правого края треугольника (x2, y2) P.S x2 - ширина треугольника y2 - неизменно
3) выбрать третью точку вершину треугольника (x3, y3) P.S x3 - середина треугольника y3 - высота треугольника 
4) выбрать закрашенный будет треугольник или нет P.S 0 - ДА, 1 - НЕТ
'''
def drawTriangleFill(x1, y1, x2, y3, i):
    x2 = x1 + x2
    y2 = y1
    x3 = ((x2 - x1) / 2) + x1
    y3 = y2 - y3
    triangle_fill = pg.draw.polygon(window, green, ((x1, y1), (x2, y2), (x3, y3)), i)

#def drawChristmasTree(c_x1, c_y1):





def start_game():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.QUIT
            drawTriangleFill(500, 500, 100, 75, 0)
            drawTriangleFill(500, 575, 100, 75, 0)
            drawTriangleFill(500, 650, 100, 75, 0)
            pg.display.flip()

start_game()