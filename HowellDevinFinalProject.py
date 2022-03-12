from tkinter import *
from tkinter import messagebox
from db import Database
# from PIL import ImageTk, Image

db = Database('store.db')

def populate_list():
    pet_list.delete(0, END)
    for row in db.fetch():
        pet_list.insert(END, row)

def add_item():
    if pet_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(pet_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    pet_list.delete(0, END)
    pet_list.insert(END, (pet_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = pet_list.curselection()[0]
        selected_item = pet_list.get(index)

        pet_entry.delete(0, END)
        pet_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass
    
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], pet_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    populate_list()

def clear_text():
    pet_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

app = Tk()

# Pet Supplies------------------------------------
pet_text = StringVar()
pet_label = Label(app, text='Pet Supply Name', bg='#856ff8', font=('bold', 14))
pet_label.grid(row=0, column=2, sticky=W)
pet_entry = Entry(app, textvariable=pet_text)
pet_entry.grid(row=0, column=1)
# Customer --------------------------------------
customer_text = StringVar()
customer_label = Label(app, text='Customer Name', bg='#856ff8', font=('bold', 14), pady=20)
customer_label.grid(row=0, column=0, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)
# Retailer ------------------------------------------
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer Name', bg='#856ff8', font=('bold', 14), pady=20)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)
# Price -----------------------------------------------
price_text = StringVar()
price_label = Label(app, text='Price', bg='#856ff8', font=('bold', 14), pady=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)
# List of Supplies -------------------------------------
pet_list = Listbox(app, height=8, width=50, border=0)
pet_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
pet_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=pet_list.yview)

add_btn = Button(app, text='Add Pet Supplies', width=12, bg='#beb4f0', command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Pet Supplies', width=12, bg='#beb4f0',command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Pet Supplies', width=12, bg='#beb4f0', command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, bg='#beb4f0', command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Pet Quest')
app.geometry('700x350')
app['background']='#856ff8'


populate_list()

app.mainloop()