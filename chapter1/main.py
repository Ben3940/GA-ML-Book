import turtle
import pickle
import random
import argparse
import inspect


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


def draw_triangles(number):
    angle = 120
    tur = turtle.Turtle()

    for i in range(1, number):
        tur.forward(i * 10)
        tur.right(angle)


# Draw all squares and save to file
def draw_squares_until_escaped(n):
    tur = turtle.Turtle()
    complete_path = draw_squares(n)
    save_path_to_file(complete_path, "data_square")


def draw_spirangles_until_escaped():
    tur = turtle.Turtle()
    # tur.penup()
    # tur.left(random.randint(0, 360))
    # tur.pendown()

    i = 0
    turn = 360 / random.randint(1, 10)
    path = list()
    store_position_data(path, tur)

    while not escaped(tur.position()):
        i += 1
        tur.forward(i * 5)
        tur.right(turn)
        store_position_data(path, tur)

    return path


def draw_random_spirangles():
    complete_path = list()
    for i in range(10):
        complete_path.extend(draw_spirangles_until_escaped())

    save_path_to_file(complete_path, "data_spirangle")


def store_position_data(path, tur):
    position = tur.position()
    path.append([position[0], position[1], escaped(position)])


def save_path_to_file(path, file_name):
    with open(file_name, "wb") as file:
        pickle.dump(path, file)


if __name__ == "__main__":

    funcs = {
        "line": draw_line,
        "squares": draw_squares_until_escaped,
        "triangles": draw_triangles,
        "spirangles": draw_random_spirangles,
    }

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--function", choices=funcs, help="One of " + ", ".join(funcs.keys())
    )
    parser.add_argument("-n", "--number", default=50, type=int, help="How many?")
    args = parser.parse_args()

    try:
        func = funcs[args.function]
        # Sets window size
        turtle.setworldcoordinates(-70.0, -70.0, 70.0, 70.0)
        draw_bag()
        turtle.hideturtle()
        if len(inspect.getargspec(func).args) == 1:
            func(args.number)
        else:
            func()
    except KeyError:
        parser.print_help()
    # Prevents window from closing automatically
    turtle.mainloop()
