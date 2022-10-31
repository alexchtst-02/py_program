from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
from tkinter import filedialog
import translator as trl 
import kryptography as krp

root = Tk()
root.title('project0.0 by:alexc')
root.geometry('470x500')
root.resizable(0, 0)

#defenisi variable
en_1 = IntVar()
en_2 = StringVar()

# fungsi execute
def execute(event):
    public_key = entry_1.get()
    message = entry_2.get()
    lismessage = list(message)
    '''
    jika entry1 (kosong, input tidak sesuai), 
    entry2 (kosong, input tidak sesuai),
    menentukan secret key sesuai aturan RSA,
    '''
    # membuat exception dari sini
    try:
        for i in lismessage:
            if i.capitalize() not in trl.alphabet or i == '':
                mb.showerror("Eror", "Enskripsi dalam bentuk huruf dan per-kata")
                en_2.set('')
                break
        else:
            if message != '':
                message_in_number = trl.generator(word=message).num()
                j = len(list(message))
                c_text = 0
                for i in trl.generator(num=message_in_number).num_slicer():
                    a = krp.RSA_kriptography(M=i, pk=en_1.get(), p=29, q=3).encript()
                    c_text = c_text + a*(100**(j-1))
                    j = j - 1
                text_0.insert(END, ('{}/').format(c_text))
                en_2.set('')
    except TypeError():
        pass
    except ValueError():
        pass
    except RuntimeError():
        pass

# label
label_0 = Label(root, font=('Times 14 bold'), text='RSA ENCRYPTION')
label_1 = Label(root, font='Times 12', text='Public key')
label_2 = Label(root, font='Times 12', text='Word')
label_3 = Label(root, font='Times 12 bold', text='Chiper txt')

# entry dan combobox
entry_1 = ttk.Combobox(root, font='Times 12', width=20, textvariable=en_1)
entry_1['values'] = [3,5,7,11,13,14,15,16,19,20] # isi supaya memudahkan user
entry_1.set(7)
entry_2 = Entry(root, font='Times 12', width=24, textvariable=en_2, border='1')
entry_2.bind("<Return>", execute)

# frame, scrollbar, text
frame_0 = Frame(root, width=400, height=220, relief='groove', bg='white')
scb_0 = Scrollbar(frame_0, orient=VERTICAL, command=YView)
text_0 = Text(frame_0, font='Times 12', width=50, height=10, border='0', yscrollcommand=scb_0.set)

# fungsi save dan open
def open_text():
    # membuat direktori file tujuan saat membuka file
    dir_file = filedialog.askopenfilename(initialdir="C:/Users/Alex/OneDrive/Dokumen/PY_PROGRAM/KRIPTOGRAPHY/encripted_file/", title="Open file", filetypes=(('Text Files', '*.txt'), ))
    text_file = open(dir_file, 'r')
    stuff = text_file.read()
    text_0.insert(END, stuff)
    text_file.close()

def save_text():
    # membuat direktori file tujuan saat membuka file
    dir_file = filedialog.askopenfilename(initialdir="C:/Users/Alex/OneDrive/Dokumen/PY_PROGRAM/KRIPTOGRAPHY/encripted_file/", title="Open file", filetypes=(('Text Files', '*.txt'), ))
    text_file = open(dir_file, 'w')
    text_file.write(text_0.get(1.0, END))
    text_file.close()

# button
execute_btn = Button(root, font='Times 12', width=10, text='Code', command=execute)
open_button = Button(root, font='Times 12', width=5, text='Open', command=open_text)
save_button = Button(root, font='Times 12', width=5, text='Save', command=save_text)

# grid
label_0.grid(row=0, column=0, columnspan=3, pady=10)
label_1.grid(row=1, column=0, sticky=N+S+W, pady=5, padx=10)
label_2.grid(row=3, column=0, sticky=N+S+W, pady=5, padx=10)
label_3.grid(row=5, column=0, columnspan=3, sticky=S+W, pady=5, padx=10)

entry_1.grid(row=1, column=1, sticky=N+S+W, pady=5)
entry_2.grid(row=3, column=1, sticky=N+S+W, pady=5)

execute_btn.grid(row=4, column=0, columnspan=3, pady=5)
open_button.grid(row=7, column=0, padx=5, sticky=W)
save_button.grid(row=7, column=1, padx=5, sticky=W)

scb_0.config(command=text_0.yview)
frame_0.grid(row=6, column=0, columnspan=3, pady=10, padx=20)
scb_0.pack(side=RIGHT, fill=Y)
text_0.pack(padx=10)

root.mainloop()