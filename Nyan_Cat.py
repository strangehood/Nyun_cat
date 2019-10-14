from tkinter import *
from tkinter import Canvas

root = Tk()

root.geometry('800x600')

c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)

color = ('indian red', 'orange', 'yellow', 'pale green', 'RoyalBlue1', 'MediumPurple')
rainbow_list = [[0 for _ in range(6)] for _ in range(10)]
cat = [0 for _ in range(11)]
body_parts = ('head', 'ear1', 'ear2', 'eye1', 'eye2', 'mouth1', 'mouth2', 'nose', 'body', 'leg1', 'leg2')

xs = 170
ys = 190
dx = 0.05
step = 0
flag_step = False


def cat_creation(xh, yh):
    # legs
    cat[body_parts.index('leg1')] = c.create_oval(60 + xh, 108 + yh, 85 + xh, 153 + yh, fill='grey', outline='grey')
    cat[body_parts.index('leg2')] = c.create_oval(115 + xh, 108 + yh, 140 + xh, 153 + yh, fill='grey', outline='grey')

    # body
    cat[body_parts.index('body')] = c.create_rectangle(50 + xh, 50 + yh, 150 + xh, 125 + yh, fill='hot pink',
                                                       outline='burlywood1', width=8)
    # head
    cat[body_parts.index('head')] = c.create_rectangle(120 + xh, 60 + yh, 180 + xh, 110 + yh, fill='grey',
                                                       outline='grey')

    # ears and eyes
    cat[body_parts.index('ear1')] = c.create_polygon(120 + xh, 60 + yh, 130 + xh, 40 + yh, 140 + xh, 60 + yh,
                                                     fill='grey', outline='grey')
    cat[body_parts.index('ear2')] = c.create_polygon(160 + xh, 60 + yh, 170 + xh, 40 + yh, 180 + xh, 60 + yh,
                                                     fill='grey', outline='grey')
    cat[body_parts.index('eye1')] = c.create_oval(130 + xh, 75 + yh, 140 + xh, 85 + yh, fill='black')
    cat[body_parts.index('eye2')] = c.create_oval(170 + xh, 75 + yh, 160 + xh, 85 + yh, fill='black')

    # mouth and nose
    cat[body_parts.index('mouth1')] = c.create_line(140 + xh, 105 + yh, 160 + xh, 105 + yh, fill='black')
    cat[body_parts.index('mouth2')] = c.create_line(150 + xh, 95 + yh, 150 + xh, 105 + yh, fill='black')
    cat[body_parts.index('nose')] = c.create_rectangle(147 + xh, 89 + yh, 153 + xh, 95 + yh, fill='hot pink')


def rainbow():
    global color, rainbow_list
    for j in range(10):
        for i in range(6):
            rainbow_list[j][i] = c.create_rectangle(22 * j, 240 + 10 * i, 22 + 22 * j, 250 + 10 * i,
                                                    fill=color[i], outline=color[i])


def running_cat():
    global xs, ys, dx, step, flag_step

    if (step < 0) and (step % 3 == 0):
        for j in range(10):
            if j % 2 == 0:
                for i in range(6):
                    c.move(rainbow_list[j][i], 0, 10 * dx)

                    # head moving
                    c.move(cat[body_parts.index('head')], 0, dx)
                    c.move(cat[body_parts.index('eye1')], 0, dx)
                    c.move(cat[body_parts.index('eye2')], 0, dx)
                    c.move(cat[body_parts.index('ear1')], 0, dx)
                    c.move(cat[body_parts.index('ear2')], 0, dx)
                    c.move(cat[body_parts.index('mouth1')], 0, dx)
                    c.move(cat[body_parts.index('mouth2')], 0, dx)
                    c.move(cat[body_parts.index('nose')], 0, dx)

        for j in range(10):
            if j % 2 == 1:
                for i in range(6):
                    c.move(rainbow_list[j][i], 0, -10 * dx)

    if (step > 0) and (step % 3 == 0):
        for j in range(10):
            if j % 2 == 0:
                for i in range(6):
                    c.move(rainbow_list[j][i], 0, - 10 * dx)

                    # head moving
                    c.move(cat[body_parts.index('head')], 0, -dx)
                    c.move(cat[body_parts.index('eye1')], 0, -dx)
                    c.move(cat[body_parts.index('eye2')], 0, -dx)
                    c.move(cat[body_parts.index('ear1')], 0, -dx)
                    c.move(cat[body_parts.index('ear2')], 0, -dx)
                    c.move(cat[body_parts.index('mouth1')], 0, -dx)
                    c.move(cat[body_parts.index('mouth2')], 0, -dx)
                    c.move(cat[body_parts.index('nose')], 0, -dx)

        for j in range(10):
            if j % 2 == 1:
                for i in range(6):
                    c.move(rainbow_list[j][i], 0, 10 * dx)

    if flag_step is False:
        c.move(cat[body_parts.index('leg1')], -1, 0)
        c.move(cat[body_parts.index('leg2')], 1, 0)
    else:
        c.move(cat[body_parts.index('leg1')], 1, 0)
        c.move(cat[body_parts.index('leg2')], -1, 0)

    if step > 10:
        flag_step = True
    elif step < -10:
        flag_step = False
    if flag_step is False:
        step += 1
    else:
        step -= 1
    root.after(30, running_cat)

def jumping_cat():
    pass


rainbow()
cat_creation(170, 190)
running_cat()
root.bind('<SPACE>', jumping_cat)

root.mainloop()
