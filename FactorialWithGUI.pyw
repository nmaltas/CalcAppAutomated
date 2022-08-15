from pywinauto import Desktop, Application
import pyautogui
import time
from tkinter import *
import tkinter.font as TkFont
import threading

class Factorial:
    def __init__(self, win):
    
        global Active
        Active = False
        
        global a
        a = 0
        
        self.default_font = TkFont.nametofont("TkDefaultFont")
        self.default_font.configure(size=16, family = "Comic Sans MS")
        
        #Daemon process
        Back = threading.Thread(name = 'Back', target = self.CalcCalc, daemon = True)
        Back.start()
        
        
        self.InputHere = Label(win, text = "Provide a number", fg = "#00FF40", bg = "black")
        self.Number = Entry( width = 5, bg = "#00FF40")
        
        self.InputHere.place(x = 35, y = 5)
        self.Number.place(x = 105, y = 53)

        # Run button
        self.RunMe = Button(win, text = "Ready", command = self.ToggleState, fg = "black", bg = "#00FF40", activebackground = "#FF6600", height = 1, width = 15)
        self.RunMe.place( x = 20, y = 120)

    def ToggleState(self):
        global Active
        global a
        a = 0
        Active = not Active
        if (Active == True):
            try:
                a = int(self.Number.get())
                if (a < 0):
                    a = 0
                    return
            except:
                return
            
            self.Number.config(state= "disabled", disabledbackground = "#FF6600")
            self.InputHere.config(fg = "#FF6600")
            DisabledText = "Calculating " + str(a) + "!"
            self.RunMe.config(text = DisabledText, activebackground = "#00FF40", bg = "#FF6600", state = "disabled")
        else:
            self.Number.config(state= "normal")
            self.InputHere.config(fg = "#00FF40")
            self.RunMe.config(text = "Ready", bg = "#00FF40", activebackground = "#FF6600", state = "normal")
    
    def CalcCalc(self):
        global Active
        global a
        
        while (True):
            
            if ( (Active == True) and (a != 0) ):
                
                Tzatziki = Application().start('Calc.exe ')
                TzatzikiTzatziki = Desktop(backend = "uia").Calculator

                while ( True) :
                    b = str(a)
                    a = a - 1
                    TzatzikiTzatziki.type_keys(b)
    
                    if (a <=0) :
                        TzatzikiTzatziki.type_keys('=')
                        break
                    else:
                        TzatzikiTzatziki.type_keys('*')
                
                self.ToggleState()
            else :
                continue

    

App=Tk()
Mpougiournti= Factorial(App)
App.configure( bg = "black")
App.title('Factorial')
App.geometry("250x200+500+200")
App.mainloop()
