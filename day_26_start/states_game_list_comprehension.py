import turtle
import pandas

image = 'blank_states_img.gif'
data = pandas.read_csv('50_states.csv')
states_list = data['state'].tolist()

turtle.screensize(canvwidth=725, canvheight=491)
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
guessed_states = []
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f'Guess the state {len(guessed_states)}/50', prompt="What's this state name?")
    answer_state = answer_state.title()

    if answer_state in states_list and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item() - len(answer_state), state_data.y.item())
        t.write(answer_state, move=False, align='left', font=('Arial', 7, 'bold'))
        t.hideturtle()
        guessed_states.append(answer_state)
    elif answer_state == 'Exit':
        break
    else:
        screen.textinput(title='Try again!', prompt='You lost a life! Type anything to continue')

not_guessed_list = [n for n in states_list if n not in guessed_states]
for x in not_guessed_list:
    print(f'{x}\n')
not_guessed_dict = {'states': not_guessed_list}

states_data = pandas.DataFrame(not_guessed_dict)
states_data.to_csv('List_of_missing_states.csv')

turtle.mainloop()
turtle.bye()
