import turtle
import random
import pandas as pd

image_path = "/Users/alisultan/Desktop/python/State_Guessing_Game/blank_states_img.gif"

#Set up screen
screen = turtle.Screen()
screen.title("U.S.A State Guessing Game")
screen.bgcolor("white")
screen.addshape(image_path)
turtle.shape(image_path)





#read the file first using pandas
states_data = pd.read_csv("/Users/alisultan/Desktop/python/State_Guessing_Game/50_states.csv")

#turtle to write the state name on the map
turtle2 = turtle.Turtle()
turtle2.hideturtle()
turtle2.penup()

#scoreboard writer
score_write = turtle.Turtle()
score_write.hideturtle()
score_write.penup()
score_write.goto(0, 250)

#calculating the score
score = 0
states_guessed = []


#loop through the states and write the name of the state on the map
game_is_on = True

while game_is_on:
#ask the question

    answer = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

    #check if the guess is correct, then hold the x and y values of the state
    if answer == "Exit":
        missing_states = []
        for state in states_data["state"]:
            if state not in states_guessed:
                missing_states.append(state)
        df_missing = pd.DataFrame(missing_states)
        df_missing.to_csv("/Users/alisultan/Desktop/python/State_Guessing_Game/missing_states.csv")
        break
    if answer in states_data["state"].values:
        x = states_data[states_data["state"] == answer]["x"].iloc[0]
        y = states_data[states_data["state"] == answer]["y"].iloc[0]
        
        turtle2.goto(x, y)

        turtle2.write(answer, align="left", font=("poppins", 10, "normal"))

        #add the state to the list of states guessed
        score += 1
        states_guessed.append(answer)
        score_write.clear()
        score_write.write(f"States Guessed: {score} / 50", align="center", font=("poppins", 20, "bold"))
        if score == 50:
            game_is_on = False
            score_write.clear()
            score_write.goto(0, 0)
            score_write.write("You Win!", align="center", font=("poppins", 24, "bold"))
            screen.update()
        else:
            pass
    #check if the answer is already guessed
    elif answer in states_guessed:
        pass

    else:
        pass




#generate a csv file for the use for only the states that are not guessed

