from tkinter import *

def populate_list():
    print('Populate')

def add_item():
    print('Add')

def remove_item():
    print('Remove')

def update_item():
    print('Update')

def clear_text():
    print('Clear')

app = Tk()

# Pet Supplies------------------------------------
pet_text = StringVar()
pet_label = Label(app, text='Pet Supply Name', font=('bold', 14))
pet_label.grid(row=0, column=2, sticky=W)
pet_entry = Entry(app, textvariable=pet_text)
pet_entry.grid(row=0, column=1)
# Customer --------------------------------------
customer_text = StringVar()
customer_label = Label(app, text='Customer Name', font=('bold', 14), pady=20)
customer_label.grid(row=0, column=0, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)
# Retailer ------------------------------------------
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer Name', font=('bold', 14), pady=20)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)
# Price -----------------------------------------------
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14), pady=20)
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

add_btn = Button(app, text='Add Pet Supplies', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Pet Supplies', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Pet Supplies', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Pet Quest')
app.geometry('700x350')

populate_list()

app.mainloop()