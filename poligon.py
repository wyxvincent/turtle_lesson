import turtle
t = turtle.Pen()

def polygon(side, length):
    if side < 2:
        print("2条边不足以构成多边形")
    else:
        angle = 180 - (side - 2) * 180 / side
        for i in range(side):
            t.forward(length)
            t.left(angle)
    turtle.done()

side = int(input("请输入多边形的边数："))
length = int(input("请输入多边形的边长："))
polygon(side, length)