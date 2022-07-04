import os
import pandas as pd
import numpy as np
from typing import Optional

from Question import Question

class Results:
    FILE_DIR = "../results"

    def __init__(self, file_name:str):
        self.file_name = file_name

        self.df_results = self.read_results()


    @property
    def file_path(self):
        return self.FILE_DIR + "/" + self.file_name + ".csv"


    @property
    def last_s_num(self):
        """
            The last session number in results.
            Returns -1 if no sessions exist.
        """
        if len(self.df_results) == 0:
            return -1
        else:
            return int(max(self.df_results["s_num"]))


    def append_result(
        self,
        s_num: int,
        s_ts_start: float,
        s_ts_end: float,
        q_ts_start: float,
        q_ts_end: float,
        q_num: int,
        q: Question,
        i_answer: int
    ):
        df_result = pd.DataFrame([{
            "s_num": s_num,
            "s_ts_start": s_ts_start,
            "s_ts_end": s_ts_end,
            "q_ts_start": q_ts_start,
            "q_ts_end": q_ts_end,
            "q_num": q_num,
            "q_operator": q.operator,
            "q_operand_1": q.operand_1,
            "q_operand_2": q.operand_2,
            "q_answer": q.answer,
            "i_answer": i_answer,
        }])

        self.df_results = pd.concat(
            [self.df_results, df_result],
            ignore_index=True
        )

        self.write_results()


    def read_results(self):
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        else:
            return pd.DataFrame(
                columns=[
                    "s_num",
                    "s_ts_start",
                    "s_ts_end",
                    "q_ts_start",
                    "q_ts_end",
                    "q_num",
                    "q_operator",
                    "q_operand_1",
                    "q_operand_2",
                    "q_answer",
                    "i_answer",
                ]
            )

    def write_results(self):
        if not os.path.exists(self.FILE_DIR):
            os.mkdir(self.FILE_DIR)

        self.df_results.to_csv(self.file_path, index=False)
