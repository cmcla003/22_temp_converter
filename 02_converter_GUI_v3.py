from tkinter import *
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

        self.history_btn = Button(self.hist_help_frame,
                                  text="Calculation History", font="Arial 10 italic",
                                  bg="gainsboro", width=15, padx=10, pady=10,
                                 command=lambda: self.history(self.all_calc_list))
        self.history_btn.grid(row=0, column=0)

        if len(self.all_calc_list)==0:
            self.history_btn.config(state=DISABLED)

        self.help_btn = Button(self.hist_help_frame, text="Help",
                                  font=("Arial 10 italic"),
                                  bg="gainsboro",width=5, padx=10, pady=10)
        self.help_btn.grid(row=0,column=1)


    def temp_convert(self,low):
        print(low)
        error = "tomato"

        # retrieve amount entered into entry feild
        to_convert = self.to_convert_entry.get()

        # check amount is valid number
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # convert to F
            if low == -273 and to_convert >=low:
                farenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                farenheit = self.round_it(farenheit)
                answer = "{} degress C is {} degrees F".format(to_convert,farenheit)

            # convert to C
            elif low == -459 and to_convert >=low:
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

        except ValueError:
            self.converted_label.configure(text = "Enter a number", fg="orange red")
            self.to_convert_entry.configure(bg=error)

        # add answer to list for history
        if answer != "Too cold!!!":
            self.all_calc_list.append(answer)
            print(self.all_calc_list)

    # round number
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round,1)

        return rounded


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
