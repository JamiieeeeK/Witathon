import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from game_logic import Game
from API import summary

theme = ["#000000", "#9CB5D6", "#A0BBDC", "#D1DDEC", "#DEE7F2", "#E8EEF6", "#8fa7bf"]

class LifeRealityUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Paths")

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.script_dir, "healthy.ico")

        # self.window.iconbitmap(self.icon_path)
        self.window.resizable(False, False)

        self.game = Game()

        self.window_width = 1400
        self.window_height = 1000

        # self.window_width = window.winfo_screenwidth()
        # self.window_height = window.winfo_screenheight()

        center_x = int(self.window_width /2 - self.window_width /2)
        center_y = int(self.window_height /2 - self.window_height /2)

        # self.window_width = 1400
        # self.window_height = 900

        # screen_width = window.winfo_screenwidth()
        # screen_height = window.winfo_screenheight()

        # center_x = int((screen_width / 2) - (self.window_width / 2))
        # center_y = int((screen_height / 2) - (self.window_height / 2))

        self.window.geometry(f"{self.window_width}x{self.window_height}+{center_x}+{center_y}")

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
        
        # self.authorization_page.pack(fill="both", expand=True)
        self.authorization_page.pack_propagate(False)

        # -------- TITLE FRAME --------
        self.title_author = tk.Frame(
            self.authorization_page,
            bg=self.authorization_page.cget("bg"),
            height=200,
            width=self.window_width
        )
        self.title_author.pack(fill="x", side="top")
        self.title_author.pack_propagate(False)

        self.author_label = tk.Label(
            self.title_author,
            text="Create your character",
            font=("Impact", 40),
            fg="black",
            bg=self.authorization_page.cget("bg")
        )
        self.author_label.pack(pady=40)

        # -------- CONTENT FRAME --------

        self.page_author = tk.Frame(
            self.authorization_page,
            bg=self.authorization_page.cget("bg"),
            height=self.window_height - 200,
            width=self.window_width
        )
        self.page_author.pack(fill="both", expand=True)
        self.page_author.pack_propagate(False)


        self.content_author = tk.Frame(
            self.page_author,
            bg=self.authorization_page.cget("bg"),
        )
        self.content_author.pack(fill="both", expand=True, anchor="center", pady=10)

        # Center everything inside
        self.content_author.pack_propagate(False)

        # NAME LABEL
        self.name_label = tk.Label(
            self.content_author,
            text="Input your name:",
            font=("Impact", 20),
            fg="black",
            bg=self.authorization_page.cget("bg"),
            anchor="center",
            justify="center"
        )
        self.name_label.pack(pady=15)

        self.name = tk.StringVar()
        self.name.get()

        # NAME ENTRY
        self.name_entry = tk.Entry(
            self.content_author,
            textvariable=self.name,
            font=("Impact", 20),
            width=20,
            justify="center"
        )
        self.name_entry.pack(pady=20)

        # GENDER LABEL
        self.gender_label = tk.Label(
            self.content_author,
            text="Choose your gender:",
            font=("Impact", 20),
            fg="black",
            bg=self.authorization_page.cget("bg"),
            anchor="center",
            justify="center"
        )
        self.gender_label.pack(pady=15)

        self.gender = tk.StringVar()

        # RADIOBUTTON FRAME
        self.frame = tk.Frame(
            self.content_author,
            bg=self.authorization_page.cget("bg")
        )
        self.frame.pack(pady=10)

        self.gender.set("") 

        # RADIOBUTTONS
        tk.Radiobutton(
            self.frame,
            text="Boy",
            variable=self.gender,
            value="Boy",
            font=("Impact", 20),
            activebackground="#63b3ed",
            activeforeground="white",
            bg=self.authorization_page.cget("bg")
        ).pack(side="left", padx=50)

        tk.Radiobutton(
            self.frame,
            text="Girl",
            variable=self.gender,
            value="Girl",
            font=("Impact", 20),
            activebackground="#63b3ed",
            activeforeground="white",
            bg=self.authorization_page.cget("bg")
        ).pack(side="left", padx=50)

        tk.Radiobutton(
            self.frame,
            text="Prefer not to say",
            variable=self.gender,
            value="Other",
            font=("Impact", 20),
            activebackground="#63b3ed",
            activeforeground="white",
            bg=self.authorization_page.cget("bg")
        ).pack(side="left", padx=50)

        self.next_button = tk.Button(
            self.content_author,
            text="Next",
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
            command=self.game_next       
        )
        self.next_button.pack(pady=30)

        # -------- PAGE 3 -------------

        self.main_frame = tk.Frame(
            self.frames,
            bg=theme[3],
            height=self.window_height,
            width=self.window_width
        )
        self.main_frame.pack_propagate(False)

        # -------- TITLE --------
        self.title_frame = tk.Frame(
            self.main_frame,
            bg=theme[3],
            height=80,
            width=self.window_width
        )
        self.title_frame.pack(fill="x", side="top", pady=(100,0))
        self.title_frame.pack_propagate(False)

        self.title_stage = tk.Label(
            self.title_frame,
            text="Paths",
            font=("Impact", 35),
            fg="black",
            bg=theme[3]
        )
        self.title_stage.pack(pady=15)

        # -------- CENTER WRAPPER --------
        self.center_wrapper = tk.Frame(
            self.main_frame,
            bg=theme[3],
            width=1150,
            height=850
        )
        self.center_wrapper.place(relx=0.5, rely=0.18, anchor="n")
        self.center_wrapper.pack_propagate(False)

        # -------- LEFT SUMMARY --------
        self.summary_frame = tk.Frame(
            self.center_wrapper,
            bg=theme[4],
            width=230,
            height=620
        )
        self.summary_frame.pack(side="left", padx=(0, 25), anchor="n")
        self.summary_frame.pack_propagate(False)

        self.summary_box = tk.Text(
            self.summary_frame,
            wrap="word",
            font=("Helvetica", 14),
            padx=16,
            pady=16,
            relief="flat",
            bd=0,
            highlightthickness=0,
            bg="#f7f7f7",
            fg="black"
        )
        self.summary_box.pack(fill="both", expand=True, padx=12, pady=12)
        self.summary_box.config(state="disabled")

        # -------- RIGHT SIDE --------
        self.right_panel = tk.Frame(
            self.center_wrapper,
            bg=theme[3],
            width=895,
            height=750
        )
        self.right_panel.pack(side="left", anchor="n")
        self.right_panel.pack_propagate(False)

        # -------- DESCRIPTION --------
        self.dialogue_frame = tk.Frame(
            self.right_panel,
            bg=theme[4],
            width=895,
            height=230
        )
        self.dialogue_frame.pack(fill="x")
        self.dialogue_frame.pack_propagate(False)

        self.dialogue_box = tk.Text(
            self.dialogue_frame,
            wrap="word",
            font=("Helvetica", 15),
            padx=18,
            pady=18,
            relief="flat",
            bd=0,
            highlightthickness=0,
            bg="#f7f7f7",
            fg="black"
        )
        self.dialogue_box.pack(fill="both", expand=True, padx=12, pady=12)
        self.dialogue_box.config(state="disabled")

        # -------- BUTTON AREA --------
        
        self.bottom_frame = tk.Frame(
            self.right_panel,
            bg=theme[3],
            width=895,
            height=420
        )
        self.bottom_frame.pack(fill="x", pady=(18, 0))
        self.bottom_frame.pack_propagate(False)

        self.choices_frame = tk.Frame(
            self.bottom_frame,
            bg=theme[3],
            width=895
        )
        self.choices_frame.pack(fill="x")

        self.render_scene()
        
    def game_start(self):
        self.start_page.pack_forget()
        self.authorization_page.pack(fill="both", expand=True)

    def game_next(self):
        player_name = self.name.get()
        self.game.state.name = self.name.get().strip() or "Player"
        self.game.state.gender = self.gender.get()

        self.game.state.name = player_name

        self.authorization_page.pack_forget()
        self.main_frame.pack(fill="both", expand=True)
        self.render_scene()

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

        # if not scene["choices"]:
        #     end_label = tk.Label(
        #         self.choices_frame,
        #         text="End of this path.",
        #         bg=theme[2],
        #         font=("Arial", 14)
        #     )
        #     end_label.pack(anchor="w", pady=5)
        #     return

        if not scene["choices"]:
            end_card = tk.Frame(
                self.choices_frame,
                bg=theme[4],
                height=340
            )
            end_card.pack(fill="x", padx=12, pady=20)
            end_card.pack_propagate(False)

            inner = tk.Frame(end_card, bg="#f7f7f7")
            inner.pack(fill="both", expand=True, padx=8, pady=8)

            end_title = tk.Label(
                inner,
                text="Final Reflection",
                font=("Impact", 24),
                bg="#f7f7f7",
                fg="black"
            )
            end_title.pack(pady=(28, 10))

            end_message = tk.Label(
                inner,
                text="End of this path." + "\n" + "Summary:" + "\n" + summary(getattr(self.state, "summary", "")),
                font=("Helvetica", 15),
                bg="#f7f7f7",
                fg="black",
                wraplength=730,
                justify="center"
            )
            end_message.pack(expand=True, padx=35, pady=(0, 30))

            return

        for i, choice in enumerate(scene["choices"]):
            card = tk.Frame(
                self.choices_frame,
                bg=theme[4],
                height=60,
                cursor="hand2"
            )
            card.pack(fill="x", padx=12, pady=8)
            card.pack_propagate(False)

            inner = tk.Frame(
                card,
                bg="#f7f7f7"
            )
            inner.pack(fill="both", expand=True, padx=6, pady=6)

            label = tk.Label(
                inner,
                text=choice["text"],
                font=("Helvetica", 14, "bold"),
                bg="#f7f7f7",
                fg="black",
                wraplength=760,
                justify="center",
                cursor="hand2"
            )
            label.pack(expand=True)

            def handler(event, idx=i):
                self.on_choice_click(idx)

            card.bind("<Button-1>", handler)
            inner.bind("<Button-1>", handler)
            label.bind("<Button-1>", handler)

            card.bind("<Enter>", lambda e, w=inner: w.config(bg="#efefef"))
            card.bind("<Leave>", lambda e, w=inner: w.config(bg="#f7f7f7"))
            inner.bind("<Enter>", lambda e, w=inner: w.config(bg="#efefef"))
            inner.bind("<Leave>", lambda e, w=inner: w.config(bg="#f7f7f7"))
            label.bind("<Enter>", lambda e, w=inner, l=label: (w.config(bg="#efefef"), l.config(bg="#efefef")))
            label.bind("<Leave>", lambda e, w=inner, l=label: (w.config(bg="#f7f7f7"), l.config(bg="#f7f7f7")))

            def on_choice_click(self, index):
                self.game.make_choice(index)
    
                self.summary_box.config(state="normal")
                self.summary_box.delete("1.0", "end")
                self.summary_box.insert("end", self.game.get_summary())
                self.summary_box.config(state="disabled")
    
                self.dialogue_box.config(state="normal")
                self.dialogue_box.delete("1.0", "end")
                self.dialogue_box.insert("end", self.game.get_current_scene()["text"])
                self.dialogue_box.config(state="disabled")
    
                self.render_choices()

            

root = tk.Tk()
app = LifeRealityUI(root)
root.mainloop()
