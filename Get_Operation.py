class GetOperation:
    def get_operation(op, Num_Input):
            global frst_num, operator

            frst_num = int(Num_Input['text'])
            operator = op
            Num_Input.config(text='')