from tkinter import *
import random


class Converter:
    def __init__(self, parent):

        # Formatting variables
        background_colour = "tomato"

        # Converter frame
        self.converter_frame= Frame(width=300, bg=background_colour,
                                    pady=10)
        self.converter_frame.grid()

        # Temp Converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial 16 bold"),
                                          bg=background_colour,
                                          padx=10,pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type the number you wish to convert and "
                                                  "then push one of the buttons below",
                                             font="Arial 10 italic", wrap=250,
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
                                  text = "Centigrade", font="Arial 10 bold",
                                  bg="yellow green", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        # Farenheit button (light goldenrod)
        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text = "Farenheit", font="Arial 10 bold",
                                  bg="light goldenrod", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.conversion_answer_label = Label(self.converter_frame, text="Answer goes here",
                                             font="Arial 18 bold",
                                             bg=background_colour,
                                             padx=10, pady=10)
        self.conversion_answer_label.grid(row=4)

        # History/Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10, padx=10)

        self.to_history = Button(self.hist_help_frame,
                                  text="Calculation History", font="Arial 10 italic",
                                  bg="gainsboro", width=15, padx=10, pady=10)
        self.to_history.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, text="Help",
                                  font=("Arial 10 italic"),
                                  bg="gainsboro",width=5, padx=10, pady=10)
        self.help_button.grid(row=0,column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
