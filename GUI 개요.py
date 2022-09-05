from tkinter import *

mainFrame = Tk()
mainFrame.geometry("400x200")

nameLabel = Label(mainFrame, text="이름", font="Serif 20")
nameLabel.pack()


def changejiwon():
    nameLabel["text"] = "지원쌤"


jiwonButton = Button(mainFrame, text="지원쌤으로 변경", command=changejiwon)
jiwonButton.pack()


def changeSunwu():
    nameLabel["text"] = "선우쌤"


SunwuButton = Button(mainFrame, text="선우쌤 으로 변경", command=changeSunwu)
SunwuButton.pack()

def changeEum():
    nameLabel["text"] = "엄서연"


EumButton = Button(mainFrame, text="엄서연으로 변경", command=changeEum)
EumButton.pack()
mainFrame.mainloop()
