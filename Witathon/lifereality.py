
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

dialogue_width = 1000
summary_width = window_width - dialogue_width

summary_frame = tk.Frame(main_frame, bg=theme[5],height=window_height, width=summary_width, borderwidth=2, relief="groove") 
summary_frame.pack(fill='x', expand=True, side="left") 
summary_frame.pack_propagate(False) 

dialogue_frame = tk.Frame(main_frame, bg=theme[4],height=window_height, width=dialogue_width, borderwidth=2, relief="groove") 
dialogue_frame.pack(fill='x', expand=True, side="right") 
dialogue_frame.pack_propagate(False) 

summary_box = Text(summary_frame, width=40, height=10)

window.mainloop()