import turtle


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


if __name__ == "__main__":
    # Sets window size
    turtle.setworldcoordinates(-70.0, -70.0, 70.0, 70.0)
    draw_bag()

    # Prevents window from closing automatically
    turtle.mainloop()
