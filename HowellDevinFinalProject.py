from tkinter import *

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

app.title('Pet Quest')
app.geometry('700x350')

app.mainloop()