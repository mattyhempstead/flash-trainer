import random

from Question import Question


class QuestionFactory:

    OPERATORS = ["+", "-", "*", "/"]

    ADDSUB_RANGE_1 = [2, 100]
    ADDSUB_RANGE_2 = [2, 100]

    MULDIV_RANGE_1 = [2, 12]
    MULDIV_RANGE_2 = [2, 100]


    def __init__(self):
        pass


    def generate(self) -> Question:

        operator = random.choice(self.OPERATORS)

        if operator in ["+", "-"]:
            a = random.randint(*self.ADDSUB_RANGE_1)
            b = random.randint(*self.ADDSUB_RANGE_2)
            c = a + b

            if operator == "+":
                operand_1 = a
                operand_2 = b
                answer = c
            else:
                operand_1 = c
                operand_2 = a
                answer = b

        else:
            a = random.randint(*self.MULDIV_RANGE_1)
            b = random.randint(*self.MULDIV_RANGE_2)
            c = a * b

            if operator == "*":
                operand_1 = a
                operand_2 = b
                answer = c
            else:
                operand_1 = c
                operand_2 = a
                answer = b

        return Question(
            operator=operator,
            operand_1=operand_1,
            operand_2=operand_2,
            answer=answer,
        )
