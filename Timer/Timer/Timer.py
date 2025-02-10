from tkinter import *
import tkinter.font as tkFont
import math

# path="digital-7.ttf"
# custom_font = tkFont.Font(family=path, size=64)


FONT_BUTTON=("Arial",10,"bold")

timer_=None


def reset_timer():
    window.after_cancel(timer_)
    canvas.itemconfig(timer,text="00:00")
    first_label.config(text="TIMER", font=("Arial",48,"bold"),fg="black",bg="#9d699f")
    canvas.itemconfig(img,image=clock_img)

def start_timer(x):
    count_down(int(x)*60)

def count_down(count):
    
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_min<10:
        count_min=f"0{count_min}"
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count>0:
       global timer_
       timer_= window.after(1000,count_down,count-1)
    else:
        first_label.config(text="TIME IS UP!", font=("Arial",48,"bold"),fg="red",bg="#9d699f")
        canvas.itemconfig(img,image=clock2_img)
        

window=Tk()
window.title("TIMER")
window.config(padx=100,pady=50,bg="#9d699f")



first_label=Label(text="TIMER",font=("Arial",48,"bold"),fg="black",bg="#9d699f")
first_label.grid(column=1,row=0)

canvas=Canvas(width=512,height=512,bg="#9d699f",highlightthickness=0)
clock_img=PhotoImage(file="clock.png")
clock2_img=PhotoImage(file="clock2.png")
img=canvas.create_image(256,256,image=clock_img)
timer=canvas.create_text(256,256,text="00:00",fill="white",font=("Arial",64,"bold"))
canvas.grid(column=1,row=1)

reset=Button(text="RESET",width=15,font=FONT_BUTTON, command=reset_timer)
reset.grid(column=2,row=2,sticky="w")

time=Entry(width=15)
time.grid(column=0,row=2,sticky="W",padx=10)

sett=Button(text="SET MINUTE", font=FONT_BUTTON ,command=lambda: start_timer(time.get()) )
sett.grid(column=1,row=2,sticky="EW",padx=120)



window.mainloop()
