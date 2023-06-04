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