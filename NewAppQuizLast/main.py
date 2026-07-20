import tkinter as tk
from question import questions

root=tk.Tk()
root.geometry("800x600")
root.title("Python Quiz App")
root.config(bg="indigo")

timeLeft=60
timerId=None
current=0
answer=[-1]*len(questions)

def countDown():
    global timeLeft,timerId
    mins=timeLeft//60
    secs=timeLeft%60

    timer_Label.config(text=f"Quiz time is: {mins:02d}:{secs:02d}")
    if(timeLeft>0):
        timeLeft-=1
        timerId=timer_Label.after(1000,countDown)
    else:
        pass

def loadQuestions():

    myQuestion=questions[current]
    question_Label.config(text=myQuestion["question"])

    for i in range(4):
        radioButton[i].config(text=myQuestion["options"][i])
    
    if answer[current]==-1:
        selected.set(-1)
    else:
        selected.set(answer[current])

def saveAnswer():
    answer[current]=selected.get()

def nextQuestion():
    global current
    saveAnswer()

    if current<len(questions)-1:
        current+=1
        loadQuestions()

def prevQuestion():
    global current
    saveAnswer()

    if current>0:
        current-=1
        loadQuestions()

def restart():
    global current, timeLeft, timerId

    # Stop previous timer
    if timerId is not None:
        root.after_cancel(timerId)
        timerId=None

    current = 0
    timeLeft = 60

    for i in range(len(answer)):
        answer[i] = -1

    selected.set(-1)

    loadQuestions()

    countDown()

def showDashBoard(correct,wrong,percentage):
    dashboard = tk.Toplevel(root)
    dashboard.title("Quiz Result")
    dashboard.geometry("500x600")
    dashboard.configure(bg="#2C3E50")
    dashboard.resizable(False, False)

    title = tk.Label(
        dashboard,
        text="Quiz Completed 🎉",
        font=("Arial",24,"bold"),
        bg="#2C3E50",
        fg="white"
    )
    title.pack(pady=20)

    canvas = tk.Canvas(
        dashboard,
        width=220,
        height=220,
        bg="#88A23B",
        highlightthickness=0
    )
    canvas.pack()

    canvas.create_oval(
        20,20,200,200,
        width=15,
        outline="#555555"
    )

    extent = (percentage/100)*360

    canvas.create_arc(
        20,20,200,200,
        start=90,
        extent=-extent,
        style="arc",
        width=15,
        outline="#2ECC71"
    )

    canvas.create_text(
        110,
        110,
        text=f"{int(percentage)}%",
        fill="white",
        font=("Arial",26,"bold")
    )

    tk.Label(
        dashboard,
        text=f"✔ Correct Answers : {correct}",
        font=("Arial",16),
        bg="#2C3E50",
        fg="#2ECC71"
    ).pack(pady=10)

    tk.Label(
        dashboard,
        text=f"✖ Wrong Answers : {wrong}",
        font=("Arial",16),
        bg="#2C3E50",
        fg="#E74C3C"
    ).pack(pady=10)

    if percentage >= 80:
        msg = "Excellent! 🌟"
    elif percentage >= 60:
        msg = "Good Job 👍"
    elif percentage >= 40:
        msg = "Keep Practicing 🙂"
    else:
        msg = "Need More Practice 📚"

    tk.Label(
        dashboard,
        text=msg,
        font=("Arial",18,"bold"),
        bg="#2C3E50",
        fg="gold"
    ).pack(pady=20)

    tk.Button(
        dashboard,
        text="Restart Quiz",
        font=("Arial",14,"bold"),
        bg="#3498DB",
        fg="white",
        width=15,
        command=lambda:[dashboard.destroy(),restart()]
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Exit",
        font=("Arial",14,"bold"),
        bg="#E74C3C",
        fg="white",
        width=15,
        command=root.destroy
    ).pack(pady=10)

def submitQuiz():
    global timerId,timeLeft,current

    if timerId is not None:
        timer_Label.after_cancel(timerId)
        timerId=None
    
    timeLeft=60
    correct=0

    for i in range(len(questions)):
        if answer[i] == questions[i]["answer"]:
            correct += 1
    
    wrong=len(questions)-correct
    percentage=(correct*100)/len(questions)

    showDashBoard(correct,wrong,percentage)

title=tk.Label(
    root,
    text="Python Quiz App",
    bg="indigo",
    fg="white",
    font=("Arial",24,"bold")
)
title.pack(pady=15)

timer_Label=tk.Label(
    root,
    text="Quiz time is: 1:00",
    bg="indigo",
    fg="white",
    font=("Arial",18,"bold")
)
timer_Label.pack(pady=10)

question_Label=tk.Label(
    root,
    text="1. Random Question",
    bg="indigo",
    fg="white",
    font=("Arial",16)
)
question_Label.pack(pady=10)

selected=tk.IntVar()
selected.set(-1)
radioButton=[]

for i in range(4):
    rb=tk.Radiobutton(
        root,
        text="Option",
        bg="indigo",
        fg="white",
        variable=selected,
        value=i,
        anchor="w",
        width=30,
        selectcolor="red",
        font=("Arial",14)
    )
    rb.pack(pady=5)
    radioButton.append(rb)

buttonFrame=tk.Frame(bg="indigo")
buttonFrame.pack(pady=20)

prevButton=tk.Button(
    buttonFrame,
    text="Previous",
    bg="black",
    fg="white",
    font=("Arial",12),
    command=prevQuestion
)
nextButton=tk.Button(
    buttonFrame,
    text="Next",
    bg="black",
    fg="white",
    font=("Arial",12),
    command=nextQuestion
)
submitButton=tk.Button(
    buttonFrame,
    text="Submit",
    bg="black",
    fg="white",
    font=("Arial",12),
    command=submitQuiz
)
resetButton=tk.Button(
    buttonFrame,
    text="Reset",
    bg="black",
    fg="white",
    font=("Arial",12),
    command=restart
)

prevButton.grid(row=0,column=0,padx=10)
nextButton.grid(row=0,column=1,padx=10)
submitButton.grid(row=0,column=2,padx=10)
resetButton.grid(row=0,column=3,padx=10)



countDown()
loadQuestions()

root.mainloop()