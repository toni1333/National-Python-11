from tkinter import *
import csv
from tkinter import messagebox

contact_list = []                # se incarca ca si..  ['a  b','99']


def open_file():
    with open('phone_agenda.txt',  'r') as file:
        reader = csv.reader(file, delimiter=',')
        for elem in reader:             # citeste linie cu linie
            contact_list.append(elem)
            select_set()                # cu 'select.insert(...)'  afisez in widget lista citita
    print('open_file',contact_list)


def save_file(contact_list):               # se apeleaza in 3 locuri 1add, 2update, 3delete
    with open('phone_agenda.txt', 'w', newline='') as csv_file:
        save_file=csv.writer(csv_file, delimiter=',')
        for row in contact_list:
            save_file.writerow(row)



def selectare():
    print("len cursor", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("EROARE!", "Selectati un nume pentru actualizare date!")
    else:
        return int(select.curselection()[0])       # returneaza un int pt incarcare contact_list si indexul de tip int


def adddetail():
    if E_name.get() != "" and E_last_name.get() != "" and E_contact.get() != "":
        if E_contact.get().isdigit():                # validare numar daca este digit merge mai departe
            contact_list.append([E_name.get() + ' ' + E_last_name.get(), E_contact.get()])
            save_file(contact_list)
            select_set()
            entryreset()
            messagebox.showinfo('CONFIRMARE!', "Contact nou adaugat cu SUCCES!")
        else:
            messagebox.showerror("EROARE!", "Va rugam introduce-ti un numarul de telefon valid!!")

    else:
        messagebox.showerror("EROARE!", "Va rugam completa-ti toate campurile!")



def updatedetail():
    if E_name.get() and E_last_name.get() and E_contact.get():
        if E_contact.get().isdigit():
            contact_list[selectare()] = [E_name.get() + ' ' + E_last_name.get(), E_contact.get()]
            save_file(contact_list)
            messagebox.showinfo('CONFIRMARE!', "Contact actualizat cu SUCCES!")
            entryreset()
            select_set()
        else:
            messagebox.showerror("EROARE!", "Va rugam introduce-ti un numarul de telefon valid!!")
    elif not (E_name.get()) and not (E_last_name.get()) and not (E_contact.get()) and not (
            len(select.curselection()) == 0):
        messagebox.showerror("EROARE!", "Selectati date pentru actualizare!")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("EROARE!", "Va rugam incarcati toate campurile \n si apasati butonul de Actualizare")
        else:
            message1 = """Pentru incarcare date selectati campul si apasati Actualizare!"""
            messagebox.showerror("Error", message1)


def entryreset():                       # ca sa-mi inlature datele din label nume etc...
    E_name_var.set('')
    E_last_name_var.set('')
    E_contact_var.set('')


def deleteEntry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('CONFIRMARE!', 'DORITI SA STERGE-TI\n SELECTARE')
        if result == True:
            del contact_list[selectare()]
            save_file(contact_list)
            select_set()
    else:
        messagebox.showerror("EROARE!", 'Va rugam selectati un nume pentru a sterge')


def loadentry():
    name, phone = contact_list[selectare()]
    print(name.split(' '))                      # cu split() impart in doua index[0] si index[1] din contact_list
    E_name_var.set(name.split()[0])             # nume aloc index[0]
    E_last_name_var.set(name.split()[1])        # l_nume aloc din index[1]
    E_contact_var.set(phone)

def exitentry():
    msg_box = messagebox.askquestion('IESIRE DIN APLICATIE!', 'Sunteti sigur ca vreti sa iesiti?',
                                        icon='info')
    if msg_box == 'yes':
        window.destroy()


def select_set():
    contact_list.sort()             # sorteaza dupa litera nume...
    select.delete(0, END)
    i = 0
    for name, phone in contact_list:
        i += 1
        select.insert(END, f"{i}  {name} : {phone}")


window = Tk()

img = PhotoImage(file = 'PngItem_3858268.png')

#---------  prima fereastra stanga sus

Frame1 = LabelFrame(window, text="PHONE-AGENDA",bg='lightblue')
Frame1.grid(padx=100, pady=100)
#------- fereastra mai mica in prima fereastra

Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0, column=0, padx=50, pady=50)
#------- declarat 3 label-uri

