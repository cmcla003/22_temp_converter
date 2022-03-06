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

        # export button (row1)
        self.export_button = Button(self.converter_frame, text="Export",
                                  font=("Arial 14 bold"),
                                  padx=10,pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)
        get_export.export_text.configure()

class Export:
    def __init__(self, partner):

        background_colour = "lemon chiffon"

        #disable export button
        partner.export_button.config(state=DISABLED)

        #set up Child window
        self.export_box = Toplevel()

        # if user press cross at top, closes export and releases button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI
        self.export_frame = Frame(self.export_box,width=300, bg=background_colour,
                                    pady=10)
        self.export_frame.grid()

        # export heading (row 0)
        self.export_label = Label(self.export_frame, text="Export File",
                                          font="Arial 16 bold",
                                          bg=background_colour,
                                          padx=10,pady=10)
        self.export_label.grid(row=0)

        # export text (row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below "
                                                         "and press the save button "
                                 "to save your calculation history to a text file.",
                               justify=LEFT, width=40, bg=background_colour, wrap=250, padx=10, pady=10)
        self.export_text.grid(row=1)

        # export warning text (row 2)
        self.export_warn_text = Label(self.export_frame, text="If the filename you enter already exists, its "
                                                         "contents with be replaced with the current calculation history. ",
                                 font = "Arial 10 italic", justify=LEFT, width=40,
                                 bg="pale violet red",fg="maroon", wrap=225, padx=10, pady=10)
        self.export_warn_text.grid(row=2)
        # Entry box for filename (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                      font="Arial 14 bold")
        self.filename_entry.grid(row=3)


        # Buttons
        # Save/ Cancel buttons (row 4)
        self.export_dismiss_frame = Frame(self.export_frame)
        self.export_dismiss_frame.grid(row=4, pady=10)

        # Save Button
        self.save_btn = Button(self.export_dismiss_frame, text="Save",
                                 font="Arial 10 bold",
                                 command=partial(self.close_export, partner))
        self.save_btn.grid(row=0, column=0)

        # Cancel button
        self.cancel_btn = Button(self.export_dismiss_frame, text="Cancel",
                                  font="Arial 10 bold",
                                  command=partial(self.close_export, partner))
        self.cancel_btn.grid(row=0, column=1)

    def close_export(self,partner):

        #reset export button
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()

