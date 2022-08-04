from distutils.log import error
from tkinter import *
from tkinter import messagebox
from app import APINotFound, Weather, CityNotFound
from tkinter import messagebox


class UI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()
        self.pack()
        self.wea = Weather()
        self.ERRORS_LIST = ["empty_city"]

    def create_widgets(self):
        root.geometry("500x500")

        self.city_value = StringVar()

        # ----------------------Functions to fetch and display weather info
        self.city_head = Label(root, text="Enter City Name", font="Helvetica").pack(
            pady=10
        )  # to generate label heading
        self.inp_city = Entry(
            root, textvariable=self.city_value, width=24, font="Helvetica 11"
        ).pack()
        Button(
            root,
            command=self.show_output,
            text="Check Weather",
            font="Helvetica 10",
            bg="white",
            fg="black",
            padx=5,
            pady=5,
        ).pack(pady=20)

        self.fahrenheit = IntVar()
        self.c1 = Checkbutton(
            root,
            text="Fahrenheit ",
            variable=self.fahrenheit,
            onvalue=1,
            offvalue=0,
            command=self.show_output,
        )
        self.c1.pack()

        self.weather = Label(text="", font="Helvetica 12")
        self.output_field = Text(width=46, height=10)

    def show_output(self):
        if self.city_value.get() != "":
            self.weather["text"] = "The weather is: "

            try:

                if self.fahrenheit == 1:
                    print("farenheit")

                    self.output_field.delete("1.0", END)
                    self.output_field.insert(
                        INSERT,
                        self.wea.showWeather(
                            self.city_value.get(), self.fahrenheit.get()
                        ),
                    )
                else:
                    print("celcius")

                    self.output_field.delete("1.0", END)
                    self.output_field.insert(
                        INSERT,
                        self.wea.showWeather(
                            self.city_value.get(), self.fahrenheit.get()
                        ),
                    )
                    self.weather.pack()
                    self.output_field.pack()
                    self.c1.pack()
            except CityNotFound as err:
                self.error(err.msg)
            except APINotFound as err:
                self.error(err.msg)
        else:
            self.error("The city cannot be empty.")

    def error(self, msg):
        messagebox.showerror("ERROR", msg)


root = Tk()
root.title("Weather App")
root.protocol("WM_DELETE_WINDOW", quit)

def initUI():    
    mf = UI(root)
    root.mainloop()
