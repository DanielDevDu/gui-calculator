import customtkinter
from tkinter import *
from calculator import Calculator


customtkinter.set_appearance_mode("Dart")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class ButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.header = customtkinter.CTkLabel(self, text=self.header_name)
        # self.header.grid(row=0, column=0, padx=10, pady=10)

        # self.radio_button_var = customtkinter.StringVar(value="")

        self.button_1 = customtkinter.CTkButton(self, text="1", width=15, height=15)
        self.button_1.grid(row=1, column=0, padx=10, pady=10)
        self.button_2 = customtkinter.CTkButton(self, text="2", width=15, height=15)
        self.button_2.grid(row=1, column=1,padx=10, pady=10)
        self.button_3 = customtkinter.CTkButton(self, text="3", width=15, height=15)
        self.button_3.grid(row=1, column=2,padx=10, pady=10)
        self.button_4 = customtkinter.CTkButton(self, text="4", width=15, height=15)
        self.button_4.grid(row=2, column=0,padx=10, pady=10)
        self.button_5 = customtkinter.CTkButton(self, text="5", width=15, height=15)
        self.button_5.grid(row=2, column=1,padx=10, pady=10)
        self.button_6 = customtkinter.CTkButton(self, text="6", width=15, height=15)
        self.button_6.grid(row=2, column=2,padx=10, pady=10)
        self.button_7 = customtkinter.CTkButton(self, text="7", width=15, height=15)
        self.button_7.grid(row=3, column=0,padx=10, pady=10)
        self.button_8 = customtkinter.CTkButton(self, text="8", width=15, height=15)
        self.button_8.grid(row=3, column=1,padx=10, pady=10)
        self.button_9 = customtkinter.CTkButton(self, text="9", width=15, height=15)
        self.button_9.grid(row=3, column=2,padx=10, pady=10)
        self.button_0 = customtkinter.CTkButton(self, text="0", width=15, height=15)
        self.button_0.grid(row=4, column=1,padx=10, pady=10)

        self.button_plus = customtkinter.CTkButton(self, text="+", width=15, height=15)
        self.button_plus.grid(row=1, column=3,padx=10, pady=10)
        self.button_minus = customtkinter.CTkButton(self, text="-", width=15, height=15)
        self.button_minus.grid(row=2, column=3,padx=10, pady=10)
        self.button_multiply = customtkinter.CTkButton(self, text="*", width=15, height=15)
        self.button_multiply.grid(row=3, column=3,padx=10, pady=10)
        self.button_divide = customtkinter.CTkButton(self, text="/", width=15, height=15)
        self.button_divide.grid(row=4, column=3,padx=10, pady=10)
        self.button_porcent = customtkinter.CTkButton(self, text="%", width=15, height=15)
        self.button_porcent.grid(row=4, column=0,padx=10, pady=10)

        self.button_equal = customtkinter.CTkButton(self, text="=", width=15, height=15)
        self.button_equal.grid(row=4, column=2,padx=10, pady=10)
        self.button_clear = customtkinter.CTkButton(self, text="C", width=15, height=15)
        self.button_clear.grid(row=4, column=0,padx=10, pady=10)



    def get_value(self):
        """ returns selected value as a string, returns an empty string if nothing selected """
        return self.radio_button_var.get()

    def set_value(self, selection):
        """ selects the corresponding radio button, selects nothing if no corresponding radio button """
        self.radio_button_var.set(selection)


class Button:

    width_numbers = 50
    height_numbers  = 50
    fg_color_button = "#7D817A" #"#048300"
    hover_color_button = "#8A8E87"

    width_operators = 30
    height_operators = 30
    hover_color_operators = "#9B5110" #"#5EB90F"
    fg_color_operators = "#7D817A" # "#9B5110"

