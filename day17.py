# import turtle

# screen=turtle.Screen()
# screen.bgcolor("#aee8be")
# # screen.title("My Rangoli")

# # myTurtle=turtle.Turtle()
# # myTurtle.pencolor("red")

# # for i in range(72):
# #     myTurtle.forward(200)
# #     myTurtle.right(90)
# #     myTurtle.right(5)


# # myTurtle.speed(2)
# # myTurtle.forward(300)
# # myTurtle.right(90)
# # myTurtle.forward(300)
# # myTurtle.right(90)
# # myTurtle.forward(300)
# # myTurtle.right(90)
# # myTurtle.forward(300)
# # myTurtle.right(45)
# # myTurtle.forward(150)

# # myTurtle.pencolor("red")
# # myTurtle.penup()
# # myTurtle.goto(200,45)

# # screen.mainloop()

# import turtle
# import math

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("white")

# screen.title("Complex Rangoli Pattern")

# # Initialize the turtle
# rangoli = turtle.Turtle()
# rangoli.speed(0)  # Fastest drawing speed
# rangoli.pensize(5)

# # Color palette for the rangoli
# colors = ["#FF595E", "#FFCA3A", "#8AC926", "#1982C4", "#6A4C93", "#F4A261"]

# # Function to draw overlapping geometric petals
# def draw_petal(t, r, angle):
#     for _ in range(2):
#         t.circle(r, angle)
#         t.left(180 - angle)

# # Main drawing loop

# num_petals = 36  # Number of rotations
# petal_radius = 150
# petal_angle = 60

# for i in range(num_petals):
#     rangoli.color(colors[i % len(colors)])  # Cycle through colors
#     draw_petal(rangoli, petal_radius, petal_angle)
#     rangoli.left(360 / num_petals)  # Rotate for the next petal

# # Hide the turtle when done
# rangoli.hideturtle()

# # Keep the window open
# turtle.done()
