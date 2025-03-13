import turtle


def koch_curve(t, order, size):
    # base case
    if order == 0:
        t.forward(size)
    # recursive case
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(size=300):
    """
    Function that drows a Koch snowflake with the depth provided by user.
    """

    try:
        # maybe better to propose input a number in cpecific range to avoid a stackoverflow for example up to 10
        order = int(input('Input number that represents depth of Koch snowflake in range 0 - 10:   ')) 
        if order in range(0, 11):
            window = turtle.Screen()
            window.bgcolor("white")

            t = turtle.Turtle()
            t.speed(0)  
            t.penup()
            t.goto(-size / 2, 0)
            t.pendown()

            for i in range(3):
                koch_curve(t, order, size)
                t.right(120)

            window.mainloop()
        else:
            print('The number is not in range from 0 to 10')    

    except ValueError:
        print("Invalid input! Please enter a number.")

draw_koch_snowflake()


