from tkinter import ttk
import tkinter as tk 
from tkinter import *


theme = ["#000000","#9CB5D6","#A0BBDC","#D1DDEC","#DEE7F2","#E8EEF6"]

window = tk.Tk()   
window.title("LifeReality") 
#window.iconbitmap('app_icon.ico') 

window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()

window.resizable(False, False)

main_frame = tk.Frame(window, bg=theme[3],height=window_height, width=window_width) 
main_frame.pack(fill='both', expand=True) 
main_frame.pack_propagate(False) 

dialogue_width = 1050
summary_width = window_width - dialogue_width

########## TITLE FRAME ####################

title_frame = tk.Frame(main_frame, bg=theme[2],height=100, width=summary_width) 
title_frame.pack(fill='x', expand=True, side="top")
title_frame.pack_propagate(False) 

title_stage = tk.Label(
    title_frame,
    text="blablabla",
    font=("Impact", 40),  
    fg="black",         
    bg= title_frame.cget("bg")           
)
title_stage.pack(pady=15)

################ MIDDLE FRAME ################




######## SUMMARY FRAME#####################

summary_frame = tk.Frame(main_frame, bg=theme[2],height=window_height-title_frame.winfo_height()*2, width=summary_width) 
summary_frame.pack(fill='x', expand=True, side="left")
summary_frame.pack_propagate(False) 

text_frame = Frame(summary_frame)
text_frame.pack(pady=20)

summary_box = Text(text_frame, width=40, height=35)
summary_box.pack(side=LEFT, fill='y')  

summary_scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=summary_box.yview)
summary_scrollbar.pack(side=RIGHT, fill=Y)  

summary_box.config(yscrollcommand=summary_scrollbar.set)
summary_box.config(state='disabled')

############## DIALOGUE FRAME #####################

dialogue_frame = tk.Frame(main_frame, bg=theme[4], height=window_height-title_frame.winfo_height()*2, width=dialogue_width)
dialogue_frame.pack(fill='none', expand=True, side="right")
dialogue_frame.pack_propagate(False)

description_frame = tk.Frame(dialogue_frame, bg=theme[2], height=70, width=200)
description_frame.pack(side="right", fill='y')
description_frame.pack_propagate(False)

main_text_frame = tk.Frame(dialogue_frame, height=70, width=100)
main_text_frame.pack(side="left", anchor="n", fill='none', expand=True, padx=5, pady=20)

dialogue_box = tk.Text(main_text_frame, width=90, height=35)
dialogue_box.pack(side="left", fill='both', expand=True)

dialogue_scrollbar = ttk.Scrollbar(main_text_frame, orient='vertical', command=dialogue_box.yview)
dialogue_scrollbar.pack(side="right", fill='y')

dialogue_box.config(yscrollcommand=dialogue_scrollbar.set)
dialogue_box.config(state='disabled')

############# BOTTOM FRAME ##################

bottom_frame = tk.Frame(main_frame, bg=theme[2],height=title_frame.winfo_height(), width=summary_width) 
bottom_frame.pack(fill='x', expand=True, side="bottom")
bottom_frame.pack_propagate(False) 


window.mainloop()