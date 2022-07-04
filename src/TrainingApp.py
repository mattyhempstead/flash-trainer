import sys
import random
import time
import os
import curses
import pandas as pd
import numpy as np
from typing import Optional

from Results import Results
from Question import Question
from QuestionFactory import QuestionFactory


KEY_ENTER = ord("\n")
KEY_BACKSPACE = curses.KEY_BACKSPACE
KEY_NUM = {ord(str(i)):i for i in range(10)}
KEY_Q = ord("q")


class TrainingApp:
    SESSION_LENGTH = 120
    TIMER_FLASH = 0.2
    FPS = 10


    def __init__(self, question_factory:QuestionFactory, results:Results):
        self.time_start = time.time()
        self.time_end = self.time_start + self.SESSION_LENGTH
        self.time_start_q = None

        self.total = 0
        self.correct = 0

        self.stdscr = None

        self.i_answer = ""

        self.q_num = 0
        self.question_factory:QuestionFactory = question_factory
        self.question:Question = None

        self.wrong_timer = 0
        self.correct_timer = 0

        self.results = results

        self.session = self.results.last_s_num + 1




    def next_question(self):
        self.time_start_q = time.time()

        self.q_num += 1
        self.question = self.question_factory.generate()


    @property
    def time_total(self):
        return time.time() - self.time_start
    
    @property
    def time_remaining(self):
        return self.time_end - time.time()

    @property
    def time_question(self):
        return time.time() - self.time_start_q

    @property
    def wrong_flash(self):
        return time.time() < self.wrong_timer

    @property
    def correct_flash(self):
        return time.time() < self.correct_timer

    @property
    def q_color(self):
        if self.wrong_flash:
            return 3
        elif self.correct_flash:
            return 4
        else:
            return 6

    @property
    def i_answer_int(self) -> Optional[int]:
        if self.i_answer == "":
            return None
        else:
            return int(self.i_answer)

    def clear_input(self):
        self.i_answer = ""

    def submit_answer(self):
        self.results.append_result(
            s_num = self.session,
            s_ts_start = self.time_start,
            s_ts_end = self.time_end,
            q_ts_start = self.time_start_q,
            q_ts_end = time.time(),
            q_num = self.q_num,
            q = self.question,
            i_answer = self.i_answer_int,
        )

        self.total += 1

        if self.question.check_answer(self.i_answer_int):
            self.correct += 1
            self.next_question()
            self.correct_timer = time.time() + self.TIMER_FLASH
        else:
            self.wrong_timer = time.time() + self.TIMER_FLASH


    def check_end(self):
        if self.time_remaining <= 0:
            self.end_session()

    def end_session(self):
        self.clear_input()
        self.submit_answer()
        exit()


    def submit_input(self, k:int):
        if k == KEY_Q:
            self.end_session()
        elif k == KEY_ENTER:
            if self.i_answer != "":
                self.submit_answer()
                self.clear_input()
        elif k == KEY_BACKSPACE:
            self.i_answer = self.i_answer[:-1]
        elif k in KEY_NUM.keys():
            self.i_answer += str(KEY_NUM[k])

    
    def main(self):
        curses.wrapper(self.draw_menu)


    def draw_menu(self, stdscr):
        self.stdscr = stdscr

        k = 0

        # Clear and refresh the screen for a blank canvas
        self.stdscr.clear()
        self.stdscr.refresh()

        # Timeout for inputs
        # -1 is returned if nothing is pressed
        self.stdscr.timeout(int(1000 / self.FPS))

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)


        self.next_question()


        # Loop where k is the last character pressed
        while True:

            # Initialization
            self.stdscr.clear()
            height, width = self.stdscr.getmaxyx()

            self.submit_input(k)

            self.check_end()


            title_str = "Quant Training"
            self.draw_text(0, 0, title_str, 2, True)

            self.draw_text(2, 0, f"Session length: {self.SESSION_LENGTH:.0f}s", 1)
            self.draw_text(3, 0, f"Time Remaining: {self.time_remaining:.1f}", 1)
            self.draw_text(4, 0, f"Time Question: {self.time_question:.1f}", 1)

            self.draw_text(6, 0, f"Question Number: {self.correct}", 1)
            self.draw_text(7, 0, f"Total Guesses: {self.total}", 1)

            # Render bottom bar
            bottom_str = "Press 'q' to exit"
            self.draw_text(height-1, 0, bottom_str, 1)


            # Rendering question
            q_str = str(self.question)
            start_x_q = int((width // 2) - (len(q_str) // 2) - len(q_str) % 2)
            start_y_q  = int((height // 2) - 2)
            self.draw_text(start_y_q, start_x_q, q_str, self.q_color)

            # Print rest of text
            i_answer_str = "= " + f"{self.i_answer:4}"
            start_x_i = int((width // 2) - (len(i_answer_str) // 2) - len(i_answer_str) % 2)
            self.draw_text(start_y_q + 2, start_x_i, i_answer_str, 1)

            stdscr.move(height-1, width-1)

            # Refresh the screen
            stdscr.refresh()

            # Wait for next input
            k = stdscr.getch()


    def draw_text(self, y, x, text, color, bold=False):
        self.stdscr.attron(curses.color_pair(color))
        if bold:
            self.stdscr.attron(curses.A_BOLD)
        else:
            self.stdscr.attroff(curses.A_BOLD)

        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.A_BOLD)

