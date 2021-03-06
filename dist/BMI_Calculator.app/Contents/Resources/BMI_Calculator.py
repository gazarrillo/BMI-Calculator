from tkinter import *

class BMI_GUI:

    def __init__(self):

        self.title_frame = Frame()
        self.top_frame = Frame()
        self.mid_frame = Frame()
        self.mid_frame2 = Frame()
        self.mid_frame3 = Frame()
        self.bottom_frame = Frame()

        self.tile_label = Label(self.title_frame, font=('none', 20),
                                text='Body Mass Index Calculator')
        self.prompt_label1 = Label(self.top_frame,
                                   text='Enter your height in inches:')
        self.prompt_label2 = Label(self.mid_frame,
                                   text='Enter your weight in pounds:')
        self.height_entry = Entry(self.top_frame, width=10)
        self.weight_entry = Entry(self.mid_frame, width=10)

        self.tile_label.pack(side='top')
        self.prompt_label1.pack(side='left')
        self.prompt_label2.pack(side='left')
        self.height_entry.pack(side='left')
        self.weight_entry.pack(side='left')

        self.calc_button = Button(self.bottom_frame,
                                  text='Calculate',
                                  command=self.BMI_Calc)

        self.calc_button.pack(side='left')

        self.descr_label = Label(self.mid_frame2,
                                 text='The Body Mass Index is: ')

        self.value = StringVar()
        self.output_label = Label(self.mid_frame2,
                                  textvariable=self.value)

        self.descr_label.pack(side='left')
        self.output_label.pack(side='left')

        self.diag_label = Label(self.mid_frame3,
                                    text='Your BMI indicates that you are:')

        self.value2 = StringVar()
        self.output_label2 = Label(self.mid_frame3,
                                    textvariable=self.value2)

        self.diag_label.pack(side='left')
        self.output_label2.pack(side='left')

        self.title_frame.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.mid_frame2.pack()
        self.mid_frame3.pack()
        self.bottom_frame.pack()

    def BMI_Calc(self):
        """This function calculates the BMI and diagnoses your weight based on it."""

        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())
        BMI = weight*703/height**2
        self.value.set(round(BMI, 1))

        if BMI <= 15:
            self.value2.set('very severely underweight')
        elif  15 < BMI <= 16:
            self.value2.set('severely underweight')
        elif 16 <= BMI < 18.5:
            self.value2.set('underweight')
        elif 18.5 < BMI <= 25:
            self.value2.set('optimal weight')
        elif 25 <= BMI < 30:
            self.value2.set('overweight')
        elif 30 < BMI <= 35:
            self.value2.set('obese')
        elif 35 <= BMI < 40:
            self.value2.set('severely obese')
        elif 40 < BMI <= 45:
            self.value2.set('very severely obese')
        elif 45 <= BMI < 50:
            self.value2.set('morbidly obese')
        elif 50 < BMI <= 55:
            self.value2.set('super obese')
        elif 60 <= BMI:
            self.value2.set('hyper obese')

root = Tk()
root.title('BMI Calculator')
BMI_GUI()
root.mainloop()
