from tkinter import *

root = Tk()

root.geometry('800x600')

c = Canvas(root, bg='black')
c.pack(fill=BOTH, expand=1)

color = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')

def cat_head(xh, yh):

    # head
    c.create_rectangle(120 + xh, 60 + yh, 180 + xh, 110 + yh, fill='grey', outline='grey')

    # ears and eyes
    c.create_polygon(120 + xh, 60 + yh, 130 + xh, 40 + yh, 140 + xh, 60 + yh, fill='grey', outline='grey')
    c.create_polygon(160 + xh, 60 + yh, 170 + xh, 40 + yh, 180 + xh, 60 + yh, fill='grey', outline='grey')
    c.create_oval(130 + xh, 75 + yh, 140 + xh, 85 + yh, fill='black')
    c.create_oval(170 + xh, 75 + yh, 160 + xh, 85 + yh, fill='black')

    # mouth and nose
    c.create_line(140 + xh, 105 + yh, 160 + xh, 105 + yh, fill='black')
    c.create_line(150 + xh, 95 + yh, 150 + xh, 105 + yh, fill='black')
    c.create_rectangle(147 + xh, 89 + yh, 153 + xh, 95 + yh, fill='pink')

def cat_body(xb, yb):
    c.create_rectangle(50 + xb, 50 + yb, 150 + xb, 125 + yb, fill='maroon2', outline='burlywood1',
                       width=8)

def cat_leg(xl, yl):
    c.create_oval(50 + xl, 108 + yl, 75 + xl, 153 + yl, fill='grey', outline='black', width=3)

#def rainbow():
   # global color
   #  c.create_rectangle(, fill=color[i])

def standing_cat(xs, ys):
    cat_leg(xs, ys)
    cat_leg(xs + 75, ys)
    cat_body(xs, ys)
    cat_head(xs, ys)


standing_cat(170, 190)
root.mainloop()

