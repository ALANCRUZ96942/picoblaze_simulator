import tkinter as tk
from tkinter import ttk
from tkinter import font
import tkinter
from turtle import right
import sys
import subprocess


from lexer import PicoBlaze
from chlorophyll import CodeView

import os
import errno

import principal

start = 0
consolas = 'Consola'

if(start == 0):
    name = input("Enter file name : ")
    start = 1






arg1 = 0
arg2 = ''

def save_code(code):

    try:
        os.mkdir('programs')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    text_file = open('programs/'+name+ '.psm', "w")
    #write string to file
    text_file.write(code)
    
    #close file
    text_file.close()


def verify_code():
    global consolas
    arg2 = name
    subprocess.call(['python','principal.py',str(arg1),str(arg2)])
    print(principal.main)
        
        
        
    
    
    
def exec_by_line(linea):
    linea.tag_add('sel', 'insert linestart', 'insert lineend')



root = tk.Tk()
root.title("Code Editor")
root.option_add("*tearOff", 0)


main_bar = tk.Frame()
main_bar.pack(fill="x") #Configurar el metodo pack()


left_frame = tk.Frame(root)
left_frame.pack_propagate(False)
left_frame.configure(width=100)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

etiqueta1 = tk.Label(left_frame,text="Status")
etiqueta1.pack(fill="x")

zeroFlag = tk.IntVar()
cbZero = tk.Checkbutton(left_frame, text="Zero", variable=zeroFlag).pack(anchor = "w")
carryFlag = tk.IntVar()
cbCarry = tk.Checkbutton(left_frame, text="Carry", variable=carryFlag).pack(anchor = "w")
enabledFlag = tk.IntVar()
cbEnabled = tk.Checkbutton(left_frame, text="Enabled", variable=enabledFlag).pack(anchor = "w")


etiqueta2 = tk.Label(left_frame,text="Interrupt")
etiqueta2.pack(fill="x")

steadyInt = tk.IntVar()
cbSteady = tk.Checkbutton(left_frame, text="Steady", variable=steadyInt).pack(anchor = "w") # anchor the pack for ttk.



edgeFlag = tk.IntVar()
cbEdge = tk.Checkbutton(left_frame, text="Edge",justify="left", variable=edgeFlag).pack(anchor = "w")

timmerFlag = tk.IntVar()
cbTimmer = tk.Checkbutton(left_frame, text="Timmer", variable=timmerFlag).pack(anchor = "w")

timmer_value = tk.Entry(left_frame,width=5).pack(anchor="w",padx=6)


etiqueta3 = tk.Label(left_frame,text="Registers")
etiqueta3.pack(fill="x")

register_frame = tk.Frame(left_frame)
register_frame.pack_propagate(False)
register_frame.configure(width=100)
register_frame.pack(side=tk.LEFT, fill=tk.Y)


#first row
r0_label = tk.Label(register_frame,text="0")
r0_value = tk.Entry(register_frame,width=5)
r8_value = tk.Entry(register_frame,width=5)
r8_label = tk.Label(register_frame,text="8")

r0_label.grid(row=0,column=0)
r0_value.grid(row=0,column=1)
r8_value.grid(row=0,column=2)
r8_label.grid(row=0,column=3)

#second row
r1_label = tk.Label(register_frame,text="1")
r1_value = tk.Entry(register_frame,width=5)
r9_value = tk.Entry(register_frame,width=5)
r9_label = tk.Label(register_frame,text="9")

r1_label.grid(row=1,column=0)
r1_value.grid(row=1,column=1)
r9_value.grid(row=1,column=2)
r9_label.grid(row=1,column=3)

#third row
r2_label = tk.Label(register_frame,text="2")
r2_value = tk.Entry(register_frame,width=5)
rA_value = tk.Entry(register_frame,width=5)
rA_label = tk.Label(register_frame,text="A")

r2_label.grid(row=2,column=0)
r2_value.grid(row=2,column=1)
rA_value.grid(row=2,column=2)
rA_label.grid(row=2,column=3)

#fourth row
r3_label = tk.Label(register_frame,text="3")
r3_value = tk.Entry(register_frame,width=5)
rB_value = tk.Entry(register_frame,width=5)
rB_label = tk.Label(register_frame,text="B")

r3_label.grid(row=3,column=0)
r3_value.grid(row=3,column=1)
rB_value.grid(row=3,column=2)
rB_label.grid(row=3,column=3)

