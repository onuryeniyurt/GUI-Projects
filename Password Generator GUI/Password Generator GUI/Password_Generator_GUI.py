from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','&','#','$','*','?']
numbers=['0','1','2','3','4','5','6','7','8','9']

def generate():
    password_l=[]
    lett=random.randint(8,10)
    symm=random.randint(2,4)
    numm=random.randint(2,4)
    
    for x in range(lett):
        password_l.append(random.choice(letters))
    for x in range(symm):
        password_l.append(random.choice(symbols))
    for x in range(numm):
        password_l.append(random.choice(numbers))
        
    random.shuffle(password_l)
    password=""
    for x in password_l:
        password+=x
        
    pass_entry.insert(0,password)
    pyperclip.copy(password)

def save():
    web=web_entry.get()
    email=email_entry.get()
    password=pass_entry.get()
    new_data={
        web:{"email":email
                   ,"password":password}
        }

    sure= messagebox.askokcancel(title="Save",message="Are you sure to save?")
    if len(web)==0 or len(email)==0 or len(password)==0:
        messagebox.showwarning(title="Error",message="You should enter all of the details!")
        
    elif sure:
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:    
            web_entry.delete(0,END)
            email_entry.delete(0,END)
            pass_entry.delete(0,END)
                
            

def on_focus_in(event):
    if email_entry.get() == placeholder:
        email_entry.delete(0,END)
        email_entry.config(fg="black")

def on_focus_out(event):
    if email_entry.get() == "":
        email_entry.insert(0, placeholder)
        email_entry.config(fg="grey")
        

def search():
    web_name=web_entry.get()
    
    with open("data.json","r") as data_file:
        data1=json.load(data_file)
     
    try:
        e_mail=data1[web_name]["email"]
        passwordd=data1[web_name]["password"]
    except KeyError:
        messagebox.showerror(title="Error",message="Website not found")
    else:
        messagebox.showinfo(title="Info",message=f"Website: {web_name}\n E-Mail: {e_mail}\n Password: {passwordd}")
        

FONT=("Arial",12,"bold")

window=Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=80,pady=50, bg="#f5d6b2")
canvas=Canvas(width=240,height=240,bg="#f5d6b2",highlightthickness=0)
lock_img=PhotoImage(file="lock.png")

canvas.create_image(120,120,image=lock_img)
canvas.grid(column=1,row=0,padx=20,pady=20)

web_label=Label(text="Website:",font=FONT,bg="#f5d6b2")
web_label.grid(column=0,row=1)


email_label=Label(text="E-mail/Username:",font=FONT,bg="#f5d6b2")
email_label.grid(column=0,row=2)

pass_label=Label(text="Password:",font=FONT,bg="#f5d6b2")
pass_label.grid(column=0,row=3)

web_entry=Entry(width=47)
web_entry.grid(column=1,row=1)
web_entry.focus()

search_button=Button(text="Search",width=13,command=search)
search_button.grid(column=2,row=1)

email_entry=Entry(width=65)
email_entry.grid(column=1,row=2,columnspan=2)

placeholder="example@example.com"

email_entry.insert(0, placeholder)
email_entry.bind("<FocusIn>", on_focus_in)
email_entry.bind("<FocusOut>", on_focus_out)

pass_entry=Entry(width=47)
pass_entry.grid(column=1,row=3,padx=2)

add_button=Button(text="Add",width=55,command=save)
add_button.grid(column=1,row=4,columnspan=2)

generate_button=Button(text="Generate Password",command=generate)
generate_button.grid(column=2,row=3,pady=5)

pass_entry.config(highlightthickness=0)
generate_button.config(highlightthickness=0)






window.mainloop()
