
class Question:

    OPERATOR_SYMBOLS = {
        "+": "+",
        "-": "-",
        "*": "×",
        "/": "÷",
    }

    def __init__(self, operator, operand_1, operand_2, answer):
        
        self.operator = operator

        self.operand_1 = operand_1
        self.operand_2 = operand_2

        self.answer = answer

    @property
    def operator_symbol(self):
        return self.OPERATOR_SYMBOLS[self.operator]

    def __str__(self, include_answer:bool = False):
        s = f"{self.operand_1} {self.operator_symbol} {self.operand_2}"
        if include_answer:
            s += f" = {self.answer}"
        return s


    def check_answer(self, answer_guess:int):
        return answer_guess == self.answer

