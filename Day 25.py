#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:09:09 2025

@author: iray
"""


# set working directory
from pathlib import Path
import os

new_dir = Path("/Users/iray/Python/100DaysOfCode/Day 25")
os.chdir(new_dir)

print(os.getcwd())

#%% The Great Squirrel Census Data Analysis
import pandas as pd

squirrel_data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

squirrel_count = squirrel_data.groupby("Primary Fur Color")["Unique Squirrel ID"].count().reset_index()
squirrel_count.columns = ["Fur Color", "Count"]

squirrel_count.to_csv("squirrel_count.csv", index = False)

#%% U.S. State Game

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                   prompt="What's another state's name? Type 'Exit' to quit").title()
    
    # Check for exit condition 
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missing_states, columns=["State"]).to_csv("states_to_learn.csv")
        break
        
    # Check if answer is correct and not already guessed
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

screen.exitonclick()
