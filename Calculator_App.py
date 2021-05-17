from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("Calculator")
root.resizable(False,False)
entry = StringVar()
display = Entry(root, font=("agencty FB", 20, "bold"), borderwidth=6, textvariable=entry, insertwidth=10, width=20, bg="white")
display.grid(row=0, column=0, columnspan=4, sticky=S+N+E+W)
operator = ""

def click(value):
    global operator
    operator += str(value)
    entry.set(operator)
def equal():
    try:
        global operator
        sum = str(eval(operator))
        entry.set(sum)
        operator = ""
    except ZeroDivisionError:
        tkinter.messagebox.showerror("ERROR!", "CANNOT DIVIDE BY 0")
    except SyntaxError:
        tkinter.messagebox.showerror("ERROR!", "A SYNTAX ERROR OCCURED")
def clear():
    global operator
    operator = ""
    entry.set("")

button7 = Button(root, padx=16, pady=16, font=("agencty FB",20,"bold"), fg="black", bg="white", width=5, text="7", command=lambda: click("7"))
button7.grid(row=1, column=1, sticky=S+N+E+W)

button8 = Button(root, padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="8", command=lambda: click("8"))
button8.grid(row=1, column=2, sticky=S+N+E+W)

button9 = Button(root, padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="9", command=lambda: click("9"))
button9.grid(row=1, column=3, sticky=S+N+E+W)

button4 = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="4", command=lambda: click("4"))
button4.grid(row=11, column=1, sticky=S+N+E+W)

button5 = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="5", command=lambda: click("5"))
button5.grid(row=11, column=2, sticky=S+N+E+W)

button6 = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="6", command=lambda: click("6"))
button6.grid(row=11, column=3, sticky=S+N+E+W)

button1 = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="1", command=lambda: click("1"))
button1.grid(row=12, column=1, sticky=S+N+E+W)

button2 = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="2", command=lambda: click("2"))
button2.grid(row=12, column=2, sticky=S+N+E+W)

button3 = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="3", command=lambda: click("3"))
button3.grid(row=12, column=3, sticky=S+N+E+W)

button0 = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="0", command=lambda: click("0"))
button0.grid(row=14, column=1, sticky=S+N+E+W)

additionButton = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="+", command=lambda: click("+"))
additionButton.grid(row=14, column=3, sticky=S+N+E+W)

subtractButton = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="-", command=lambda: click("-"))
subtractButton.grid(row=14, column=2, sticky=S+N+E+W)

decimalButton = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text=".", command=lambda:  click("."))
decimalButton.grid(row=15, column=1, sticky=S+N+E+W)

multiplyButton = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="x", command=lambda: click("*"))
multiplyButton.grid(row=15, column=2, sticky=S+N+E+W)

divisionButton = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="/", command=lambda: click("/"))
divisionButton.grid(row=15, column=3, sticky=S+N+E+W)

equalButton = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="=", command=lambda: equal())
equalButton.grid(row=16, column=1, sticky=S+N+E+W)

clearButton = Button(padx=16, pady=16, font=("agencty FB", 20, "bold"), fg="black", bg="white", width=5, text="C", command=lambda: clear())
clearButton.grid(row=16, column=2, sticky=S+N+E+W)

root.mainloop()
