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
        
        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        #we call this after all because the it's a dynamic window so fits is't important to put the
        #widgets inside and then with the size center the window
        self._center_window()
    

    def main(self):
        #this is a infinite loop that help us to show the GUI because finish when we close the form
        self.mainloop()
        
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
        
    #in python we don't have private methods so when we put one underscore means that this method is only use it inside of the class
    def _make_entry(self):
        ent = ttk.Entry(self.main_frm, justify='right', textvariable = self.value_var,
        state='disabled')
        ent.pack(fill='x')
    
    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()
        
        frm = ttk.Frame(outer_frm)
        frm.pack()
        
        button_in_row = 0
        
        for caption in self.button_captions:
            if button_in_row == self.MAX_BUTTONS_PER_ROW:
                frm = ttk.Frame(outer_frm)
                frm.pack()
                
                button_in_row = 0
                
            btn = ttk.Button(
                frm,text=caption, 
                command=(lambda button=caption: self.controller.on_button_click(button))
                )
            btn.pack(side='left')
            
            button_in_row += 1
            
            
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
        
            
        