#fiveth row
r4_label = tk.Label(register_frame,text="4")
r4_value = tk.Entry(register_frame,width=5)
rC_value = tk.Entry(register_frame,width=5)
rC_label = tk.Label(register_frame,text="C")

r4_label.grid(row=4,column=0)
r4_value.grid(row=4,column=1)
rC_value.grid(row=4,column=2)
rC_label.grid(row=4,column=3)

#sixth row
r5_label = tk.Label(register_frame,text="5")
r5_value = tk.Entry(register_frame,width=5)
rD_value = tk.Entry(register_frame,width=5)
rD_label = tk.Label(register_frame,text="D")

r5_label.grid(row=5,column=0)
r5_value.grid(row=5,column=1)
rD_value.grid(row=5,column=2)
rD_label.grid(row=5,column=3)

#seventh row
r6_label = tk.Label(register_frame,text="6")
r6_value = tk.Entry(register_frame,width=5)
rE_value = tk.Entry(register_frame,width=5)
rE_label = tk.Label(register_frame,text="E")

r6_label.grid(row=6,column=0)
r6_value.grid(row=6,column=1)
rE_value.grid(row=6,column=2)
rE_label.grid(row=6,column=3)

#eighth row
r7_label = tk.Label(register_frame,text="7")
r7_value = tk.Entry(register_frame,width=5)
rF_value = tk.Entry(register_frame,width=5)
rF_label = tk.Label(register_frame,text="F")

r7_label.grid(row=7,column=0)
r7_value.grid(row=7,column=1)
rF_value.grid(row=7,column=2)
rF_label.grid(row=7,column=3)








central = tk.Frame(root)
central.pack(side=tk.LEFT, fill=tk.Y) #Configurar el metodo pack()
notebook = ttk.Notebook(central)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text=name)
notebook.pack(fill="both", expand=True)




codeview = CodeView(central, lexer=PicoBlaze, color_scheme="monokai")
codeview.pack(fill="both", expand=True)

path = "./programs/"+str(name)+".psm"
 

isFile = os.path.isfile(path)


if(isFile):
    with open(path) as f:
        contents = f.read()
        codeview.insert('1.0',contents)




back_frame = tk.Frame(root)
back_frame.pack_propagate(False)
back_frame.configure(width=100,height=200)
back_frame.pack(side=tk.BOTTOM, fill=tk.X)

etiqueta5 = tk.Label(back_frame,text="Consola")
etiqueta5.pack(fill="x")

my_string_var = tk.StringVar()
my_string_var.set("Nothing to update")

consola = tk.Label(back_frame,textvariable =my_string_var)






"""
Texto = tk.Text(back_frame)
#Texto.insert(tk.END, "prubeasdasdasd")

Texto.insert(tk.END,consolas)
Texto.pack(fill="x",padx=10,pady=10)"""





r_btn_image = tk.PhotoImage(file = r"assets\save.png")
photoimage = r_btn_image.subsample(12, 12)
run_btn = tk.Button(main_bar, text='Run Code',  fg='lime',
                    font=('Bold', 15),image=photoimage,
                    command=lambda:
                     
                    save_code(codeview.get('1.0', tk.END))
        
                    )
run_btn.grid(row=0,column=0)



r_btn_image2 = tk.PhotoImage(file = r"assets\run.png")
photoimage2 = r_btn_image2.subsample(25, 25)
run_btn2 = tk.Button(main_bar, text='Run Code',  fg='lime',
                    font=('Bold', 15),image=photoimage2,
                    
                    command=lambda: verify_code())
run_btn2.grid(row=0,column=1)





r_btn_image3 = tk.PhotoImage(file = r"assets\run.png")
photoimage3 = r_btn_image3.subsample(25, 25)
run_btn3 = tk.Button(main_bar, text='Run Code',  fg='lime',
                    font=('Bold', 15),image=photoimage3,
                    
                    command=lambda: exec_by_line(codeview))
                    
run_btn3.grid(row=0,column=2)







right_frame = tk.Frame(root)
right_frame.pack_propagate(False)
right_frame.configure(width=200)
right_frame.pack(side=tk.LEFT, fill=tk.Y)

etiqueta4 = tk.Label(right_frame,text="InputPort")
etiqueta4.pack(anchor="w")

consola.pack(fill="x")

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()