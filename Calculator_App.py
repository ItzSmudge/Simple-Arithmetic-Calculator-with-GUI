from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Calculator")
window.resizable(False,False)

text_font = ("Sans Serif", 20, "bold")
fg_color = "#000000"
bg_color = "#ffffff"

#Gray = #636162
#White = #ffffff
#Black = #000000

entry = StringVar()
display = Entry(window, font=text_font, borderwidth=6, textvariable=entry, insertwidth=10, width=20, bg=bg_color)
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

button7 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="7", command=lambda: click("7"))
button7.grid(row=1, column=1, sticky=S+N+E+W)

button8 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="8", command=lambda: click("8"))
button8.grid(row=1, column=2, sticky=S+N+E+W)

button9 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="9", command=lambda: click("9"))
button9.grid(row=1, column=3, sticky=S+N+E+W)

button4 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="4", command=lambda: click("4"))
button4.grid(row=11, column=1, sticky=S+N+E+W)

button5 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="5", command=lambda: click("5"))
button5.grid(row=11, column=2, sticky=S+N+E+W)

button6 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="6", command=lambda: click("6"))
button6.grid(row=11, column=3, sticky=S+N+E+W)

button1 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="1", command=lambda: click("1"))
button1.grid(row=12, column=1, sticky=S+N+E+W)

button2 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="2", command=lambda: click("2"))
button2.grid(row=12, column=2, sticky=S+N+E+W)

button3 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="3", command=lambda: click("3"))
button3.grid(row=12, column=3, sticky=S+N+E+W)

button0 = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="0", command=lambda: click("0"))
button0.grid(row=14, column=1, sticky=S+N+E+W)

addition_button = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="+", command=lambda: click("+"))
addition_button.grid(row=14, column=3, sticky=S+N+E+W)

subtract_button = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="-", command=lambda: click("-"))
subtract_button.grid(row=14, column=2, sticky=S+N+E+W)

decimal_button = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text=".", command=lambda:  click("."))
decimal_button.grid(row=15, column=1, sticky=S+N+E+W)

multiply_button = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="x", command=lambda: click("*"))
multiply_button.grid(row=15, column=2, sticky=S+N+E+W)

division_button = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="/", command=lambda: click("/"))
division_button.grid(row=15, column=3, sticky=S+N+E+W)

equal_button = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="=", command=lambda: equal())
equal_button.grid(row=16, column=1, sticky=S+N+E+W)

clear_button = Button(window, padx=16, pady=16, font=text_font, fg=fg_color, bg=bg_color, width=5, text="C", command=lambda: clear())
clear_button.grid(row=16, column=2, sticky=S+N+E+W)

window.mainloop()
