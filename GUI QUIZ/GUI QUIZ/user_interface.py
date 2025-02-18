from tkinter import *
from quiz_brain import QuizBrain

class Quiz_Interface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20,pady=20,bg="#10587c")
        
        self.score=Label(text="Score:0",fg="white",bg="#10587c",font=("Arial",12,"bold"))
        self.score.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=200,bg="white")
        self.question_text=self.canvas.create_text(150,125,text="kdjshfgkjdg",font=("Arial",14,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        

        true_image=PhotoImage(file="rr.png")
        self.true_button=Button(image=true_image,width=100,height=100,highlightthickness=0,bd=0,relief=FLAT,command=self.press_true)
        self.true_button.grid(row=2,column=0)

        false_image=PhotoImage(file="X.png")
        self.false_button=Button(image=false_image,width=100,height=100,highlightthickness=0,bd=0,relief=FLAT,command=self.press_false)
        self.false_button.grid(row=2,column=1)
        
        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            quiz=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=quiz)
        else:
            self.canvas.itemconfig(self.question_text,text=f"FINAL SCORE: {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def press_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def press_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self,ans):
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_q)

