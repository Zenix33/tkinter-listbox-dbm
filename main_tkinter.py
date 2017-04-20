
import tkinter as tk
import dbm

def ajout_item():
    """
    add an entrie to the list
    """
    listbox1.insert(tk.END, entrer1.get())
    fichier[entrer1.get()] = entrer1.get()
    get_list()

def supp_item():
    """
    delete the selected line
    """
    try:
        index = listbox1.curselection()
        del fichier[listbox1.get(index)]
        listbox1.delete(index)
        get_list()
    except IndexError:
        pass

def get_list():

    listbox1.delete(0, tk.END)
    for i in fichier.items():
        listbox1.insert(0, str(fichier[i[0]].decode("utf_8")) )

def set_list(event):

    try:
        index = listbox1.curselection()[0]
        # supp l'ancien entré
        listbox1.delete(index)
    except IndexError:
        index = tk.END
    # insert edited item back into listbox1 at index
    listbox1.insert(index, entrer1.get())
    get_list()

def save_list():
    # get the line on the listebox
    temp_list = list(listbox1.get(0, tk.END))
    # add to the next line
    temp_list = [chem + '\n' for chem in temp_list]

    fout.writelines(temp_list)
    fout.close()

def show_selection(event):
    entryVar = listbox1.get(listbox1.curselection())
    entrer1.delete(0,50)
    entrer1.insert(0,entryVar)

root = tk.Tk()
root.title("liste des étudi&nts")  # titre de la fenetre
# create a listbox
listbox1 = tk.Listbox(root, width=50, height=10)
listbox1.grid(row=0, column=0)

# scrollbar
yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N + tk.S)
listbox1.configure(yscrollcommand=yscroll.set)

entryVar = tk.StringVar()
entryVar=""
entrer1 = tk.Entry(root, width=50, bg='yellow', textvariable=entryVar)
#entrer1.insert(0, '')
entrer1.grid(row=1, column=0)
# pressing the return key will update edited line
entrer1.bind('<Return>', set_list)
# or double click left mouse button to update line
entrer1.bind('<Double-1>', set_list)

# button to add a line to the listbox
button3 = tk.Button(root, text='ajouter', command=ajout_item)
button3.grid(row=2, column=0, sticky=tk.E)

# button to delete a line from listbox
button4 = tk.Button(root, text='supprimer', command=supp_item)
button4.grid(row=3, column=0, sticky=tk.E)

fichier = dbm.open("liste", "c" )
get_list()
# left mouse click on a list item to display selection
listbox1.bind('<ButtonRelease-1>', show_selection)

root.mainloop()
fichier.close()
# les entrées sont automiquement sauvegarder dans un fichier liste.dir a la fermeture de la fenetre