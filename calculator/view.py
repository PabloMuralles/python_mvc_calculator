'''
Created on Jul 31, 2022

@author: pablo
'''

import tkinter as tk
from tkinter import ttk
 
 




class View(tk.Tk):
    '''
    classdocs
    '''

    PAD = 10
    
    MAX_BUTTONS_PER_ROW = 4
    
    button_captions = [
        'C','+/-','%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',     
        0, '.', '='    
        ]

    def __init__(self, controller):
        '''
        Constructor
        '''
        #super is the tool that help us to initialize the class that we are initialize the inheriting class
        super().__init__()
        
        self.controller = controller
        
        self.value_var = tk.StringVar()
        
        self.title("PyCalc1.0")
        
        self.config(bg='black')
        
        self._configure_button_styles()
        
        self._make_main_frame()
        self._make_label()
        self._make_buttons()
        #we call this after all because the it's a dynamic window so fits is't important to put the
        #widgets inside and then with the size center the window
        self._center_window()
        
    def _configure_button_styles(self):
        style = ttk.Style()
        
        style.theme_use('alt')
        
        #style for number buttons
        style.configure(
            'N.TButton', foreground='white', background='gray'
            )
        
        #style for operator buttons
        style.configure(
            'O.TButton', foreground='white', background='orange'
            )
        
        #style for miscellaneos buttons
        style.configure(
            'M.TButtons', background='white'
            )
        
    def main(self):
        #this is a infinite loop that help us to show the GUI because finish when we close the form
        self.mainloop()
        
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
        
    #in python we don't have private methods so when we put one underscore means that this method is only use it inside of the class
    def _make_label(self):
        #we change the ttk for tk label becuase it's one label so don't have much sense to create a style for one label
        #if we have more than two labels have much sense so in this case it's more easy
        lbl = tk.Label(self.main_frm, anchor='e', textvariable=self.value_var, bg='black', fg='white', font=('Arial', 30))
        lbl.pack(fill='x')
    
    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()
        
        is_firt_row = True
        
        button_in_row = 0
        
        for caption in self.button_captions:
            if is_firt_row == True or button_in_row == self.MAX_BUTTONS_PER_ROW:
                is_firt_row = False
                
                frm = ttk.Frame(outer_frm)
                frm.pack(fil='x')
                
                button_in_row = 0
                
            if isinstance(caption, int):
                style_prefix = 'N'
            elif self._is_operator(caption):
                style_prefix = 'O'
            else:
                style_prefix = 'M'
                
            style_name = f'{style_prefix}.TButton'
                
            btn = ttk.Button(
                frm,text=caption, 
                command=(lambda button=caption: self.controller.on_button_click(button)),
                style=style_name
                )
            
            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'none'
                expand = 0
            
            btn.pack(fill=fill, expand=expand, side='left')
            
            button_in_row += 1
            
    
    def _is_operator(self, button_caption):
        return button_caption in ['/', '*', '-', '+' , '=']
            
            
    def _center_window(self):
        #with tk the width and height for default are 1 and when we put widgets this two don't update so 
        #we need to call this method
        self.update()
        #this method it's for tk
        width = self.winfo_width()
        height = self.winfo_height()
        
        #we need a int because the method geometry only accept an int
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        
        #this method not accept * only x
        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
            )
        
            
        