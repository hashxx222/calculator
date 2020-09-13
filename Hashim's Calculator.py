from tkinter import *
  
cal = Tk()
cal.title("Calculator")
operator=""
 

display = Entry(cal,font=('arial', 20, 'bold'), insertwidth=4, bd = 30, bg='white',
                justify='right',) 
display.grid(columnspan=4)

def button_click(number):
    hashim = display.get()
    display.delete(0, END)
    display.insert(0, str(hashim) + str(number))    
        
    

                    
def clear():
    display.delete(0, END)

    
def add():
    global number
    global math
    number = int(display.get())
    display.delete(0, END)
    math = "addition"

def substract():
    global number
    global math
    number = int(display.get())
    display.delete(0, END)
    math = "substract"


def multiply():
    global math
    global number
    number = int(display.get())
    display.delete(0, END)
    math = "multiplication"



def divide():
    global math
    global number
    number = int(display.get())
    display.delete(0, END)
    math = "division"

                            
    


 
    
def equal():
    num = display.get()
    display.delete(0, END)
    if math == "addition":
       display.insert(0,number + int(num))

    if math == "multiplication":
        display.insert(0,number * int(num))

    if math == "substract":
        display.insert(0,number - int(num))

    if math == "division":
        display.insert(0,number / int(num))
     
        

 
    


 
 
             

 
 
    

btn1 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='1',  command= lambda: button_click(1), bg='blue',).grid(row=1, column=0)
btn2 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='2',command=lambda: button_click(2), bg='purple').grid(row=1, column=1)
btn3 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='3',command=lambda: button_click(3), bg='green').grid(row=1, column=2)
addition = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='+',command=add, bg='yellow').grid(row=1, column=3)

#leave space between every 4 rows to not get confused though

btn4 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='4',command=lambda: button_click(4), bg='blue').grid(row=2, column=0)
btn5 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='5',command=lambda: button_click(5), bg='purple').grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='6',command=lambda: button_click(6), bg='green').grid(row=2, column=2)
Substraction = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='-', command=substract, bg='yellow').grid(row=2, column=3)


btn7 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='7',command=lambda: button_click(7), bg='blue').grid(row=3, column=0)
btn8 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='8',command=lambda: button_click(8), bg='purple').grid(row=3, column=1)
btn9 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='9',command=lambda: button_click(9), bg='green').grid(row=3, column=2)
multiplication = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='*', command=multiply, bg='yellow').grid(row=3, column=3)


btn0 = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='0', command=lambda: button_click(0), bg='blue').grid(row=4, column=0)
equal = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='=', command=equal, bg='purple').grid(row=4, column=1)
C = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='C', command=clear, bg='green').grid(row=4, column=2)
division = Button(cal, padx=16, bd=8, fg ='black', font=('arial', 20, 'bold'), text='/', command=divide, bg='yellow').grid(row=4, column=3)








                  
 


               
 
