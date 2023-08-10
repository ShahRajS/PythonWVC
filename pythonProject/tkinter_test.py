from tkinter import *

#tk._test()

def click():
    entered_text = textbox.get()
    print(entered_text)
    output.delete(0.0, END)
    if entered_text == "W":
        text = "You moved up one!"
    else:
        text = "False movement"
    output.insert(END, text)

def exitter():
    print("Good Game")
    quit()

win = Tk()
win.title("Dungeon Crawlhalla")
win.configure(background = "turquoise")

bg_pic = PhotoImage(file = "maze.png")
Label(win, image = bg_pic,bg = "black").grid(row = 0, column = 0, sticky = W)
Label(win, text = "Type your movement", bg = "black", fg = "white").grid(row = 0, column = 1, sticky = E)

textbox = Entry(win, width = 20, bg = "tan")
textbox.grid(row = 1, column = 1, sticky = W)
print(type(textbox))
Button(win, text = "Submit", width = 12, command = click).grid(row = 1, column = 0, sticky = W)
Button(win, text = "Exit", width = 12, command = exitter).grid(row = 0, column = 0)

output = Text(win, wrap = WORD, background = "grey")
output.grid(row = 2,column = 0, sticky = S)

win.mainloop()