class App(customtkinter.CTk):
    """
    Calculator
    """
    WIDTH = 300
    HEIGHT = 400
    index = 0
    equation = ""

    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH, App.HEIGHT)
        self.maxsize(App.WIDTH, App.HEIGHT)
        # self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        # self.button.pack(padx=20, pady=20)

        # ============ create two frames ============

        # create 2x1 grid system
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure((4,4), weight=1)

        # self.textbox = customtkinter.CTkTextbox(master=self, width=App.WIDTH*0.95, height=App.HEIGHT*0.05)
        self.textbox = customtkinter.CTkEntry(master=self, text="0", width=App.WIDTH*0.95, height=App.HEIGHT*0.05, fg_color="#414040", border_width=2,
                               corner_radius=10)

        self.textbox.grid(row=0, column=0, pady = (30, 30), padx=App.WIDTH*0.025, columnspan=4)

        # Numbers
        self.button_1 = customtkinter.CTkButton(self, text="1", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(1), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_1.grid(row=1, column=0, padx=10, pady=10)
        self.button_2 = customtkinter.CTkButton(self, text="2", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(2), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_2.grid(row=1, column=1,padx=10, pady=10)
        self.button_3 = customtkinter.CTkButton(self, text="3", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(3), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_3.grid(row=1, column=2,padx=10, pady=10)
        self.button_4 = customtkinter.CTkButton(self, text="4", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(4), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_4.grid(row=2, column=0,padx=10, pady=10)
        self.button_5 = customtkinter.CTkButton(self, text="5", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(5), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_5.grid(row=2, column=1,padx=10, pady=10)
        self.button_6 = customtkinter.CTkButton(self, text="6", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(6), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_6.grid(row=2, column=2,padx=10, pady=10)
        self.button_7 = customtkinter.CTkButton(self, text="7", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(7), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_7.grid(row=3, column=0,padx=10, pady=10)
        self.button_8 = customtkinter.CTkButton(self, text="8", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(8), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_8.grid(row=3, column=1,padx=10, pady=10)
        self.button_9 = customtkinter.CTkButton(self, text="9", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(9), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_9.grid(row=3, column=2,padx=10, pady=10)
        self.button_0 = customtkinter.CTkButton(self, text="0", width=Button.width_numbers, height=Button.height_numbers, command=lambda: self.on_click(0), fg_color=Button.fg_color_button, hover_color=Button.hover_color_button)
        self.button_0.grid(row=4, column=1,padx=10, pady=10)

        # Operators
        self.button_plus = customtkinter.CTkButton(self, text="+", width=Button.width_operators, height=Button.height_operators, command=lambda: self.on_click("+"),  fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.button_plus.grid(row=1, column=3,padx=10, pady=10)
        self.button_minus = customtkinter.CTkButton(self, text="-", width=Button.width_operators, height=Button.height_operators, command=lambda: self.on_click("-"), fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.button_minus.grid(row=2, column=3,padx=10, pady=10)
        self.button_multiply = customtkinter.CTkButton(self, text="*", width=Button.width_operators, height=Button.height_operators, command=lambda: self.on_click("*"), fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.button_multiply.grid(row=3, column=3,padx=10, pady=10)
        self.button_divide = customtkinter.CTkButton(self, text="/", width=Button.width_operators, height=Button.height_operators, command=lambda: self.on_click("/"), fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.button_divide.grid(row=4, column=3,padx=10, pady=10)
        self.button_porcent = customtkinter.CTkButton(self, text="%", width=Button.width_operators, height=Button.height_operators, command=lambda: self.on_click("%"), fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.button_porcent.grid(row=5, column=2,padx=10, pady=10)

        # Parenthesis
        self.parenthesis_left = customtkinter.CTkButton(self, text="(", width=Button.width_operators, height=Button.height_operators, command=lambda: self.on_click("("), fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.parenthesis_left.grid(row=5, column=0,padx=10, pady=10)
        self.parenthesis_right = customtkinter.CTkButton(self, text=")", width=Button.width_operators, height=Button.height_operators, command=lambda: self.on_click(")"), fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.parenthesis_right.grid(row=5, column=1,padx=10, pady=10)

        # Equal
        self.button_equal = customtkinter.CTkButton(self, text="=", width=Button.width_operators, height=Button.height_operators, command=self.calculate, fg_color="#048300", hover_color="#059400")
        self.button_equal.grid(row=5, column=3,padx=10, pady=10)

        # Clear
        self.button_clear = customtkinter.CTkButton(self, text="C", width=Button.width_operators, height=Button.height_operators, command=self.clear, fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.button_clear.grid(row=4, column=0,padx=10, pady=10)

        self.removeOne = customtkinter.CTkButton(self, text="<-", width=Button.width_operators, height=Button.height_operators, command=self.remove, fg_color=Button.fg_color_operators, hover_color=Button.hover_color_operators)
        self.removeOne.grid(row=4, column=2,padx=10, pady=10)






        # self.button_clear = customtkinter.CTkButton(master=self, text="C", command=self.clear)
        # self.button_clear.grid(row=2, column=0, pady = (0, 0), padx=10)

        # self.button0 = customtkinter.CTkButton(master=self, text="0", command=self.button_callback)
        # self.button0.grid(row=1, column=0, pady = (20, 0), padx=10)

        # self.button1 = customtkinter.CTkButton(master=self, text="1", command=self.button_callback)
        # self.button1.grid(row=1, column=1, pady = (20, 0), padx=10)

        # self.button2 = customtkinter.CTkButton(master=self, text="2", command=self.button_callback)
        # self.button2.grid(row=1, column=2, pady = (20, 0), padx=10)

    def on_click(self, value):
        """button callback"""
        self.textbox.insert(self.index, str(value))
        self.index += 1
        self.equation += str(value)

    def clear(self):
        self.textbox.delete(0, 'end')
        self.index = 0
        self.equation = ""

    def calculate(self):
        self.textbox.delete(0, 'end')
        result = eval(self.equation)
        self.textbox.insert(0, result)
    
    def remove(self):
        self.textbox.delete(self.index-1, self.index)
        self.index -= 1
        self.equation = self.equation[:-1]



    def button_event(self):
        print("Login pressed - username:", self.entry_1.get(), "password:", self.entry_2.get())

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()