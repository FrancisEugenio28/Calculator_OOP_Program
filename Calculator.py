#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Simple Calculator w/ implementation of Object Oriented Programming

from GUI_Calculator import GUI_calculator
Num_Input = GUI_calculator()
Num_Input.GUI()

#pseudocode
#create function for each number button
def get_digit(digit):
    current = Num_Input['text']
    new = current + str(digit)
    Num_Input.config(text=new)
#create a function for the clear button
#create a function for each operation
# Perform operation within the = button