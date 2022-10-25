from tkinter import *
import csv
from tkinter import messagebox

contact_list = []


def open_file():
    with open('phone_agenda.txt',  'r') as file:
        reader = csv.reader(file, delimiter=',')
        for elem in reader:
            contact_list.append(elem)
            set_select()
    print(contact_list)


def save_file(contact_list):
    with open('phone_agenda.txt', 'w', newline='') as csv_file:
        save_file=csv.writer(csv_file, delimiter=',')
        for row in contact_list:
            save_file.writerow(row)



def selectare():
    print("hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("EROARE!", "Va rugam introduce-ti nume!")
    else:
        return int(select.curselection()[0])


def AddDetail():
    if E_name.get() != "" and E_last_name.get() != "" and E_contact.get() != "":
        if E_contact.get().isdigit():
            contact_list.append([E_name.get() + ' ' + E_last_name.get(), E_contact.get()])
            save_file(contact_list)
            set_select()
            EntryReset()
            messagebox.showinfo('CONFIRMARE!', "Contact nou adaugat cu SUCCES!")
        else:
            messagebox.showerror("EROARE!", "Va rugam introduce-ti un numarul de telefon valid!!")

    else:
        messagebox.showerror("EROARE!", "Va rugam completa-ti toate campurile!")
    print('din add detail()',contact_list)


def UpdateDetail():
    if E_name.get() and E_last_name.get() and E_contact.get():
        contact_list[selectare()] = [E_name.get() + ' ' + E_last_name.get(), E_contact.get()]
        save_file(contact_list)
        messagebox.showinfo('CONFIRMARE!', "Contact actualizat cu SUCCES!")
        EntryReset()
        set_select()

    elif not (E_name.get()) and not (E_last_name.get()) and not (E_contact.get()) and not (
            len(select.curselection()) == 0):
        messagebox.showerror("EROARE!", "Selectati date pentru actualizare!")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("EROARE!", "Va rugam selectati numele \n si apasati butonul de Incarcare")
        else:
            message1 = """Pentru incarcare date \n 
		                    selectati campul si apasati Actualizare\n.
						  """
            messagebox.showerror("Error", message1)


def EntryReset():
    E_name_var.set('')
    E_last_name_var.set('')
    E_contact_var.set('')


def DeleteEntry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('CONFIRMARE!', 'DORITI SA STERGE-TI\n SELECTARE')
        if result == True:
            del contact_list[selectare()]
            save_file(contact_list)
            set_select()
    else:
        messagebox.showerror("EROARE!", 'Va rugam selectati numele')


def LoadEntry():
    name, phone = contact_list[selectare()]
    print(name.split(' '))
    E_name_var.set(name.split()[0])
    E_last_name_var.set(name.split()[1])
    E_contact_var.set(phone)

def ExitEntry():
    msg_box = messagebox.askquestion('IESIRE DIN APLICATIE!', 'Sunteti sigur ca vreti sa iesiti?',
                                        icon='info')
    if msg_box == 'yes':
        window.destroy()


def set_select():
    contact_list.sort(key=lambda elem:elem[0])
    select.delete(0, END)
    i = 0
    for name, phone in contact_list:
        i += 1
        select.insert(END, f"{i}  {name} : {phone}")


window = Tk()

img = PhotoImage(file = 'PngItem_3858268.png')

Frame1 = LabelFrame(window, text="PHONE-AGENDA",bg='lightblue')
Frame1.grid(padx=100, pady=100)

Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0, column=0, padx=50, pady=50)

l_name = Label(Inside_Frame1, text="Nume",bg='lightblue')
l_name.grid(row=0, column=0, padx=5, pady=5)
E_name_var = StringVar()

E_name = Entry(Inside_Frame1, width=30, textvariable=E_name_var)
E_name.grid(row=0, column=1, padx=5, pady=5)

l_last_name = Label(Inside_Frame1, text="Prenume",bg='lightblue')
l_last_name.grid(row=1, column=0, padx=5, pady=5)
E_last_name_var = StringVar()
E_last_name = Entry(Inside_Frame1, width=30, textvariable=E_last_name_var)
E_last_name.grid(row=1, column=1, padx=5, pady=5)

l_contact = Label(Inside_Frame1, text="Numar de telefon",bg='lightblue')
l_contact.grid(row=2, column=0, padx=5, pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1, width=30, textvariable=E_contact_var)
E_contact.grid(row=2, column=1, padx=5, pady=5)

Frame2 = Frame(window)
Frame2.grid(row=0, column=1, padx=15, pady=15, sticky=E)

Add_button = Button(Frame2, text="Adauga contact", width=15, bg="MediumSeaGreen", fg="black", command=AddDetail)
Add_button.grid(row=0, column=0, padx=8, pady=8)

Update_button = Button(Frame2, text="Actualizeaza contact", width=15, bg="lightblue", fg="black", command=UpdateDetail)
Update_button.grid(row=1, column=0, padx=8, pady=8)

Reset_button = Button(Frame2, text="Reseteaza", width=15, bg="lightyellow", fg="black", command=EntryReset)
Reset_button.grid(row=2, column=0, padx=8, pady=8)
# ----------------------------------------------------------------------------

DisplayFrame = Frame(window)
DisplayFrame.grid(row=1, column=0, padx=10, pady=10)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set, font=("Arial Bold", 12),bg="#282923",fg="SandyBrown",width=40,
                 height=15, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
select.grid(row=0, column=0, sticky=W)
scroll.grid(row=0, column=1, sticky=N + S)

# -----------------------------------------------------------------------------------
ActionFrame = Frame(window)
ActionFrame.grid(row=1, column=1, padx=15, pady=15, sticky=E)

Delete_button = Button(ActionFrame, text="Sterge", width=15, bg="darkred", fg="black", command=DeleteEntry)
Delete_button.grid(row=0, column=0, padx=5, pady=5, sticky=S)

Loadbutton = Button(ActionFrame, text="Incarca editare", width=15, bg="DarkGoldenRod", fg="black", command=LoadEntry)
Loadbutton.grid(row=1, column=0, padx=5, pady=5)

Exit_button = Button(ActionFrame, text="Iesire", width=15, bg="red", fg="white", command=ExitEntry)
Exit_button.grid(row=2, column=0, padx=5, pady=5, sticky=S)

# --------------------------------- de aici ruleaza programul


open_file()

window.mainloop()