l_name = Label(Inside_Frame1, text="Nume",bg='lightblue',font=("Arial Bold", 11))
l_name.grid(row=0, column=0, padx=5, pady=5)
E_name_var = StringVar()
E_name = Entry(Inside_Frame1, width=30, textvariable=E_name_var,font=("Arial Bold", 11))
E_name.grid(row=0, column=1, padx=5, pady=5)
l_last_name = Label(Inside_Frame1, text="Prenume",bg='lightblue',font=("Arial Bold", 11))
l_last_name.grid(row=1, column=0, padx=5, pady=5)
E_last_name_var = StringVar()         # string1
E_last_name = Entry(Inside_Frame1, width=30, textvariable=E_last_name_var,font=("Arial Bold", 11))
E_last_name.grid(row=1, column=1, padx=5, pady=5)

l_contact = Label(Inside_Frame1, text="Numar de telefon",bg='lightblue',font=("Arial Bold", 11))
l_contact.grid(row=2, column=0, padx=5, pady=5)
E_contact_var = StringVar()           # string2
E_contact = Entry(Inside_Frame1, width=30, textvariable=E_contact_var,font=("Arial Bold", 11))
E_contact.grid(row=2, column=1, padx=5, pady=5)

#------------ a 2 a fereastra dreapta sus

Frame2 = Frame(window)
Frame2.grid(row=0, column=1, padx=15, pady=15, sticky=E)   # row0 col1 alipit Dreapta sau sticky=EST legata de fereastra 3

#---------- 3 butoane   add update reset

Add_button = Button(Frame2, text="Adauga contact", width=15, bg="MediumSeaGreen", fg="black", command=adddetail)
Add_button.grid(row=0, column=0, padx=8, pady=8)

Update_button = Button(Frame2, text="Actualizeaza contact", width=15, bg="lightblue", fg="black", command=updatedetail)
Update_button.grid(row=1, column=0, padx=8, pady=8)

Reset_button = Button(Frame2, text="Reseteaza", width=15, bg="lightyellow", fg="black", command=entryreset)
Reset_button.grid(row=2, column=0, padx=8, pady=8)

# ---------- fereastra Display unde se afiseaza ['nume prenume', 'numarTelefon'] widget  are si scroll

DisplayFrame = Frame(window)
DisplayFrame.grid(row=1, column=0, padx=10, pady=10)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set, font=("Arial Bold", 12),bg="#282923",fg="SandyBrown",width=40,
                 height=15, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
select.grid(row=0, column=0, sticky=W)
scroll.grid(row=0, column=1, sticky=N + S)

# --------------- fereastra a 3 a jos dreapta

ActionFrame = Frame(window)
ActionFrame.grid(row=1, column=1, padx=15, pady=15, sticky=E)             #-- row1 col1 alipit Dreapta sau EST

#------   3 butoane delete load exit

Delete_button = Button(ActionFrame, text="Sterge", width=15, bg="darkred", fg="black", command=deleteEntry)
Delete_button.grid(row=0, column=0, padx=5, pady=5, sticky=S)

Loadbutton = Button(ActionFrame, text="Incarca editare", width=15, bg="DarkGoldenRod", fg="black", command=loadentry)
Loadbutton.grid(row=1, column=0, padx=5, pady=5)

Exit_button = Button(ActionFrame, text="Iesire", width=15, bg="red", fg="white", command=exitentry)
Exit_button.grid(row=2, column=0, padx=5, pady=5, sticky=S)

# --------------------------------- de aici ruleaza programul ---------------------------------


open_file()

window.mainloop()