# Dimensional Analysis code support file
# author: Mohammad Afzal Shadab
# date: 02/18/2021
# email: mashadab@utexas.edu

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global che61
    che61 = tk.IntVar()
    global che62
    che62 = tk.IntVar()
    global che63
    che63 = tk.IntVar()
    global che64
    che64 = tk.IntVar()
    global che65
    che65 = tk.IntVar()
    global che66
    che66 = tk.IntVar()
    global che67
    che67 = tk.IntVar()
    global che68
    che68 = tk.IntVar()
    global che69
    che69 = tk.IntVar()
    global che70
    che70 = tk.IntVar()
    global che71
    che71 = tk.IntVar()
    global che72
    che72 = tk.IntVar()
    global che73
    che73 = tk.IntVar()
    global che74
    che74 = tk.IntVar()
    global che75
    che75 = tk.IntVar()
    global che76
    che76 = tk.IntVar()
    global che77
    che77 = tk.IntVar()
    global che78
    che78 = tk.IntVar()
    global che79
    che79 = tk.IntVar()
    global che80
    che80 = tk.IntVar()
    global che81
    che81 = tk.IntVar()
    global che82
    che82 = tk.IntVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    from dimensional_analysis import solve_lin_sys
    solve_lin_sys.vp_start_gui()




