from tkinter import *
import pandas as pd
import random


data=pd.read_csv('english_turkish.csv')
words_to_learn = data.copy()

index=0
def next_card():
    global index,timer
    index=random.randint(0,len(words_to_learn)-1)
    window.after_cancel(timer)
    canvas.itemconfig(text1,text="English",fill="white")
    canvas.itemconfig(text2,text=words_to_learn.iloc[index]["English"],fill="white")
    canvas.itemconfig(card,image=img)
    timer=window.after(3000,card_flip)
    
def card_flip():
    canvas.itemconfig(text1,text="Turkish",fill="black")
    canvas.itemconfig(text2,text=words_to_learn.iloc[index]["Turkish"],fill="black")
    canvas.itemconfig(card,image=img2)
        
def known():
    global words_to_learn
    words_to_learn=words_to_learn.drop(index=index).reset_index(drop=True)
    words_to_learn.to_csv('words_to_learn.csv',index=False)
    next_card()
    

def reset():
    global words_to_learn, data
    words_to_learn = data.copy()
    words_to_learn.to_csv('words_to_learn.csv', index=False)
    next_card()

window=Tk()
window.title("ENG-TUR")
window.config(padx=50,pady=50,bg="#d3eacd")
timer=window.after(3000,card_flip)
canvas=Canvas(width=800,height=600,bg="#d3eacd",highlightthickness=0)
img=PhotoImage(file="cardd1.png")
img2=PhotoImage(file="cardd2.png")
card=canvas.create_image(400,300,image=img)
text1=canvas.create_text(400,160,text="Title",font=("Arial",40,"italic"))
text2=canvas.create_text(400,260,text="Word",font=("Arial",60,"bold"))
canvas.grid(column=0,row=1,columnspan=2)


true_img=PhotoImage(file="true.png")
true_=Button(image=true_img,highlightthickness=0, bd=0, bg="#d3eacd", activebackground="#d3eacd",relief="flat",overrelief="flat",command=known)
true_.grid(column=1,row=2)

false_img=PhotoImage(file="false.png")
false_=Button(image=false_img,highlightthickness=0, bd=0, bg="#d3eacd", activebackground="#d3eacd",relief="flat",overrelief="flat",command=next_card)
false_.grid(column=0,row=2)

reset_img=PhotoImage(file="reset.png")
reset_button=Button(image=reset_img,highlightthickness=0, bd=0, bg="#d3eacd", activebackground="#d3eacd",relief="flat",overrelief="flat",command=reset)
reset_button.grid(column=2,row=0)

next_card()

window.mainloop()
