from tkinter import *
from functools import partial # to prevent unwanted windows
import random

class Converter:
    def __init__(self, parent):

        # Formatting variables
        background_colour = "light gray"

        # Intialise list to hold calculation history
        self.all_calc_list = []

        # Converter frame
        self.converter_frame= Frame(bg=background_colour,
                                    pady=10)
        self.converter_frame.grid()

        # Temp Converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial 20 bold"),
                                          bg=background_colour,
                                          padx=10,pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type the number you wish to convert and "
                                                  "then push one of the buttons below",
                                             font="Arial 10 italic", wrap=290,
                                             justify=LEFT, bg=background_colour,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Converstion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        # Centigrade button (yellow green)
        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text = "Celsius", font="Arial 10 bold",
                                  bg="gold", padx=10, pady=10,
                                  command =lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        # Farenheit button (light goldenrod)
        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text = "Farenheit", font="Arial 10 bold",
                                  bg="yellow", padx=10, pady=10,
                                  command = lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, text="Answer goes here",
                                             font="Arial 18 bold",
                                             bg=background_colour,
                                             padx=10, pady=10)
        self.converted_label.grid(row=4)

        # History/Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10, padx=10)


        # history button (row1)
        self.history_btn = Button(self.hist_help_frame, text="History",
                                     font=("Arial 10 italic"),padx=10,pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_btn.grid(column=0,row=1)

        if len(self.all_calc_list) == 0:
            self.history_btn.config(state=DISABLED)

        # help button
        self.help_btn = Button(self.hist_help_frame, text="Help",
                               font=("Arial 10 italic"),padx=10, pady=10)
        self.help_btn.grid(column=1, row=1)

    def temp_convert(self, low):
        print(low)
        error = "tomato"

        # retrieve amount entered into entry feild
        to_convert = self.to_convert_entry.get()

        # check amount is valid number
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # convert to F
            if low == -273 and to_convert >= low:
                farenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                farenheit = self.round_it(farenheit)
                answer = "{} degress C is {} degrees F".format(to_convert, farenheit)

            # convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degress F is {} degrees C".format(to_convert, celsius)

            else:
                answer = "Too cold!!!"
                has_errors = "yes"

            # display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="black")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="orange red")

            # add answer to list for history
            if has_errors!= "yes":
                self.all_calc_list.append(answer)
                print(self.all_calc_list)
                self.history_btn.config(state=NORMAL)

        except ValueError:
            self.converted_label.configure(text="Enter a number", fg="orange red")
            self.to_convert_entry.configure(bg=error)

    # round number
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

    def history(self, calc_history):
        print("History")
        get_history = History(self, calc_history)
        get_history.history_text.configure()

class History:
    def __init__(self, partner, calc_history):

        background_colour = "light blue"

        #disable history button
        partner.history_btn.config(state=DISABLED)

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
                                  command=self.export)
        self.export_btn.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 10 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)


    def close_history(self,partner):
        #reset history button
        partner.history_btn.config(state=NORMAL)
        self.history_box.destroy()

    def export(self):
        print("You asked for export")
        get_export = Export(self)
        get_export.export_text.configure()

class Export:
    def __init__(self, partner):

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
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
