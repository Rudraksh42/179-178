from tkinter import *
import random

root = Tk()
root.title("color randomizer game")
root.geometry("800x600")
root.configure(bg="skyblue")

color_label = Label(root,bg="orange",font=("Times",22,"bold"))
color_label.place(relx=0.5,rely=0.5,anchor=CENTER)

score_label = Label(root,text="Score: 0",font=("Arial",18,"bold"),bg="black",fg="white")
score_label.place(relx=0.05,rely=0.1,anchor=W)

input_value = Entry(root)
input_value.place(relx=0.5,rely=0.6,anchor=CENTER)

class game:
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.color = ["red","purple","maroon","skyblue","yellow","white","lightgreen","teal"]
        self.text_color = ["RED","PURPLE","MAROON","SKYBLUE","YELLOW","WHITE","LIGHTGREEN","TEAL"]
        self.random_number_for_text = random.randint(0,7)
        self.random_number_for_color = random.randint(0,7)
        color_label["fg"] = self.color[self.random_number_for_color]
        color_label["text"] = self.text_color[self.random_number_for_text]
        
    def __updateScore(self,input_value):
        if (input_value == self.color[self.random_number_for_color]):
            print(self.color[self.random_number_for_color])
            self.__score = self.__score + random.randint(0,7)
            score_label["text"] = "Score: " + str(self.__score)
            
    def publicFunction(self,input_value):
        self.__updateScore(input_value)
        
gameObj = game()
def getInput():
    value = input_value.get()
    gameObj.publicFunction(value)
    gameObj.updateGame()
    input_value.delete(0,END)
    
start_button = Button(root,text="START",bg="IndianRed2",fg="white",font=("Arial",15,"italic"),command=gameObj.updateGame)
start_button.place(relx=0.4,rely=0.7,anchor=CENTER)

check_button = Button(root,text="CHECK",font=("Arial",15,"italic"),bg="navy blue",fg="white",command=getInput)
check_button.place(relx=0.6,rely=0.7,anchor=CENTER)

root.mainloop()