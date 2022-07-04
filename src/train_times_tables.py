from QuestionFactory import QuestionFactory
from Results import Results

from TrainingApp import TrainingApp


class TimesTablesQuestionFactory(QuestionFactory):
    OPERATORS = ["*"]

    MULDIV_RANGE_1 = [2, 12]
    MULDIV_RANGE_2 = [2, 12]


if __name__ == '__main__':
    qf = TimesTablesQuestionFactory()
    results = Results(file_name="results_ttables")

    app = TrainingApp(
        question_factory=qf,
        results=results
    )
    app.main()
