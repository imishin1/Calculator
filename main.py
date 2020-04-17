from tkinter import *

class Calculator():
    def __init__(self, root, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.enter_num1 = Entry(root, width=int(WIDTH * 0.8))
        self.enter_num2 = Entry(root, width=int(WIDTH * 0.8))
        self.addition_button = Button(root, command=eval('self.addition'), text='+')
        self.subtraction_button = Button(root, command=eval('self.subtraction'), text='-')
        self.multiplication_button = Button(root, command=eval('self.multiplication'),text='*')
        self.division_button = Button(root,command=eval('self.division') ,text='/')
        self.answer_field = Label(root)

        self.enter_num1.pack()
        self.enter_num2.pack()
        self.addition_button.pack()
        self.subtraction_button.pack()
        self.multiplication_button.pack()
        self.division_button.pack()
        self.answer_field.pack()

    def addition(self):
        try:
            self.answer_field['text'] = str(float(self.enter_num1.get()) + float(self.enter_num2.get()))
        except ValueError:
            self.answer_field['text'] = str('Введите число')
    
    def subtraction(self):
        try:
            self.answer_field['text'] = str(float(self.enter_num1.get()) - float(self.enter_num2.get()))
        except ValueError:
            self.answer_field['text'] = str('Введите число')

    def division(self):
        try:
            self.answer_field['text'] = str(float(self.enter_num1.get()) / float(self.enter_num2.get()))
        except ValueError:
            self.answer_field['text'] = str('Введите число')
        except ZeroDivisionError:
            self.answer_field['text'] = str('Деление на ноль невозможно')

    def multiplication(self):
        try:
            self.answer_field['text'] = str(float(self.enter_num1.get()) * float(self.enter_num2.get()))
        except ValueError:
            self.answer_field['text'] = str('Введите число')

def main():
    root = Tk()

    WIDTH = 250
    HEIGHT = 300

    root.title('Calculator')
    root.geometry(f'{WIDTH}x{HEIGHT}')

    calculator = Calculator(root, WIDTH, HEIGHT)
    root.mainloop()

if __name__ == "__main__":
    main()