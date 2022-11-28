import tkinter as tk


def copy_line(event=None):
    data = text.get('insert linestart', 'insert lineend')
    root.clipboard_clear()
    root.clipboard_append(data)


def select_line(event=None):
    # `sel` is a special tag name that represents the current selection if any
    text.tag_add('sel', 'insert linestart', 'insert lineend')


root = tk.Tk()

text = tk.Text(root)
text.pack()

text.bind('<Control-q>', copy_line)
text.bind('<Control-e>', select_line)

root.mainloop()