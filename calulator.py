from tkinter import *

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
    
def btnClear():
    global operator
    operator=" "
    text_Input.set(" ")    

def btnEquals():
    try:
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup) 
        operator=" "      
    except:
        text_Input.set("ERROR!!!")
        operator = ""
    

cal= Tk()
cal.title("Calculator")
operator=" "
text_Input= StringVar()


txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable= text_Input, bd=30, insertwidth=3, 
                   bg="white",justify='right').grid(columnspan=4)

button7= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="7", 
               command= lambda:btnclick(7))
button7.grid(row=1,column=0)

button8= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="8", 
               command= lambda:btnclick(8))
button8.grid(row=1,column=1)

button9= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="9", 
               command= lambda:btnclick(9))
button9.grid(row=1,column=2)

buttonAdd= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="+", 
               command= lambda:btnclick("+"))
buttonAdd.grid(row=1,column=3)

button4= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="4", 
               command= lambda:btnclick(4))
button4.grid(row=2,column=0)

button5= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="5", 
               command= lambda:btnclick(5))
button5.grid(row=2,column=1)

button6= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="6", 
               command= lambda:btnclick(6))
button6.grid(row=2,column=2)

buttonSub= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="-", 
               command= lambda:btnclick("-"))
buttonSub.grid(row=2,column=3)

button1= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="1", 
               command= lambda:btnclick(1))
button1.grid(row=3,column=0)

button2= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="2", 
               command= lambda:btnclick(2))
button2.grid(row=3,column=1)

button3= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="3", 
               command= lambda:btnclick(3))
button3.grid(row=3,column=2)

buttonMul= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="*", 
               command= lambda:btnclick("*"))
buttonMul.grid(row=3,column=3)

buttonClr= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="C", 
               command = btnClear)
buttonClr.grid(row=4,column=0)

button0= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="0", 
               command= lambda:btnclick(0))
button0.grid(row=4,column=1)

buttonEqu= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="=", 
               command= btnEquals)
buttonEqu.grid(row=4,column=2)

buttonDiv= Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="/", 
               command= lambda:btnclick("/"))
buttonDiv.grid(row=4,column=3)


cal.mainloop()
