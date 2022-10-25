from tkinter import *
import csv
from tkinter import messagebox

phonelist = []


def ReadCSVFile():
    global header

    with open('phone_agenda.txt') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            phonelist.append(row)
    set_select()
    print(phonelist)


def WriteInCSVFile(phonelist):
    with open('phone_agenda.txt', 'w', newline='') as csv_file:
        save_file=csv.writer(csv_file, delimiter=',')
        for row in phonelist:
            save_file.writerow(row)



def WhichSelected():
    print("hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def AddDetail():
    if E_name.get() != "" and E_last_name.get() != "" and E_contact.get() != "":
        phonelist.append([E_name.get() + ' ' + E_last_name.get(), E_contact.get()])
        print(phonelist)
        WriteInCSVFile(phonelist)
        set_select()
        EntryReset()
        messagebox.showinfo("Confermation", "Succesfully Add New Contact")

    else:
        messagebox.showerror("Error", "Please fill the information")


def UpdateDetail():
    if E_name.get() and E_last_name.get() and E_contact.get():
        phonelist[WhichSelected()] = [E_name.get() + ' ' + E_last_name.get(), E_contact.get()]
        WriteInCSVFile(phonelist)
        messagebox.showinfo("Confirmation", "Succesfully Update Contact")
        EntryReset()
        set_select()

    elif not (E_name.get()) and not (E_last_name.get()) and not (E_contact.get()) and not (
            len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill the information")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n 
		                    selected row press Load button\n.
						  """
            messagebox.showerror("Error", message1)


def EntryReset():
    E_name_var.set('')
    E_last_name_var.set('')
    E_contact_var.set('')


def DeleteEntry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result == True:
            del phonelist[WhichSelected()]
            WriteInCSVFile(phonelist)
            set_select()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


def LoadEntry():
    name, phone = phonelist[WhichSelected()]
    print(name.split(' '))
    E_name_var.set(name.split()[0])
    E_last_name_var.set(name.split()[1])
    E_contact_var.set(phone)


def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i = 0
    for name, phone in phonelist:
        i += 1
        select.insert(END, f"{i}   {name}  :     {phone}")


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

Add_button = Button(Frame2, text="Adauga contact", width=15, bg="green", fg="black", command=AddDetail)
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

# --------------------------------- aici ruleaza programul


ReadCSVFile()

window.mainloop()