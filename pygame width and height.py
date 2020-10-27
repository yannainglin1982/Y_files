import pygme
def create_window(width, height):
    win= pg.display.set_mode((width, height), pg.RESIZABLE)
    win.fill ((255, 0, 0))
    pygame.display.set_caption("wow")
    sf= "size x=%s y=%s" % (width, height)
    pg.display.set_caption(sf)

    white=(255, 255, 255)
    cent= (150, 150)
    radius=100
    pg.draw.circle(win, whit, center, radius)

    pg.display.flip()

pg.init()
width=300
height=200
win= creat_window(width, height)
while True:
    if event.type == pg.VIDEORESIZE:
        width, height = event.size
        win = create_window(width, height)
        print(win.get_size())
        if event.type == pg.QUIT:
            raise SystemExit
