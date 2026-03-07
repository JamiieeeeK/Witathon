
# import tkinter as tk 
# from tkinter import *


# theme = ["#000000","#9CB5D6","#A0BBDC","#D1DDEC","#DEE7F2","#E8EEF6"]

# window = tk.Tk()   
# window.title("LifeReality") 
# #window.iconbitmap('app_icon.ico') 

# window_width = window.winfo_screenwidth()
# window_height = window.winfo_screenheight()

# window.resizable(False, False)

# main_frame = tk.Frame(window, bg=theme[3],height=window_height, width=window_width) 
# main_frame.pack(fill='both', expand=True) 
# main_frame.pack_propagate(False) 

# dialogue_width = 1000
# summary_width = window_width - dialogue_width

# summary_frame = tk.Frame(main_frame, bg=theme[5],height=window_height, width=summary_width, borderwidth=2, relief="groove") 
# summary_frame.pack(fill='x', expand=True, side="left") 
# summary_frame.pack_propagate(False) 

# dialogue_frame = tk.Frame(main_frame, bg=theme[4],height=window_height, width=dialogue_width, borderwidth=2, relief="groove") 
# dialogue_frame.pack(fill='x', expand=True, side="right") 
# dialogue_frame.pack_propagate(False) 

# summary_box = Text(summary_frame, width=40, height=10)

# window.mainloop()

import tkinter as tk
from game_logic import Game

theme = ["#000000", "#9CB5D6", "#A0BBDC", "#D1DDEC", "#DEE7F2", "#E8EEF6"]


class LifeRealityUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LifeReality")
        self.root.geometry("1200x700")
        self.root.resizable(False, False)

        self.game = Game()

        self.main_frame = tk.Frame(root, bg=theme[3])
        self.main_frame.pack(fill="both", expand=True)

        self.summary_frame = tk.Frame(self.main_frame, bg=theme[5], width=300)
        self.summary_frame.pack(fill="y", side="left")
        self.summary_frame.pack_propagate(False)

        self.dialogue_frame = tk.Frame(self.main_frame, bg=theme[4])
        self.dialogue_frame.pack(fill="both", expand=True, side="right")

        self.summary_label = tk.Label(
            self.summary_frame,
            text="",
            bg=theme[5],
            justify="left",
            font=("Arial", 14)
        )
        self.summary_label.pack(padx=20, pady=20, anchor="nw")

        self.text_label = tk.Label(
            self.dialogue_frame,
            text="",
            bg=theme[4],
            wraplength=700,
            justify="left",
            font=("Arial", 18)
        )
        self.text_label.pack(padx=30, pady=30, anchor="nw")

        self.choices_frame = tk.Frame(self.dialogue_frame, bg=theme[4])
        self.choices_frame.pack(padx=30, pady=20, anchor="nw")

        self.render_scene()

    def clear_choices(self):
        for widget in self.choices_frame.winfo_children():
            widget.destroy()

    def on_choice_click(self, choice_index):
        self.game.make_choice(choice_index)
        self.render_scene()

    def render_scene(self):
        scene = self.game.get_current_scene()

        self.text_label.config(text=scene["text"])
        self.summary_label.config(text=self.game.get_summary())

        self.clear_choices()

        if not scene["choices"]:
            end_label = tk.Label(
                self.choices_frame,
                text="End of this path.",
                bg=theme[4],
                font=("Arial", 14)
            )
            end_label.pack(anchor="w")
            return

        for i, choice in enumerate(scene["choices"]):
            btn = tk.Button(
                self.choices_frame,
                text=choice["text"],
                command=lambda idx=i: self.on_choice_click(idx),
                width=25
            )
            btn.pack(anchor="w", pady=5)


root = tk.Tk()
app = LifeRealityUI(root)
root.mainloop()