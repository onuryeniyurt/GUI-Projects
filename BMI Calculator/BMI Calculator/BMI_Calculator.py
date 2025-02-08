from tkinter import *

FONT=("Arial",10,"bold")

def bmi_calculate():
    h=float(height.get())
    w=float(weight.get())
    bmi_value=w/(h*h)
    result.config(text=f"{bmi_value:.3f}")
    
    if bmi_value<18.5:
        youre.config(text="You need to gain more weight")
    elif bmi_value>25:
        youre.config(text="You need to lose weight")
    else:
        youre.config(text="Your weight is normal")
    

window=Tk()
window.title("Body Mass Index Calculator")
window.config(padx=50,pady=50)

weight=Entry(width=6)
weight.grid(column=0,row=1,padx=10, pady=10)

weight_label=Label(text="Weight(kg)",font=FONT)
weight_label.grid(column=0,row=0,padx=10, pady=10, sticky="EW")

height=Entry(width=6)
height.grid(column=1, row=1, padx=10, pady=10)

height_label=Label(text="Height(m)",font=FONT)
height_label.grid(column=1,row=0, padx=10, pady=10, sticky="EW")

bmi=Label(text="Your BMI is ",font=FONT)
bmi.grid(column=0,row=3, padx=10, pady=10, sticky="E")

result=Label(text="0",font=FONT)
result.grid(column=1,row=3,padx=10, pady=10, sticky="W")

youre=Label(text="",font=FONT)
youre.grid(column=0,row=4,padx=10, pady=10, sticky="W")

calc=Button(text="Calculate",command=bmi_calculate)
calc.grid(row=2, column=0, padx=20, pady=10,sticky="EW")














window. mainloop()
