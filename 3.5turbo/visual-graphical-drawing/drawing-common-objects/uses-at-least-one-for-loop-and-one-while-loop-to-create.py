import turtle

# Create a turtle object
turtle_obj = turtle.Turtle()

# Set the speed and shape of the turtle
turtle_obj.speed(10)
turtle_obj.shape("turtle")

# Define the number of sides of the polygon
num_sides = 5

# Define the colors for the design
colors = ["red", "orange", "yellow", "green", "blue"]

# Draw the abstract design using a for loop
for i in range(num_sides):
    # Change the color based on the index
    turtle_obj.pencolor(colors[i])

    # Draw a polygon with the current number of sides
    for j in range(num_sides):
        turtle_obj.forward(100)
        turtle_obj.right(360 / num_sides)

    # Increase the number of sides for the next polygon
    num_sides += 1

# Hide the turtle
turtle_obj.hideturtle()

# Exit on click
turtle.done()
