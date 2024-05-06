import turtle


# Renders paper bag that turtle must escape
def draw_bag():
    turtle.shape("turtle")
    turtle.pen(pencolor="blue", pensize=5)
    turtle.penup()  # Lift pen off canvas
    turtle.goto(-35, 35)
    turtle.pendown()  # place pen on canvas to draw
    turtle.right(90)  # Rotate 90 degrees clock-wise
    turtle.forward(70)  # Move 70 units
    turtle.left(90)  # Rotate 90 degrees counter-clock-wise
    turtle.forward(70)  # Move 70 units
    turtle.left(90)
    turtle.forward(70)


# Check if turtle escaped x or y bounds of paper bag
def escaped(position):
    x = int(position[0])
    y = int(position[1])

    return x < -35 or x > 35 or y < -35 or y > 35


def draw_line():
    angle = 0
    step = 5
    tur = turtle.Turtle()

    while not escaped(tur.position()):
        tur.left(angle)
        tur.forward(step)


if __name__ == "__main__":
    # Sets window size
    turtle.setworldcoordinates(-70.0, -70.0, 70.0, 70.0)
    draw_bag()
    draw_line()
    # Prevents window from closing automatically
    turtle.mainloop()
