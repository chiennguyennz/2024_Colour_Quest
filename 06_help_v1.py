from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random

class ChooseRounds:
    def __init__(self):
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)
        root.withdraw()

class Play:
    def __init__(self, how_many):
        self.play_box = Toplevel()
        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()
        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        control_buttons = [
            ["#CC6600", "Help", self.get_help],
            ["#004C99", "Statistics", self.get_stats],
            ["#808080", "Start Over", self.start_over]
        ]

        self.control_button_ref = []

        for item in range(0, 3):
            self.make_control_button = Button(self.control_frame,
                                              fg="#FFFFFF",
                                              bg=control_buttons[item][0],
                                              text=control_buttons[item][1],
                                              width=11, font=("Arial", "12", "bold"),
                                              command=control_buttons[item][2])
            self.make_control_button.grid(row=0, column=item, padx=5, pady=5)
            self.control_button_ref.append(self.make_control_button)

        self.to_help_btn = self.control_button_ref[0]

    def get_help(self):
        DisplayHelp(self)

    def get_stats(self):
        pass

    def start_over(self):
        pass

class DisplayHelp:
    def __init__(self, partner):
        background =  "#ffe6cc"
        self.help_box = Toplevel()
        partner.to_help_btn.config(state=DISABLED)
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))
        self.help_frame = Frame(self.help_box, width=300,
                                height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="Help / Hints",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "Your goal in this game is to beat the computer " \
                    "and you have an advantage - you get to choose " \
                    "your colour first. The points associated with " \
                    "the colours are based on the colour's hex code.\n " \
                    "The higher the value of the colour, the greater" \
                    "your score. To see your statistics, click on " \
                    "the 'Statistics' button. \n\n" \
                    "Win the game by scoring more than the computer " \
                    "overall. Don't be discouraged if you don't win each" \
                    "round, it's your overall score that counts. \n\n" \
                    "Good luck! Choose carefully"
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                               partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_help(self, partner):
        partner.to_help_btn.config(state=NORMAL)
        self.help_box.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()
