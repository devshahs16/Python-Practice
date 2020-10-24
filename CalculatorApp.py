from tkinter import *

root = Tk()
root.title("Simple Calculator")

input_box = Entry(root, width = 48)
input_box.grid(row = 0, column = 0, columnspan=4, padx = 3, pady = 3)

def button_click(number):
    input_box.insert(END, number)


def button_backspace():
    input_box.delete(len(input_box.get())-1)


def button_clear():
    input_box.delete(0, END)


def button_add():
    global f_num
    global functions
    functions = "addition"
    f_num = float(input_box.get())
    input_box.delete(0,END)


def button_equals():
    global s_num
    s_num = float(input_box.get())
    input_box.delete(0, END)
    global functions
    global math

    if functions == 'addition':
        math = f_num + s_num
        input_box.insert(0, str(math))
    elif functions == 'subtract':
        math = f_num - s_num
        input_box.insert(0, str(math))
    elif functions == 'divide':
        math = f_num / s_num
        input_box.insert(0, str(math))
    elif functions == 'multiply':
        math = f_num * s_num
        input_box.insert(0, str(math))
    else:
        pass

def button_divide():
    global f_num
    global functions
    functions = "divide"
    f_num = int(input_box.get())
    input_box.delete(0, END)


def button_multiply():
    global f_num
    global functions
    functions = "multiply"
    f_num = int(input_box.get())
    input_box.delete(0, END)


def button_subtract():
    global f_num
    global functions
    functions = "subtract"
    f_num = int(input_box.get())
    input_box.delete(0, END)


button_backspace = Button(root, text = "BACK", width = 8, height= 2, padx = 4, pady = 8, command = button_backspace)
button_backspace.grid(row = 1, column = 0)

button_clear = Button(root, text = "CLEAR", width = 8, height= 2, padx = 4, pady = 8, command = button_clear)
button_clear.grid(row = 1, column = 1)

button_divide = Button(root, text = "/", width = 8, height= 2, padx = 4, pady = 8, command = button_divide)
button_divide.grid(row = 1, column = 2)

button_multiply = Button(root, text = "*", width = 8, height= 2, padx = 4, pady = 8, command = button_multiply)
button_multiply.grid(row = 1, column = 3)

button_subtract = Button(root, text = "-", width = 8, height= 2, padx = 4, pady = 8, command = button_subtract)
button_subtract.grid(row = 2, column = 3)

button_point = Button(root, text = ".", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click('.'))
button_point.grid(row = 5, column = 0)

button1 = Button(root, text = "1", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("1"))
button1.grid(row = 4, column = 0)

button2 = Button(root, text = "2", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("2"))
button2.grid(row = 4, column = 1)

button3 = Button(root, text = "3", width = 8, height= 2,padx = 4, pady = 8, command = lambda: button_click("3"))
button3.grid(row = 4, column = 2)

button4 = Button(root, text = "4", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("4"))
button4.grid(row = 3, column = 0)

button5 = Button(root, text = "5", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("5"))
button5.grid(row = 3, column = 1)

button6 = Button(root, text = "6", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("6"))
button6.grid(row = 3, column = 2)

button7 = Button(root, text = "7", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("7"))
button7.grid(row = 2, column = 0)

button8 = Button(root, text = "8", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("8"))
button8.grid(row = 2, column = 1)

button9 = Button(root, text = "9", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("9"))
button9.grid(row = 2, column = 2)

button_0= Button(root, text = "0", width = 8, height= 2, padx = 4, pady = 8, command = lambda: button_click("0"))
button_0.grid(row = 5, column = 1)

button_add = Button(root, text = "+", width = 8, height= 6, padx = 4, pady = 5, command = button_add)
button_add.grid(row = 3, column = 3, rowspan =2)

button_equals = Button(root, text = "=", width = 19, height= 2, padx = 3, pady = 8, command = button_equals)
button_equals.grid(row = 5, column = 2, columnspan = 2 )

root.mainloop()

