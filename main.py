from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=60, height=70)
window.config(padx=20,pady=20)


# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
print(entry.get())
entry.grid(column=1, row=0)


# Labels
label = Label(text="miles")

label.grid(column=2, row=0)

# Labels
label = Label(text="is equal to")

label.grid(column=0, row=1)

# Labels
show_label = Label(text="0")

show_label.grid(column=1, row=1)

label = Label(text="Km")

label.grid(column=2, row=1)
# Buttons


def calculate():
    miles_int = int(entry.get())
    km = round(miles_int * 1.6)
    show_label.config(text=km)


# calls action() when pressed
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)







window.mainloop()