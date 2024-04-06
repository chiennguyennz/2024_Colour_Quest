from tkinter import *
from functools import partial
import csv
import random

# users choose
class ChooseRounds:
    def __init__(self):
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)
        root.withdraw()

class Play:
    def __init__(self, num_rounds):
        self.num_rounds = num_rounds
        self.play_box = Toplevel()

        self.user_scores = [20, 14, 14, 13, 14, 11, 20, 10, 20, 11]
        self.computer_scores = [12, 4, 6, 20, 20, 14, 10, 14, 16, 12]

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        control_buttons = [
            ["#CC6600", "Help", "get help"],
            ["#004C99", "Statistics", "get stats"],
            ["#808080", "Start Over", "start over"]
        ]

        self.control_button_ref = []

        for item in range(0, 3):
            button = Button(self.control_frame,
                            fg="#FFFFFF",
                            bg=control_buttons[item][0],
                            text=control_buttons[item][1],
                            width=11, font=("Arial", "12", "bold"),
                            command=lambda i=item: self.to_do(control_buttons[i][2]))
            button.grid(row=0, column=item, padx=5, pady=5)
            self.control_button_ref.append(button)

        self.to_stats_btn = self.control_button_ref[1]

    def to_do(self, action):
        if action == "get help":
            pass
        elif action == "get stats":
            DisplayStats(self, self.user_scores, self.computer_scores)
        else:
            self.close_play()

    def close_play(self):
        root.destroy()

class DisplayStats:
    def __init__(self, partner, user_scores, computer_scores):
        self.stats_box = Toplevel()
        stats_bg_colour = "#DAE8FC"
        partner.to_stats_btn.config(state=DISABLED)
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        self.stats_frame = Frame(self.stats_box, width=300, height=200, bg=stats_bg_colour)
        self.stats_frame.grid()

        self.help_heading_label = Label(self.stats_frame, text="Statistics", font=("Arial", "14", "bold"), bg=stats_bg_colour)
        self.help_heading_label.grid(row=0)

        stats_text = "Here are your game statistics"
        self.help_text_label = Label(self.stats_frame, text=stats_text, justify="left", bg=stats_bg_colour)
        self.help_text_label.grid(row=1, padx=10)

        self.data_frame = Frame(self.stats_frame, bg=stats_bg_colour, borderwidth=1, relief="solid")
        self.data_frame.grid(row=2, padx=10, pady=10)

        self.user_stats = self.get_stats(user_scores, "User")
        self.comp_stats = self.get_stats(computer_scores, "Computer")

        head_back = "#FFFFFF"
        odd_rows = "#C9D6E8"
        even_rows = stats_bg_colour
        row_names = ["", "Total", "Best Score", "Worst Score", "Average"]
        row_formats = [head_back, odd_rows, even_rows, odd_rows, even_rows]

        all_labels = []

        count = 0
        for item in range(0, len(self.user_stats)):
            all_labels.append([row_names[item], row_formats[count]])
            all_labels.append([self.user_stats[item], row_formats[count]])
            all_labels.append([self.comp_stats[item], row_formats[count]])
            count += 1

        for item in range(0, len(all_labels)):
            self.data_label = Label(self.data_frame, text=all_labels[item][0], bg=all_labels[item][1], width="10", height="2", padx=5)
            self.data_label.grid(row=item // 3, column=item % 3, padx=0, pady=0)

        # Adjust the row index for the dismiss button to be at the bottom
        dismiss_row = len(all_labels) // 3 + 1

        self.dismiss_button = Button(self.stats_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=dismiss_row, column=0, columnspan=3, padx=10, pady=10)

    @staticmethod
    def get_stats(score_list, entity):
        total_score = sum(score_list)
        best_score = max(score_list)
        worst_score = min(score_list)
        average = total_score / len(score_list)

        return [entity, total_score, best_score, worst_score, average]

    def close_stats(self, partner):
        partner.to_stats_btn.config(state=NORMAL)
        self.stats_box.destroy()


    def close_stats(self, partner):
        partner.to_stats_btn.config(state=NORMAL)
        self.stats_box.destroy()


    @staticmethod
    def get_stats(score_list, entity):
        total_score = sum(score_list)
        best_score = max(score_list)
        worst_score = min(score_list)
        average = total_score / len(score_list)

        return [entity, total_score, best_score, worst_score, average]

    def close_stats(self, partner):
        partner.to_stats_btn.config(state=NORMAL)
        self.stats_box.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()
