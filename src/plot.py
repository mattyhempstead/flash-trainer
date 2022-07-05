import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Results import Results



def boxplot_q_group(group_col:str):
    df_q = results.df_q
    # print(df_op)

    mean_q_time = df_q.groupby([group_col])["q_time_total"].mean()
    print(mean_q_time)

    import seaborn as sns
    sns.boxplot(x=group_col, y="q_time_total", data=df_q)

    # plt.yscale('log')
    plt.show()



def plot_q_num():
    q_ans_y = np.array(list(results.df_results.groupby(['s_num'])["q_num"].max() - 1))
    q_ans_x = np.array(list(range(len(q_ans_y))))

    plt.xlabel("Session No.")
    plt.ylabel("Questions Answered")
    plt.ylim(0, max(q_ans_y))

    m, b = np.polyfit(q_ans_x, q_ans_y, 1)
    plt.plot(q_ans_x, m*q_ans_x + b)

    plt.plot(q_ans_y)

    plt.show()


results = Results("results_ttables")

# results.df_q_operand_time

# boxplot_q_group("q_operator")
# boxplot_q_group("q_operand_1")
# boxplot_q_group("q_operand_2")
# boxplot_q_group("s_num")
# boxplot_q_group("q_answer")
boxplot_q_group("q_num")

# plot_q_num()

