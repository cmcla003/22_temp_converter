from tkinter import *
from functools import partial # to prevent unwanted windows
import random


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
                                  command=partial(self.close_history, partner))
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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()

