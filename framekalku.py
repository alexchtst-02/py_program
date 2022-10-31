from tkinter import *
from math import *

root = Tk()
root.title("Frame Kalkulator")
root.geometry('307x330')
root.resizable(0,0)

# serangkaian fungsi
value = StringVar()
act_1 = lambda : value.set(('{}{}').format(value.get(), '1'))
act_2 = lambda : value.set(('{}{}').format(value.get(), '2'))
act_3 = lambda : value.set(('{}{}').format(value.get(), '3'))
act_4 = lambda : value.set(('{}{}').format(value.get(), '4'))
act_5 = lambda : value.set(('{}{}').format(value.get(), '5'))
act_6 = lambda : value.set(('{}{}').format(value.get(), '6'))
act_7 = lambda : value.set(('{}{}').format(value.get(), '7'))
act_8 = lambda : value.set(('{}{}').format(value.get(), '8'))
act_9 = lambda : value.set(('{}{}').format(value.get(), '9'))
act_0 = lambda : value.set(('{}{}').format(value.get(), '0'))
act_delall = lambda : value.set('')
act_del = lambda : value.set(value.get()[:-1])
act_clrhstr = lambda : txt.delete(1.0, END)


# fungsi untuk operasi
op = []
my_n = []
def act_times():
    if value.get() != "":
        my_n.insert(0, value.get())
        op.append('*')
        if len(op) == 1:
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}{}').format(value.get(), '*')))
            value.set('')

def act_devides():
    if value.get() != "":
        my_n.insert(0, value.get())
        op.append(':')
        if len(op) == 1:
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}{}').format(value.get(), ':')))
            value.set('')

def act_plus():
    if value.get() != "":
        my_n.insert(0, value.get())
        op.append('+')
        if len(op) == 1:
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}{}').format(value.get(), '+')))
            value.set('')

def act_mines():
    if value.get() != "":
        my_n.insert(0, value.get())
        op.append('-')
        if len(op) == 1:
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}{}').format(value.get(), '-')))
            value.set('')

def act_sqroot():
    if value.get() != "":
        my_n.insert(0, value.get())
        op.append('sqrt')
        if len(op) == 1:
            txt.delete(1.0, END)
            txt.insert(1.0, (('sqrt({})={}').format(value.get(), sqrt(float(my_n[0])))))
            value.set(('{}').format(sqrt(float(my_n[0]))))
            op.clear()
            my_n.clear()

def act_fct():
    if value.get() != "":
        my_n.insert(0, value.get())
        op.append('fct')
        if len(op) == 1:
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}!={}').format(value.get(), factorial(int(my_n[0])))))
            value.set(('{}').format(factorial(int(my_n[0]))))
            op.clear()
            my_n.clear()

def eql():
    if value.get() != "":
        my_n.insert(0, value.get())
        if op[0] == '*':
            a = str(txt.get(1.0, END))
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}{}={}').format(a[:-1], value.get(), float(my_n[1])*float(my_n[0]))))
            value.set(('{}').format(float(my_n[1])*float(my_n[0])))
            op.clear()
            my_n.clear()
        elif op[0] == ':':
            a = str(txt.get(1.0, END))
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}{}={}').format(a[:-1], value.get(), float(my_n[1])/float(my_n[0]))))
            value.set(('{}').format(float(my_n[1])/float(my_n[0])))
            op.clear()
            my_n.clear()
        elif op[0] == '+':
            a = str(txt.get(1.0, END))
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}{}={}').format(a[:-1], value.get(), float(my_n[1])+float(my_n[0]))))
            value.set(('{}').format(float(my_n[1])+float(my_n[0])))
            op.clear()
            my_n.clear()
        elif op[0] == '-':
            a = str(txt.get(1.0, END))
            txt.delete(1.0, END)
            txt.insert(1.0, (('{}{}={}').format(a[:-1], value.get(), float(my_n[1])-float(my_n[0]))))
            value.set(('{}').format(float(my_n[1])-float(my_n[0])))
            op.clear()
            my_n.clear()


# membuat frame, text, dan scrb utk history
frame = Frame(root, width=25, height=15, relief=GROOVE)
scb = Scrollbar(frame, orient=VERTICAL, command=YView)
txt = Text(frame, width=30, height=5, font=('Helvatica 12'), relief=GROOVE, yscrollcommand=scb.set)
scb.config(command=txt.yview)
scb.pack(side=RIGHT, fill=Y, padx=2, pady=1)
txt.pack(fill=X, padx=1, pady=1)
btn_clearhstr = Button(root, font=('Helvatica 13'), height=1, justify=CENTER, text='Clear History', relief=GROOVE, command=act_clrhstr)

