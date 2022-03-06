from tkinter import *
from functools import partial # to prevent unwanted windows
import random


class Converter:
    def __init__(self, parent):
        #formatting variables
        background_colour = "tomato"

        # Converter main screen GUI
        self.converter_frame= Frame(width=600, height=600, bg=background_colour,
                                    pady=10)
        self.converter_frame.grid()

        # Temp Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial 16 bold"),
                                          bg=background_colour,
                                          padx=10,pady=10)
        self.temp_converter_label.grid(row=0)

        # Help button (row1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial 14 bold"),
                                  padx=10,pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure()

class Help:
    def __init__(self, partner):

        background_colour = "pale violet red"

        #disable help button
        partner.help_button.config(state=DISABLED)

        #set up Child window
        self.help_box = Toplevel()

        # if user press cross at top, closes help and releases button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI
        self.help_frame = Frame(self.help_box,width=300, bg=background_colour,
                                    pady=10)
        self.help_frame.grid()

        # Help heading (row 0)
        self.help_label = Label(self.help_frame, text="Help",
                                          font=("Arial", "16", "bold"),
                                          bg=background_colour,
                                          padx=10,pady=10)
        self.help_label.grid(row=0)

        # Help text (row 1)
        self.help_text = Label(self.help_frame, text="Instructions",
                               justify=LEFT, width=40, bg=background_colour, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=40,
                                  font="Arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self,partner):

        #reset help button
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()

