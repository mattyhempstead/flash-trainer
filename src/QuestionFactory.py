import random
import numpy as np

from Question import Question


class QuestionFactory:

    OPERATORS = ["+", "-", "*", "/"]
    OPERATORS_RATIO = None

    ADDSUB_RANGE_1 = [2, 100]
    ADDSUB_RANGE_2 = [2, 100]

    MULDIV_RANGE_1 = [2, 12]
    MULDIV_RANGE_2 = [2, 100]


    def __init__(self):
        pass


    @property
    def operators_p(self):
        if self.OPERATORS_RATIO is None:
            return None
        else:
            return np.array(self.OPERATORS_RATIO) / sum(self.OPERATORS_RATIO)

    @property
    def generate_operator(self):
        return np.random.choice(self.OPERATORS, p=self.operators_p)

    @property
    def generate_operand_1(self):
        return random.randint(*self.MULDIV_RANGE_1)

    def generate(self) -> Question:
        operator = self.generate_operator

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
            a = self.generate_operand_1
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
