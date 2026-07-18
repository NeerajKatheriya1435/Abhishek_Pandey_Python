
import tkinter as tk
from question import questions

root=tk.Tk()
root.title("Python Quiz App")
root.geometry("800x500")
root.config(bg="brown")

current=0
myTime=60
timerId=None

title=tk.Label(
    root,
    text="Quiz App",
    font=("Arial",24,"bold"),
    bg="brown",
    fg="white"
)

title.pack(pady=20)

timer=tk.Label(
    root,
    text="",
    bg="brown",
    fg="white",
    font=("Arial",14,"bold")
)

timer.pack()

myQuestion=tk.Label(
    root,
    text="JavaScript Was so popular",
    bg="brown",
    fg="white",
    font=("Arial",12,"bold"),
    width=40
)

myQuestion.pack(pady=15)

select=tk.IntVar()
select.set(-1)

radioButton=[]

for i in range(4):
    rb=tk.Radiobutton(
        root,
        text="Option",
        value=i,
        variable=select,
        font=("Arial",10,"bold"),
        bg="brown",
        fg="White",
        width=50,
        anchor="w",
        selectcolor="red"
    )
    rb.pack()
    radioButton.append(rb)


buttonFrame=tk.Frame(
    root,
    bg="yellow",
)

def MyTimer():

    global myTime

    if myTime >= 0:
        # Calculate minutes and seconds
        mins, secs = divmod(myTime, 60)
        # Format as MM:SS string
        timer_text = f"{mins:02d}:{secs:02d}"
        timer.config(text=timer_text)
        
        # Decrement time and schedule the next update in 1000ms (1 second)
        myTime -= 1
        root.after(1000, MyTimer)

def loadQuestion():
    myQuestion.config(text=questions[current]["question"])
    
    

    for i in range(4):
        radioButton[i].config(text=questions[current]["options"][i])


def nextQuestion():
    pass

previous= tk.Button(buttonFrame, text="Previous")
next=tk.Button(buttonFrame, text="Next",command=nextQuestion)
submit=tk.Button(buttonFrame, text="Submit")
reset=tk.Button(buttonFrame, text="Reset")

previous.pack(side="left", fill="x", padx=10, pady=5)
next.pack(side="left", fill="x", padx=10, pady=5)
submit.pack(side="left", fill="x", padx=10, pady=5)
reset.pack(side="left", fill="x", padx=10, pady=5)

buttonFrame.pack(pady=80)

loadQuestion()
MyTimer()

root.mainloop()