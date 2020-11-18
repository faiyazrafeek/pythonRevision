from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth = 1)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def btnClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
    return

def btnClear():
    e.delete(0, END)

def btnAdd():
    global math
    math = "add"
    fNum = e.get()
    global num1
    num1 = int(fNum)
    e.delete(0, END)

def btnSub():
    global math
    math = "sub"
    fNum = e.get()
    global num1
    num1 = int(fNum)
    e.delete(0, END)

def btnMul():
    global math
    math = "mul"
    fNum = e.get()
    global num1
    num1 = int(fNum)
    e.delete(0, END)

def btnDiv():
    global math
    math = "div"
    fNum = e.get()
    global num1
    num1 = int(fNum)
    e.delete(0, END)

def btnEqual():
    num2 = int(e.get())
    e.delete(0,END)

    if math=="add":
        sum = num1 + num2
        e.insert(0, sum)
    elif math=="sub":
        sum = num1 - num2
        e.insert(0, sum)
    elif math=="mul":
        sum = num1 * num2
        e.insert(0, sum)
    else:
        sum = num1 / num2
        e.insert(0, sum)


btn1 = Button(root, text="1", padx=30, pady=20, command=lambda: btnClick(1))
btn2 = Button(root, text="2", padx=30, pady=20, command=lambda: btnClick(2))
btn3 = Button(root, text="3", padx=30, pady=20, command=lambda: btnClick(3))
btn4 = Button(root, text="4", padx=30, pady=20, command=lambda: btnClick(4))
btn5 = Button(root, text="5", padx=30, pady=20, command=lambda: btnClick(5))
btn6 = Button(root, text="6", padx=30, pady=20, command=lambda: btnClick(6))
btn7 = Button(root, text="7", padx=30, pady=20, command=lambda: btnClick(7))
btn8 = Button(root, text="8", padx=30, pady=20, command=lambda: btnClick(8))
btn9 = Button(root, text="9", padx=30, pady=20, command=lambda: btnClick(9))
btn0 = Button(root, text="0", padx=30, pady=20, command=lambda: btnClick(0))
btnAdd = Button(root, text="+", padx=29, pady=20, command= btnAdd)
btnEqual = Button(root, text="=", padx=68, pady=20, command= btnEqual)
btnClear = Button(root, text="Clear", padx=58, pady=20,command=btnClear)

btnSub = Button(root, text="-", padx=30, pady=20, command= btnSub)
btnMul = Button(root, text="*", padx=30, pady=20, command= btnMul)
btnDiv = Button(root, text="/", padx=30, pady=20, command= btnDiv)



btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn6.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn4.grid(row=2, column=2)

btn3.grid(row=3, column=2)
btn2.grid(row=3, column=1)
btn1.grid(row=3, column=0)

btn0.grid(row=4, column=0)
btnClear.grid(row=4, column=1, columnspan=2)
btnAdd.grid(row=5, column=0)
btnEqual.grid(row=5, column=1, columnspan=2)
btnSub.grid(row=6, column=0)
btnMul.grid(row=6, column=1)
btnDiv.grid(row=6, column=2)




root.mainloop()