# membuat entry
entry = Entry(frame, font=('Helvatica 15'), width=25, justify=RIGHT, relief=GROOVE, textvariable=value)

# membuat button untuk angka dan +, -, x, : dan sqrt(n), bagian1
btn_1 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='1', relief=GROOVE, command=act_1)
btn_2 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='2', relief=GROOVE, command=act_2)
btn_3 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='3', relief=GROOVE, command=act_3)
btn_4 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='4', relief=GROOVE, command=act_4)
btn_5 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='5', relief=GROOVE, command=act_5)
btn_6 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='6', relief=GROOVE, command=act_6)
btn_7 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='7', relief=GROOVE, command=act_7)
btn_8 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='8', relief=GROOVE, command=act_8)
btn_9 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='9', relief=GROOVE, command=act_9)
btn_dot = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='.', relief=GROOVE)
btn_0 = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='0', relief=GROOVE, command=act_0)
btn_plus = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='+', relief=GROOVE, command=act_plus)
btn_mines = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='-', relief=GROOVE, command=act_mines)
btn_times = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='x', relief=GROOVE, command=act_times)
btn_devides = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text=':', relief=GROOVE, command=act_devides)
btn_sqroot = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='sqrt(n)', relief=GROOVE, command=act_sqroot)

# membuat tombol button untuk operasi (n!, del, c, dan =)
btn_factorial = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='n!', relief=GROOVE, command=act_fct)
btn_del = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='del', relief=GROOVE, command=act_del)
btn_delall = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='c', relief=GROOVE, command=act_delall)
btn_equal = Button(root, font=('Helvatica 13'), width=5, height=1, justify=CENTER, text='=', relief=GROOVE, command=eql)

# grid
frame.grid(row=0, column=0, columnspan=6, padx=2, pady=1)

#entry.grid(row=1, column=0, columnspan=6, padx=5, pady=5)
entry.pack(fill=X, padx=2, pady=1)

btn_1.grid(row=2, column=0, sticky=W+N+S+E, padx=2, pady=1)
btn_2.grid(row=2, column=1, sticky=W+N+S+E, padx=2, pady=1)
btn_3.grid(row=2, column=2, sticky=W+N+S+E, padx=2, pady=1)
btn_mines.grid(row=2, column=3, sticky=W+N+S+E, padx=2, pady=1)
btn_4.grid(row=3, column=0, sticky=W+N+S+E, padx=2, pady=1)
btn_5.grid(row=3, column=1, sticky=W+N+S+E, padx=2, pady=1)
btn_6.grid(row=3, column=2, sticky=W+N+S+E, padx=2, pady=1)
btn_times.grid(row=3, column=3, sticky=W+N+S+E, padx=2, pady=1)
btn_7.grid(row=4, column=0, sticky=W+N+S+E, padx=2, pady=1)
btn_8.grid(row=4, column=1, sticky=W+N+S+E, padx=2, pady=1)
btn_9.grid(row=4, column=2, sticky=W+N+S+E, padx=2, pady=1)
btn_devides.grid(row=4, column=3, sticky=W+N+S+E, padx=2, pady=1)
btn_dot.grid(row=5, column=0, sticky=W+N+S+E, padx=2, pady=1)
btn_0.grid(row=5, column=1, sticky=W+N+S+E, padx=2, pady=1)
btn_plus.grid(row=5, column=2, sticky=W+N+S+E+E, padx=2, pady=1)
btn_sqroot.grid(row=5, column=3, sticky=W+N+S+E, padx=2, pady=1)

btn_factorial.grid(row=2, column=5, sticky=W+N+S+E, padx=2, pady=1)
btn_del.grid(row=3, column=5, sticky=W+N+S+E, padx=2, pady=1)
btn_delall.grid(row=4, column=5, sticky=W+N+S+E, padx=2, pady=1)
btn_equal.grid(row=5, column=5, sticky=W+N+S+E, padx=2, pady=1)

btn_clearhstr.grid(row=6, column=0, columnspan=6, sticky=W+N+S+E, padx=2, pady=1)
root.mainloop()