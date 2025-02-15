from tkinter import *
from tkinter.messagebox import showerror
import requests as rq
import pandas as pd

country_data=pd.read_csv("countries_lat_lng.csv")


def on_click():
    
    country=entry.get().title()
    if country in country_data["Country"].values:
        paramss=None
        for c in range(len(country_data)):
            if country==country_data.iloc[c]["Country"]:
                paramss = {"lat": country_data.iloc[c]["Latitude"], "lng": country_data.iloc[c]["Longitude"], "formatted": 0}
                response=rq.get("https://api.sunrise-sunset.org/json",params=paramss)
                response.raise_for_status()
                data=response.json()
        sunrise=data["results"]["sunrise"].split('T')[1].split(':')
        sunset=data["results"]["sunset"].split('T')[1].split(':')
        canvas.delete("all")
        canvas.create_image(576,360,image=sun)
        canvas.create_text(300,370,text=f"{sunrise[0]}:{sunrise[1]}",font=("Arial",70,"bold"),fill="black")
        canvas.create_text(900,370,text=f"{sunset[0]}:{sunset[1]}",font=("Arial",70,"bold"),fill="white")
    else:
        showerror(title="NOT FOUND",message="Your country couldn't found")
    
    

data=pd.read_csv("countries_lat_lng.csv")

window=Tk()
window.title("Sunset-Sunrise")
window.config(padx=0,pady=0)
canvas=Canvas(height=720,width=1152)
bg_img = PhotoImage(file="background.png")
sun=PhotoImage(file="background2.png")
bg=canvas.create_image(576,360,image=bg_img)
text1=canvas.create_text(600,160,text="Enter Your Country",font=("Arial",50,"bold"),fill="white")
entry = Entry(window, width=30,font=("Arial",20,"bold"))
canvas.create_window(600, 230, window=entry)
button = Button(window, text="ENTER",font=("Arial",20,"bold"),command=on_click)
canvas.create_window(600, 300, window=button)
canvas.pack(fill="both", expand=True)



window.mainloop()
