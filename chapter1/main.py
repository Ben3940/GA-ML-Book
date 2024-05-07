import turtle
import pickle


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


def draw_square(tur, size):
    path = list()

    for i in range(4):
        # move turtle forward step size and then turn 90 degrees
        tur.forward(size)
        tur.left(90)
        store_position_data(path, tur)
    return path


def draw_squares(number):
    tur = turtle.Turtle()
    path = list()

    for i in range(1, number + 1):
        # reset pen position to next square start point
        tur.penup()
        tur.goto(-i, -i)
        tur.pendown()
        # Draw square and add to complete path
        path.extend(draw_square(tur, i * 2))

    return path


# Draw all squares and save to file
def draw_squares_until_escaped(n):
    tur = turtle.Turtle()
    complete_path = draw_squares(n)
    with open("data_square", "wb") as file:
        pickle.dump(complete_path, file)


def store_position_data(path, tur):
    position = tur.position()
    path.append([position[0], position[1], escaped(position)])


if __name__ == "__main__":
    # Sets window size
    turtle.setworldcoordinates(-70.0, -70.0, 70.0, 70.0)
    draw_bag()
    # draw_line()
    draw_squares(10)
    # Prevents window from closing automatically
    turtle.mainloop()
