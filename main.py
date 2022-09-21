import tkinter as tk
from tkinter import ttk
from tkinter import font

import pygments.lexers
from chlorophyll import CodeView

name=input("Enter file name : ")

root = tk.Tk()
root.title("Code Editor")
root.option_add("*tearOff", 0)


notebook = ttk.Notebook(root)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text=name)
notebook.pack(fill="both", expand=True)



codeview = CodeView(root, lexer=pygments.lexers.CppObjdumpLexer, color_scheme="monokai")
codeview.pack(fill="both", expand=True)


root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()