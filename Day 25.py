from pathlib import Path
import os

new_dir = Path("/Users/iray/Python/100DaysOfCode/Day 25")
os.chdir(new_dir)
        
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.dox", mode="w") as completed_letter:
             completed_letter.write(new_letter)