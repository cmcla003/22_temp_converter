from tkinter import *
from functools import partial # to prevent unwanted windows
import random
import re


class Converter:
    def __init__(self, parent):
        #formatting variables
        background_colour = "light gray"

        # list of conversions (in converter GUI this is a blank list populated with user calculations
        self.all_calc_list = ['12 degrees C is 53.6 degrees F',
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 37.8 degrees F']

        '''self.all_calc_list = []'''

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

        # history button (row1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font="Arial 14 bold",padx=10,pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        print("History")
        get_history = History(self, calc_history)
        get_history.history_text.configure()

class History:
    def __init__(self, partner, calc_history):

        background_colour = "light blue"

        #disable history button
        partner.history_button.config(state=DISABLED)

        #set up Child window
        self.history_box = Toplevel()

        # if user press cross at top, closes history and releases button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI
        self.history_frame = Frame(self.history_box,width=300, bg=background_colour,
                                    pady=10)
        self.history_frame.grid()

        # history heading (row 0)
        self.history_label = Label(self.history_frame, text="Calculation History",
                                          font=("Arial", "16", "bold"),
                                          bg=background_colour,
                                          padx=10,pady=10)
        self.history_label.grid(row=0)

        # history text (row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent entries. "
                                  "Use the Export button to create a file of all your calculations",
                               font = "Arial 10 italic",wrap=250,
                               justify=LEFT, bg=background_colour,)
        self.history_text.grid(row=1)

        # History Output goes here (row 2)
        # generate a string from list of calculations
        history_string = ""

        if len(calc_history) >7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history) - item -1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] +"\n"
                self.history_text.config(text="Here is your calculation history "
                                         "You can use the export button to save this data to a file")

        # Display results to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background_colour, font="Arial 14", justify=LEFT)
        self.calc_label.grid(row=2)

        # Dismiss/export button (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_btn = Button(self.export_dismiss_frame, text="Export",
                                 font="Arial 10 bold",
                                  command=lambda: self.export(calc_history))
        self.export_btn.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 10 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)


    def close_history(self,partner):
        #reset history button
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self,calc_history):
        Export(self,calc_history)

class Export:
    def __init__(self, partner,calc_history):

        print(calc_history)

        background_colour = "lemon chiffon"

        #disable export button
        partner.export_btn.config(state=DISABLED)

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

        # Error message labels (row 4)
        self.save_error_label = Label(self.export_frame, text="",fg="maroon", bg=background_colour)
        self.save_error_label.grid(row=4)


        # Buttons
        # Save/ Cancel buttons (row 5)
        self.export_dismiss_frame = Frame(self.export_frame)
        self.export_dismiss_frame.grid(row=5, pady=10)

        # Save Button
        self.save_btn = Button(self.export_dismiss_frame, text="Save",
                                 font="Arial 10 bold",
                                 command=partial(lambda:self.save_history(partner, calc_history)))
        self.save_btn.grid(row=0, column=0)

        # Cancel button
        self.cancel_btn = Button(self.export_dismiss_frame, text="Cancel",
                                  font="Arial 10 bold",
                                  command=partial(self.close_export, partner))
        self.cancel_btn.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        valid_char = "[A-Za-z0-9_]"
        has_errors = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "no spaces allowed"

            else:
                problem = "no {} allowed".format(letter)
            has_errors = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_errors = "yes"

        if has_errors == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filemane - {}".format(problem))
            # Change background
            self.filename_entry.configure(bg="orange red")
            print()

        # correct file name
        else:

            # add .txt suffix
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at the end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self,partner):

        #reset export button
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
