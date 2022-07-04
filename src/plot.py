import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# RESULTS_PATH = "results/results.csv"
RESULTS_PATH = "results/results_ttables.csv"

Q_COLS = ['session', 'q_num', 'q_operator', 'q_operand_1', 'q_operand_2']


def boxplot_q_group(group_col:str):
    df_operator_group = df_results.groupby(Q_COLS)

    df_op = pd.DataFrame(df_operator_group["q_ts_start"].min())
    df_op["q_ts_end"] = pd.DataFrame(df_operator_group["q_ts_end"].max())
    df_op["q_time_total"] = df_op["q_ts_end"] - df_op["q_ts_start"]

    # df_op["q_time_total"] *= 1000

    df_op = df_op.reset_index(drop=False)
    # print(df_op)

    mean_q_time = df_op.groupby([group_col])["q_time_total"].mean()
    print(mean_q_time)

    import seaborn as sns
    sns.boxplot(x=group_col, y="q_time_total", data=df_op)

    # plt.yscale('log')
    plt.show()



def plot_q_num():
    q_ans_y = np.array(list(df_results.groupby(['session'])["q_num"].max() - 1))
    q_ans_x = np.array(list(range(len(q_ans_y))))

    plt.xlabel("Session No.")
    plt.ylabel("Questions Answered")
    plt.ylim(0, max(q_ans_y))

    m, b = np.polyfit(q_ans_x, q_ans_y, 1)
    plt.plot(q_ans_x, m*q_ans_x + b)

    plt.plot(q_ans_y)

    plt.show()


df_results = pd.read_csv(RESULTS_PATH)
# print(df_results)

# boxplot_q_group("q_operator")
# boxplot_q_group("q_operand_1")
# boxplot_q_group("session")

plot_q_num()

