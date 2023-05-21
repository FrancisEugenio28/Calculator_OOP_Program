#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Simple Calculator w/ implementation of Object Oriented Programming

from GUI_Calculator import GUI_calculator
input_num = GUI_calculator()
input_num.Num_Input()
#pseudocode
#create function for each number button
def get_digit(digit):
    current = input_num.Num_Input()['text']
    new = current + str(digit)
    input_num.Num_Input()(text=new)
#create a function for the clear button
#create a function for each operation
# Perform operation within the = button