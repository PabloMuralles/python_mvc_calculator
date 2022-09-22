'''
Created on Jul 31, 2022

@author: pablo
'''



class Model:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.previous_value = ''
        self.value = ''
        self.operator = ''
        
        
    def calculate(self,caption):
        
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''
            
        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
            
        elif caption == '%':
            pass
        
        elif caption == '=':
            self.value = str(self._evaluate())
        
        elif caption == '.':
            if not caption in self.value:
                self.value += '.'
            
        elif isinstance(caption, int):##this instance help us to validate if the caption is an int
            self.value += str(caption)
        
        else:
            if self.value:
                #if instance (self.previous_value, int):
                self.operator = caption
                
                self.previous_value = self.value
                
                self.value = ''
            
        
        return self.value
    
    def _evaluate(self):
        ##eval is't a function of python
        return eval(self.previous_value+self.operator+self.value)
    
        