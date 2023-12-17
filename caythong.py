import turtle as t
import random as r

# Thiết lập môi trường
n = 100.0
t.speed("fastest")
t.screensize(bg='black')
t.left(90)
t.color("orange", "yellow")


# Hàm vẽ nến của cây
def draw_light():
    if r.randint(0, 30) == 0:
        t.color('tomato')
        t.circle(6)
    elif r.randint(0, 30) == 1:
        t.color('orange')
        t.circle(3)
    else:
        t.color('dark green')


# Hàm vẽ cây
def draw_tree(d, s):
    if d <= 0:
        return
    t.forward(s)
    draw_tree(d - 1, s * .8)
    t.right(120)
    draw_tree(d - 3, s * .5)
    draw_light()
    t.right(120)
    draw_tree(d - 3, s * .5)
    t.right(120)
    t.backward(s)


# Hàm vẽ tuyết
def draw_snow():
    t.ht()
    t.pensize(2)
    for i in range(200):
        t.pencolor("white")
        t.penup()
        t.setx(r.randint(-350, 350))
        t.sety(r.randint(-100, 350))
        t.pendown()
        dens = 6
        snow_size = r.randint(1, 10)
        for j in range(dens):
            t.forward(int(snow_size))
            t.backward(int(snow_size))
            t.right(int(360 / dens))


# Vẽ cây
t.begin_fill()
t.left(126)
for i in range(5):
    t.forward(n / 5)
    t.right(144)
    t.forward(n / 5)
    t.left(72)
t.end_fill()
t.right(126)
t.color("dark green")
t.backward(n * 4.8)
draw_tree(15, n)
t.backward(n / 2)

# Vẽ tuyết
for i in range(200):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    t.penup()
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.pendown()
    if r.randint(0, 1) == 0:
        t.color('tomato')
    else:
        t.color('wheat')
    t.circle(2)
    t.penup()
    t.backward(a)
    t.right(90)
    t.backward(b)

# Ghi lời chúc
t.color("dark red", "red")
t.write("Chúc Mừng Giáng Sinh", align="center", font=("Arial", 20, "bold"))

# Vẽ tuyết rơi
draw_snow()

# Hiển thị
t.done()
