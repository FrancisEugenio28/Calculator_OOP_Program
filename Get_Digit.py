class GetDigit:
        def get_digit(self, digit, Num_Input):
            current = Num_Input['text']
            new = current + str(digit)
            Num_Input.config(text=new)