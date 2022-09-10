import turtle
import pandas
# create screen object using turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# create pandas object to read CSV data
data = pandas.read_csv("50_states.csv")
# get all the states in the state column
all_states = data.state.to_list()
# create a list to input all the states user has made.
guessed_state = []


while len(guessed_state) < 50:
    # take in the input of the user
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="Guess another state?").title()
    # allow user to exit the game
    if answer == "Exit":
        # create list to check all the states the user has missed
        missing_states = []
        # loop through the states
        for state in all_states:
            # check if the states are in the guessed list, and if not add them to the missing_states list
            if state not in guessed_state:
                missing_states.append(state)
        # create new panda object from the missing states using panda DataFrame
        new_data = pandas.DataFrame(missing_states)
        # create CSV file of the missing_states list
        new_data.to_csv("states_to_learn.csv")
        break
    # check if the answer is in states column.
    if answer in all_states:
        # add the answer to the guessed list
        guessed_state.append(answer)
        # create turtle object
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # get the row data
        state_row = data[data.state == answer]
        # move the turtle object to the x and y coordinates of the guessed state
        t.goto(int(state_row.x), int(state_row.y))
        # write the answer on the screen
        t.write(answer)



