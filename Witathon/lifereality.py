import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from game_logic import Game

theme = ["#000000", "#9CB5D6", "#A0BBDC", "#D1DDEC", "#DEE7F2", "#E8EEF6", "#8fa7bf"]

class LifeRealityUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Paths")

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.script_dir, "healthy.ico")

        self.window.iconbitmap(self.icon_path)
        self.window.resizable(False, False)

        self.game = Game()

        self.window_width = window.winfo_screenwidth()
        self.window_height = window.winfo_screenheight()

        center_x = int(self.window_width /2 - self.window_width /2)
        center_y = int(self.window_height /2 - self.window_height /2)

        self.window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        self.frames = tk.Frame(
            self.window,
            bg=theme[3],
            height=self.window_height,
            width=self.window_width
        )
        self.frames.pack(fill="both", expand=True)
        self.frames.pack_propagate(False)


        # --------- PAGE 1 ------------


        self.start_page = tk.Frame(
            self.frames,
            bg=theme[3],
            height=self.window_height,
            width=self.window_width
        )
        self.start_page.pack(fill="both", expand=True)
        self.start_page.pack_propagate(False)

        self.center_frame = tk.Frame(self.start_page, bg=theme[3])
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center") 

        self.welcome_title = tk.Label(
            self.center_frame,
            text="Welcome to Paths.",
            font=("Impact", 40),
            fg="black",
            bg=self.start_page.cget("bg"),
            justify="center",
            wraplength=700 
        )
        self.welcome_title.pack(anchor="center")

        self.game_description = tk.Label(
            self.center_frame,
            text="This is your story." \
            "\n Every decision you make will shape the life you live — the people you meet, the places you travel, and the career you build." \
            "\n You will choose your background, personality, and ambitions. Some paths will be easy. Others will test your determination." \
            "\n There is no single correct way to play.",
            font=("Impact", 20),
            fg="black",
            bg=self.start_page.cget("bg"),
            wraplength=700,
            justify="center"
        )
        self.game_description.pack(pady=30, anchor="center")

        self.start_button = tk.Button(
            self.center_frame,
            text="Start Game",
            font=("Impact", 20),
            fg="white",            
            bg=theme[6],          
            activebackground="#63b3ed",  
            activeforeground="white",
            relief="raised",       
            bd=5,                  
            padx=20,
            pady=10,
            cursor="hand2",        
            command=self.game_start       
        )
        self.start_button.pack(pady=30)


        # -------- PAGE 2 -------------

        self.authorization_page = tk.Frame(
            self.frames,
            bg=theme[4],
            height=self.window_height,
            width=self.window_width
        )
        
        self.authorization_page.pack(fill="both", expand=True)
        self.authorization_page.pack_propagate(False)

        # -------- TITLE FRAME --------
        self.title_author = tk.Frame(
            self.authorization_page,
            bg=self.authorization_page.cget("bg"),
            height=100,
            width=self.window_width
        )
        self.title_author.pack(fill="x", side="top")
        self.title_author.pack_propagate(False)

        self.author_label = tk.Label(
            self.title_author,
            text="Paths",
            font=("Impact", 40),
            fg="black",
            bg=self.authorization_page.cget("bg")
        )
        self.author_label.pack(pady=15)

        # -------- CONTENT FRAME --------
        self.content_author = tk.Frame(
            self.authorization_page,
            bg=self.authorization_page.cget("bg"),
            height=self.window_height - 200,
            width=self.window_width
        )
        self.content_author.pack(fill="both", expand=True)
        self.content_author.pack_propagate(False)







        # -------- PAGE 3 -------------

        self.dialogue_width = 1050
        self.summary_width = self.window_width - self.dialogue_width

        self.main_frame = tk.Frame(
            self.frames,
            bg=theme[3],
            height=self.window_height,
            width=self.window_width
        )
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.pack_propagate(False)

        # -------- TITLE FRAME --------
        self.title_frame = tk.Frame(
            self.main_frame,
            bg=theme[2],
            height=100,
            width=self.window_width
        )
        self.title_frame.pack(fill="x", side="top")
        self.title_frame.pack_propagate(False)

        self.title_stage = tk.Label(
            self.title_frame,
            text="Paths",
            font=("Impact", 40),
            fg="black",
            bg=theme[2]
        )
        self.title_stage.pack(pady=15)

        # -------- CONTENT FRAME --------
        self.content_frame = tk.Frame(
            self.main_frame,
            bg=theme[3],
            height=self.window_height - 200,
            width=self.window_width
        )
        self.content_frame.pack(fill="both", expand=True)
        self.content_frame.pack_propagate(False)

        # -------- SUMMARY FRAME --------
        self.summary_frame = tk.Frame(
            self.content_frame,
            bg=theme[2],
            height=self.window_height - 200,
            width=self.summary_width
        )
        self.summary_frame.pack(fill="y", side="left")
        self.summary_frame.pack_propagate(False)

        self.text_frame = tk.Frame(self.summary_frame, bg=theme[2])
        self.text_frame.pack(pady=20)

        self.summary_box = tk.Text(self.text_frame, width=40, height=35)
        self.summary_box.pack(side=LEFT, fill="y")

        self.summary_scrollbar = ttk.Scrollbar(
            self.text_frame,
            orient="vertical",
            command=self.summary_box.yview
        )
        self.summary_scrollbar.pack(side=RIGHT, fill=Y)

        self.summary_box.config(yscrollcommand=self.summary_scrollbar.set)
        self.summary_box.config(state="disabled")

        self.dialogue_frame = tk.Frame(
            self.content_frame,
            bg=theme[4],
            height=self.window_height - 200,
            width=self.dialogue_width
        )
        self.dialogue_frame.pack(fill="both", expand=True, side="right")
        self.dialogue_frame.pack_propagate(False)

        self.description_frame = tk.Frame(
            self.dialogue_frame,
            bg=theme[2],
            width=200
        )
        self.description_frame.pack(side="right", fill="y")
        self.description_frame.pack_propagate(False)

        self.main_text_frame = tk.Frame(
            self.dialogue_frame,
            bg=theme[4]
        )
        self.main_text_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=20
        )

        self.dialogue_box = tk.Text(
            self.main_text_frame,
            width=90,
            height=35,
            wrap="word"
        )
        self.dialogue_box.pack(side="left", fill="both", expand=True)

        self.dialogue_scrollbar = ttk.Scrollbar(
            self.main_text_frame,
            orient="vertical",
            command=self.dialogue_box.yview
        )
        self.dialogue_scrollbar.pack(side="right", fill="y")

        self.dialogue_box.config(yscrollcommand=self.dialogue_scrollbar.set)
        self.dialogue_box.config(state="disabled")

        self.choices_frame = tk.Frame(self.description_frame, bg=theme[2])
        self.choices_frame.pack(padx=10, pady=20, anchor="n")

        self.bottom_frame = tk.Frame(
            self.main_frame,
            bg=theme[2],
            height=100,
            width=self.window_width
        )
        self.bottom_frame.pack(fill="x", side="bottom")
        self.bottom_frame.pack_propagate(False)

        self.render_scene()

    def game_start(self):
        self.start_page.pack_forget()


    def clear_choices(self):
        for widget in self.choices_frame.winfo_children():
            widget.destroy()

    def update_summary_box(self):
        self.summary_box.config(state="normal")
        self.summary_box.delete("1.0", tk.END)
        self.summary_box.insert(tk.END, self.game.get_summary())
        self.summary_box.config(state="disabled")

    def update_dialogue_box(self, text):
        self.dialogue_box.config(state="normal")
        self.dialogue_box.delete("1.0", tk.END)
        self.dialogue_box.insert(tk.END, text)
        self.dialogue_box.config(state="disabled")

    def on_choice_click(self, choice_index):
        self.game.make_choice(choice_index)
        self.render_scene()

    def render_scene(self):
        scene = self.game.get_current_scene()

        self.update_dialogue_box(scene["text"])
        self.update_summary_box()

        self.clear_choices()

        if not scene["choices"]:
            end_label = tk.Label(
                self.choices_frame,
                text="End of this path.",
                bg=theme[2],
                font=("Arial", 14)
            )
            end_label.pack(anchor="w", pady=5)
            return

        for i, choice in enumerate(scene["choices"]):
            btn = tk.Button(
                self.choices_frame,
                text=choice["text"],
                command=lambda idx=i: self.on_choice_click(idx),
                width=20
            )
            btn.pack(anchor="w", pady=5)


root = tk.Tk()
app = LifeRealityUI(root)
root.mainloop()
