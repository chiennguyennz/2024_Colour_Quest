from tkinter import *
from functools import partial  # To prevent unwanted windows

class ChooseRound:

    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "13", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        self.intro_heading_label = Label(self.intro_frame,
                                         text="Colour Quest",
                                         font=("Arial", "16", "bold")
                                         )
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = "In each round you will be given  " \
                                  "six different colours to choose " \
                                  "from. Pick a colour and see if " \
                                  "you can beat the computer's " \
                                  "score!\n\n" \
                                  "To begin , choose how many rounds " \
                                  "you'd like to play..."
        self.choose_instructions_label = Label(self.intro_frame,
                                               text=choose_instructions_txt,
                                               wraplength=300,
                                               justify="left")
        self.choose_instructions_label.grid(row=1)

        # Round buttons...
        self.how_many_frame = Frame(self.intro_frame)
        self.how_many_frame.grid(row=2)

        self.three_button = Button(self.how_many_frame,
                                   text="3 Rounds",
                                   bg="CC0000",
                                   fg=button_fg,
                                   font=button_font, width=10,
                                   )
        self.three_button.grid(row=0, column=0, padx=5, pady=5)

        self.five_button = Button(self.how_many_frame,
                                  text="5 Rounds",
                                  bg="#009900",
                                  fg=button_fg,
                                  font=button_font, width=10,
                                  )
        self.five_button.grid(row=0, column=1, padx=5, pady=5)

        self.ten_button = Button(self.how_many_frame,
                                 text="10 Rounds",
                                 bg="#000099",
                                 fg=button_fg,
                                 font=button_font,
                                 width=10,
                                 )
        self.ten_button.grid(row=0, column=2, padx=5, pady=5)