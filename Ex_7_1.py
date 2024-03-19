from tkinter import *
# function to add two numbers
def add():
    t3.delete(0, 'end')
    num1 = float(t1.get())
    num2 = float(t2.get())
    result = num1 + num2
    result = round(result, 4)
    t3.insert(END, str(result))
    label3.config(text="Addition")


# function to subtract two numbers
def sub():
    t3.delete(0, 'end')
    num1 = float(t1.get())
    num2 = float(t2.get())
    result = num1 - num2
    result = round(result, 4)
    t3.insert(END, str(result))
    label3.config(text="Subtraction")


# function to multiply two numbers
def mul():
    t3.delete(0, 'end')
    num1 = float(t1.get())
    num2 = float(t2.get())
    result = num1 * num2
    result = round(result, 4)
    t3.insert(END, str(result))
    label3.config(text="Multiplication")

def div():
    t3.delete(0, 'end')
    num1 = float(t1.get())
    num2 = float(t2.get())
    result = num1 / num2
    result = round(result, 4)
    t3.insert(END, str(result))
    label3.config(text="Division")


# create main window
win = Tk()
win.title('Python GUI Program - 4 Function Calculator')
win.geometry("400x300+10+10")

# create labels, text boxes, buttons
label1 = Label(win, text='Type Value 1:')
label2 = Label(win, text='Type Value 2:')
label3 = Label(win, text='Result')
t1 = Entry(bd=3)
t2 = Entry()
t3 = Entry()

# place widgets
label1.place(x=100, y=50)
t1.place(x=200, y=50)
label2.place(x=100, y=100)
t2.place(x=200, y=100)

# create buttons and bind functions on click event
b1 = Button(win, text='+', fg='white', height=2, width=4,  bg='green', command=add)
b2 = Button(win, text='-', fg='white', height=2, width=4, bg='green', command=sub)
b3 = Button(win, text='X', fg='white', height=2, width=4, bg='green', command=mul)
b4 = Button(win, text='/', fg='white', height=2, width=4, bg='green', command=div)
b1.place(x=100, y=150)
b2.place(x=160, y=150)
b3.place(x=220, y=150)
b4.place(x=280, y=150)
label3.place(x=100, y=200)
t3.place(x=200, y=200)
# start event loop
win.mainloop()
