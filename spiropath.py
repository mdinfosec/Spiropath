import turtle, random

# Create window and turtle
window = turtle.screensize(2000,1500)
window = turtle.Screen()
squirtle = turtle.Turtle()
squirtle.hideturtle()
angle = random.randint(10, 360)
squirtle.left(angle)

loops = random.randint(1, 25)

for x in range(0, loops):

    angle = random.randint(10, 360)
    steps = random.randint(20, 200)
    size = random.randint(2, 4)

    colors = random.choice(['red','grey','black','white'])

    redpen = random.choice(['grey','black','white'])
    greypen = random.choice(['red','black','white'])
    blackpen = random.choice(['red','grey','white'])
    whitepen = random.choice(['red','grey','black'])

    circle = random.choice(['Yes', 'No'])

    home = random.choice(['Yes', 'No'])
    clear = random.choice(['Yes', 'No'])

    for i in range(steps):
        
        squirtle.pensize(size)
        squirtle.speed(10)
        
        window.bgcolor(colors)
        if window.bgcolor() == 'red':
            squirtle.pencolor(redpen)
        if window.bgcolor() == 'grey':
            squirtle.pencolor(greypen)
        if window.bgcolor() == 'black':
            squirtle.pencolor(blackpen)
        if window.bgcolor() == 'white':
            squirtle.pencolor(whitepen)
        
        squirtle.forward(steps)
        squirtle.left(steps)
        squirtle.backward(steps)
        squirtle.right(steps * 2)
        
        if circle == 'Yes':
            squirtle.circle(steps // 3)

    squirtle.penup()

    if home == 'Yes':
        squirtle.home()

    squirtle.left(angle)
    squirtle.forward(steps // 3)
    squirtle.pendown()
    
    if clear == 'Yes':
        window.clear()
                           
# Tidy up window
squirtle.done()
