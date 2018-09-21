from tkinter import *
from math import *

class Calculator:
    def __init__(self, master):
        self.stored_value = None
        self.master = master
        self.master.title('Calculator')
        self.expression = ''
        self.display = Text(master, width = 30, height = 3)
        self.display.grid(row = 0, column = 0, columnspan = 5, rowspan = 2)
        self.create_buttons()
           
    def button_constructor(self, text, command, row, column): 
        button = Button(self.master, text = text, command = command,bg = 'gray30', fg = 'white', relief = FLAT)
        button.grid(row = row, column = column, sticky = N + S + W + E)
        return button
    
    def create_buttons(self):
        x_squared_button = self.button_constructor('x^2', self.x_squared, 3, 0)
        x_cubed_button = self.button_constructor('x^3', self.x_cubed, 3, 1)
        x_power_of_n_button = self.button_constructor('x^n', self.x_power_of_n, 3, 2)
        off_button = self.button_constructor('OFF', self.clear, 3, 3)
        on_button = self.button_constructor('ON', self.clear, 3, 4)
        left_button = self.button_constructor('<-', self.left, 4, 0)
        right_button = self.button_constructor('->', self.right, 4, 1)
        log_button = self.button_constructor('log', self.log, 4, 2)
        ln_button = self.button_constructor('ln', self.ln, 4, 3)
        sqrt_button = self.button_constructor('sqrt', self.sqrt, 4, 4)
        pi_button = self.button_constructor('pi', self.pi, 5, 0)
        e_button = self.button_constructor('e', self.e, 5, 1)
        arcsin_button = self.button_constructor('asin', self.sin_inverse, 5, 2)
        arccos_button = self.button_constructor('acos', self.cos_inverse, 5, 3)
        arctan_button = self.button_constructor('atan', self.tan_inverse, 5, 4)
        left_bracket_button = self.button_constructor('(', self.left_bracket, 6, 0)
        right_bracket_button = self.button_constructor(')', self.right_bracket, 6, 1)
        sin_button = self.button_constructor('sin', self.sin, 6, 2)
        cos_button = self.button_constructor('cos', self.cos, 6, 3)
        tan_button = self.button_constructor('tan', self.tan, 6, 4)   
        del_button = self.button_constructor('DEL', self.delete, 7, 3)
        ac_button = self.button_constructor('AC', self.ac, 7, 4)
        times_button = self.button_constructor('X', self.times, 8, 3)
        divide_button = self.button_constructor('/', self.divide, 8, 4) 
        plus_button = self.button_constructor('+', self.plus, 9, 3)
        minus_button = self.button_constructor('-', self.minus, 9, 4)
        decimal_button = self.button_constructor('.', self.decimal, 10, 1)
        clear_button = self.button_constructor('C', self.clear, 10, 2)   
        ans_button = self.button_constructor('Ans', self.ans, 10, 3)  
        equal_button = self.button_constructor('=', self.equals, 10, 4)     
        
        for i in range(1, 10):
            if i <= 3:
                row = 9
            elif 4 <= i <= 6:
                row = 8
            else:
                row = 7
            column = (i % 3) - 1 if ((i%3) - 1) >= 0 else 2
            
            new_button = self.button_constructor(i, lambda i=i: self.print_num(i), row = row, column = column)
            
        zero_button = self.button_constructor(0, lambda i=i: self.print_num(0), row = 10, column = 0)       
        
    def print_num(self, number: int):
        self.expression += str(number)
        self.display.insert(END, number)
            
    def x_squared(self):
        self.expression += '** 2'
        self.display.insert(END, '^2')
                
    def x_cubed(self):
        self.expression += '** 3'
        self.display.insert(END, '^3')
    
    def x_power_of_n(self):
        self.expression += '**'
        self.display.insert(END, '^')
    
    def left(self):        
        pass
    
    def right(self):    
        pass
    
    def log(self):
        self.expression += 'log10('
        self.display.insert(END, 'log(')
        
    def ln(self):   
        self.expression += 'log('
        self.display.insert(END, 'ln(')
    
    def sqrt(self):
        self.expression += 'sqrt('
        self.display.insert(END, 'sqrt(')
     
    def pi(self):
        try:
            if int(self.expression[-1]) in range(10):
                self.expression += '*pi'
        except:
            self.expression += 'pi'
        self.display.insert(END, 'pi')
     
    def e(self):
        try:
            if int(self.expression[-1]) in range(10):
                self.expression += '*e'
        except:
            self.expression += 'e'
        self.display.insert(END, 'e')
         
    def sin_inverse(self):
        self.expression += 'asin('
        self.display.insert(END, 'arcsin(')      
        
    def cos_inverse(self):
        self.expression += 'acos('
        self.display.insert(END, 'arccos(')
        
    def tan_inverse(self):
        self.expression += 'atan('
        self.display.insert(END, 'arctan(')
    
    def left_bracket(self):
        self.expression += '('
        self.display.insert(END, '(')
        
    def right_bracket(self):
        self.expression += ')'
        self.display.insert(END, ')')
    
    def sin(self):
        self.expression += 'sin('
        self.display.insert(END, 'sin(')   
    
    def cos(self):
        self.expression += 'cos('
        self.display.insert(END, 'cos(')   
    
    def tan(self):
        self.expression += 'tan('
        self.display.insert(END, 'tan(')
        
    def delete(self):
        self.expression = str(self.expression)[: -1]        
        current_string = self.display.get(1.0, END)
        column_index = len(current_string) - 2
        index_to_delete = float('1.'+ str(column_index))
        self.display.delete(index_to_delete)
        
    def ac(self):
        self.stored_value = eval(self.expression)
        self.expression = ''
        self.display.delete(0.0, END)
            
    def times(self):
        self.expression += '*'
        self.display.insert(END, 'x')
        
    def divide(self):
        self.expression += '/'
        self.display.insert(END, '/')
        
    def plus(self):
        self.expression += '+'
        self.display.insert(END, '+')
    
    def minus(self):
        self.expression += ' - '
        self.display.insert(END, '-')
        
    def decimal(self):
        self.expression += '.'   
        self.display.insert(END, '.')   
    
    def clear(self):
        self.expression = ''
        self.display.delete(1.0, END)
          
    def ans(self):
        self.expression += str(self.stored_value)
        self.display.insert(END, 'Ans')
          
    def equals(self):
        print(self.expression)
        print(eval(self.expression))
        result = str(eval(self.expression))   
        self.display.delete(0.0, END)    
        self.display.insert(END, result)
        self.expression = result           
        
root = Tk()
main = Calculator(root)
root.mainloop()
        