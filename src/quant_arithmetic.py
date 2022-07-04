from QuestionFactory import QuestionFactory
from Results import Results

from TrainingApp import TrainingApp


class QuantArithmeticQuestionFactory(QuestionFactory):
    OPERATORS = ["+", "-", "*", "/"]

    ADDSUB_RANGE_1 = [2, 100]
    ADDSUB_RANGE_2 = [2, 100]

    MULDIV_RANGE_1 = [2, 12]
    MULDIV_RANGE_2 = [2, 100]



if __name__ == '__main__':
    qf = QuantArithmeticQuestionFactory()
    results = Results(file_name="results_quant")

    app = TrainingApp(
        question_factory=qf,
        results=results
    )
    app.main()

