import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states["state"].to_list()

guessed = 0

answered_states = []


while len(answered_states) < 50:
    answer_state = screen.textinput(title=f"Guessed states: {guessed} / 50", prompt="What's another state's name?")
    guess = answer_state.title()

    if guess == "Exit":
        states_to_learn = [state for state in states_list if state not in answered_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess in states_list and guess not in answered_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_cor = states[states.state == guess]
        t.goto(int(state_cor.x), int(state_cor.y))
        t.write(guess)


        print("you got it!")
        answered_states.append(guess)
        guessed += 1
    elif guess in states_list and guess in answered_states:
        print("Try again, you guessed this one already.")




#states_to_learn.csv

#def get_mouse_click_coor(x, y):
#   print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# screen.exitonclick()