from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random


# users choose round 3, 5 or 10 rounds
class ChooseRounds:

    def __init__(self):
        # invoke play class with three rounds for testing purposes.
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # Hide root windows (ie: hide rounds choice windows).
        root.withdraw()


class Play:

    def __init__(self, how_many):

        self.play_box = Toplevel()

        # If users press cross at top, closes help and
        # 'release' help button
        self.play_box.protocol('WM_DELETE_WINDOWS',
                               partial(self.close_play))

        # Variables used to work out statistics, when game end etc
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # Intially set rounds played and rounds won to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        # lists to hold users score/s and computer score/s
        # used to work out statistics

        user_scores = []
        computer_scores = []

        # get all the colours for use in game
        self.all_colours = self.all_colours()

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame,
                                    text=rounds_heading,
                                    font=("Arial", "16", "bold")
                                    )
        self.choose_heading.grid(row=0)