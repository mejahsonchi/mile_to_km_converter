from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=60, height=70)
window.config(padx=20, pady=20)


# Entries
miles_input = Entry(width=30)
# Add some text to begin with
miles_input.insert(END, string="0")
# Gets text in entry
#print(entry.get())
miles_input.grid(column=1, row=0)


# Labels
miles_label = Label(text="miles")

miles_label.grid(column=2, row=0)

# Labels
equal_to_label = Label(text="is equal to")

equal_to_label.grid(column=0, row=1)

# Labels
show_label = Label(text="0")

show_label.grid(column=1, row=1)

km_label = Label(text="Km")

km_label.grid(column=2, row=1)
# Buttons


def calculate():
    miles_int = float(miles_input.get())
    km = round(miles_int * 1.609)
    show_label.config(text=f"{km}")


# calls action() when pressed
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)







window.mainloop()