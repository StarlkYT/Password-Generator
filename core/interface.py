import tkinter
from .generator import generator

class Interface:
    """
    Main class for the graphical user interface.
    """
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("250x350")
        self.root.resizable(False, False)
        self.root.title("Password Generator")

        self.checked_alphabet = tkinter.IntVar()
        self.checked_numeric  = tkinter.IntVar()
        self.checked_special  = tkinter.IntVar()

    def start(self):
        _password = generator(self.length_scale.get(), self.checked_alphabet.get(), self.checked_numeric.get(), self.checked_special.get())
        self.password_label.configure(text=_password)

    def menu(self):
        self.label_frame = tkinter.LabelFrame(self.root, text="Settings:")

        # "Password length" & Horizontal scale
        self.length_label = tkinter.Label(self.label_frame, text="Password length:")
        self.length_scale = tkinter.Scale(self.label_frame, from_=2, to=32, orient=tkinter.HORIZONTAL)

        self.alphabet_checkbox = tkinter.Checkbutton(self.label_frame,  text="Contains letters ",  variable=self.checked_alphabet)
        self.numeric_checkbox  = tkinter.Checkbutton(self.label_frame,  text="Contains numbers ",  variable=self.checked_numeric)
        self.special_checkbox  = tkinter.Checkbutton(self.label_frame,  text="Contains specials",  variable=self.checked_special)

        # "Enter" to get password & {password} label
        self.password_label        = tkinter.Label(self.label_frame, text="")
        self.password_enter_button = tkinter.Button(self.label_frame, text="Enter", command=self.start)

        # Packs
        self.label_frame.place(x=125, y=155, anchor=tkinter.CENTER)

        # Check boxes:
        self.alphabet_checkbox.pack()
        self.numeric_checkbox.pack()
        self.special_checkbox.pack()

        # Scale length password
        self.length_label.pack()
        self.length_scale.pack()

        # Show password
        self.password_label.pack()
        self.password_enter_button.pack()

    def show(self):
        self.menu()
        self.root.mainloop()
