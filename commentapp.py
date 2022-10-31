from tkinter import *
import time

root = Tk()
root.title("Aplikasi Comment")
root.geometry('600x600')
root.resizable(0, 0)

# membuat fungsi
envar2 = StringVar()
envar3 = StringVar()
envar4 = StringVar()
envar4.set(time.asctime(time.localtime(time.time())))
def send():
    mystuff = ( ("{}\nNama: {}\nUsername: {}\nPesan:{}\n").format(entry4.get(), entry2.get(), entry3.get(), text1.get(1.0, END)) )
    text_file = open("C:/Users/Alex/OneDrive/Dokumen/PY_PROGRAM/program/data/data.txt", 'a')
    stuff = text_file.write(mystuff)
    text_file.close()
    envar4.set(time.asctime(time.localtime(time.time())))
    text1.delete(1.0, END)

# membuat label
label1 = Label(root, font=('Helvatica 14'), text="Pemograman Comment and Notes")
label2 = Label(root, font=('Helvatica 12'), text="Nama")
label3 = Label(root, font=('Helvatica 12'), text="Username")
label4 = Label(root, font=('Helvatica 12'), text="Tanggal")

# menbuat enrty
entry2 = Entry(root, font=('Helvatica 12'), width=30, textvariable= envar2)
entry3 = Entry(root, font=('Helvatica 12'), width=30, textvariable= envar3)
entry4 = Entry(root, font=('Helvatica 12'), width=30, textvariable= envar4)

# membuat text, scrollbar
frame1 = Frame(root, width=200, height=100, bg='lightgrey', borderwidth=5, border=5)
scrollbar = Scrollbar(frame1, orient=VERTICAL, command=YView)
text1 = Text(frame1, font=('Helvatica 12'), width=60, height=17, yscrollcommand=scrollbar.set)
scrollbar.config(command=text1.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text1.pack()

# membuat button
send_button = Button(root, width=10, height=1, font=('Helvatica 12'), text="Send", command=send)

# grid
label1.grid(row=0, column=0, columnspan=5, padx=10, pady=20)
label2.grid(row=1, column=0, sticky=W+S+N, padx=10, pady=10)
label3.grid(row=2, column=0, sticky=W+S+N, padx=10, pady=10)
label4.grid(row=3, column=0, sticky=W+S+N, padx=10, pady=10)

entry2.grid(row=1, column=1, sticky=W+S+N, padx=10, pady=10)
entry3.grid(row=2, column=1, sticky=W+S+N, padx=10, pady=10)
entry4.grid(row=3, column=1, sticky=W+S+N, padx=10, pady=10)

send_button.grid(row=4, column=0, sticky=W+S+N, padx=10, pady=10)

frame1.grid(row=5, column=0, columnspan=5, sticky=W+S+N, padx=5, pady=10)

root.mainloop()