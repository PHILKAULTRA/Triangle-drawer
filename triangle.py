import turtle

# Get user input for triangle angles
angle1 = int(input("Enter the first angle in degrees: "))
angle2 = int(input("Enter the second angle in degrees: "))

# Calculate the third angle and check that the angles add up to 180 degrees
angle3 = 180 - angle1 - angle2
if angle3 <= 0:
    print("Error: Invalid angle values.")
    turtle.done()
else:
    # Set up turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(3)

    # Draw the triangle
    t.pencolor('red')
    t.fillcolor('orange')
    t.begin_fill()
    t.forward(200)
    t.write(str(angle1) + '°', font=("Arial", 12, "normal"))
    t.left(180 - angle1)
    t.forward(200)
    t.write(str(angle2) + '°', font=("Arial", 12, "normal"))
    t.left(180 - angle2)
    t.forward(200)
    t.write(str(angle3) + '°', font=("Arial", 12, "normal"))
    t.end_fill()

    # Print the third angle
    print("The third angle is", angle3)

    turtle.done()
