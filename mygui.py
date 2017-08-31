#Class header goes here

import tkinter
import tkinter.messagebox

class MyGUI:

    def __init__(self):
        #Create main GUI window
        self.main_window = tkinter.Tk()

        #Create top and bottom frames to hold widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create label in top frame to prompt user
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter number:")

        #Create entry box in top frame for user to enter a number
        self.number_entry = tkinter.Entry(self.top_frame, width=10)

        #Display the label and the entry in the top frame
        self.prompt_label.pack(side='left')
        self.number_entry.pack(side='left')

        #Create the calculate button in bottom frame
        #Should call calculate function when clicked
        self.button_calc = tkinter.Button(self.bottom_frame, text="Calculate", \
                                       command=self.calculate)

        #Create the quit button in bottom frame
        #Should close GUI window when clicked
        self.button_quit = tkinter.Button(self.bottom_frame, text="Quit", \
                                         command=self.main_window.destroy)

        #Make buttons visible in the bottom frame
        self.button_calc.pack(side='left')
        self.button_quit.pack(side='left')

        #Make frames visible in the window
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Call mainloop to display the window
        tkinter.mainloop()

    def calculate(self):
        #Initialize square
        square = 0

        #Retrieve the number entered by the user in the entry box
        number = self.number_entry.get()

        #Check to see if the user entered a value
        if number != "":
            #Convert number entered by user to int
            number = int(number)

            #Calculate square of number entered by user
            square = number**2

        #Display dialog box with the results of the calculation
        tkinter.messagebox.showinfo("Results", str(number) + " squared is " + str(square))
