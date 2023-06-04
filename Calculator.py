from GUI_Calculator import GUI_calculator

class CalculatorEugenio(GUI_calculator):
    def get_digit(self, digit, Num_Input):
            current = Num_Input['text']
            new = current + str(digit)
            Num_Input.config(text=new)

    def clear(Num_Input):
        Num_Input.config(text='')

    def get_operation(op, Num_Input):
            global frst_num, operator

            frst_num = int(Num_Input['text'])
            operator = op
            Num_Input.config(text='')

    def get_answer(Num_Input):
        global frst_num, scnd_num, operator
                            
        scnd_num = Num_Input['text']

        if operator == '+':
            Num_Input.config(text=int(float(frst_num) + float(scnd_num)))
        elif operator == '-':
            Num_Input.config(text=int(float(frst_num) - float(scnd_num)))
        elif operator == '*':
            Num_Input.config(text=int(float(frst_num) * float(scnd_num)))
        else:
            if scnd_num == 0:
                Num_Input.config(text='Syntax Error')
            else:
                Num_Input.config(text=str(round(float(frst_num) / float(scnd_num), 2)))
