from tkinter import *

class Caculator:
    def __init__(self,window):
        self.window=window
        self.operator=''
        self.value=StringVar()
        self.window.title('Calculator')

        self.ent_display=Entry(self.window,textvariable=self.value,bd=30,fg='white',bg='green',
                               font=('arial',14,'bold'),justify=RIGHT)
        self.ent_display.grid(columnspan=4)

        #==========Buttons of row 1
        self.btn9=Button(self.window,text='9',font=('arial',14,'bold'),bd=14,command=lambda:self.btn_click(9))
        self.btn9.grid(row=1,column=0)

        self.btn8 = Button(self.window, text='8', font=('arial', 14, 'bold'),bd=14,command=lambda:self.btn_click(8))
        self.btn8.grid(row=1, column=1)

        self.btn7 = Button(self.window, text='7', font=('arial', 14, 'bold'),bd=14,command=lambda:self.btn_click(7))
        self.btn7.grid(row=1, column=2)

        self.btn6 = Button(self.window, text='6', font=('arial', 14, 'bold'),bd=14,command=lambda:self.btn_click(6))
        self.btn6.grid(row=1, column=3)

        # =======buttons of row 2
        self.btn5 = Button(self.window, text='5', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click(5))
        self.btn5.grid(row=2, column=0)

        self.btn4 = Button(self.window, text='4', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click(4))
        self.btn4.grid(row=2, column=1)

        self.btn3 = Button(self.window, text='3', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click(3))
        self.btn3.grid(row=2, column=2)

        self.btn2 = Button(self.window, text='2', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click(2))
        self.btn2.grid(row=2, column=3)

        #=========Buttons for row=3
        self.btn1 = Button(self.window, text='1', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click(1))
        self.btn1.grid(row=3, column=0)

        self.btn0 = Button(self.window, text='0', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click(0))
        self.btn0.grid(row=3, column=1)

        self.btn_add = Button(self.window, text='+', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click('+'))
        self.btn_add.grid(row=3, column=2)

        self.btn_sub = Button(self.window, text='-', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click('-'))
        self.btn_sub.grid(row=3, column=3)

        #=======Buttons for row 4
        self.btn_mul = Button(self.window, text='*', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click('*'))
        self.btn_mul.grid(row=4, column=0)

        self.btn_div = Button(self.window, text='/', font=('arial', 14, 'bold'), bd=14,command=lambda:self.btn_click('/'))
        self.btn_div.grid(row=4, column=1)

        self.btn_del = Button(self.window, text='D', font=('arial', 14, 'bold'), bd=14)
        self.btn_del.grid(row=4, column=2)

        self.btn_clr = Button(self.window, text='C', font=('arial', 14, 'bold'), bd=14,command=self.clear)
        self.btn_clr.grid(row=4, column=3)

        #=========eql button
        self.btneq = Button(self.window, text='=', font=('arial', 14, 'bold'), bd=14,command=self.btn_eq_click)
        self.btneq.grid(row=5,columnspan=4)

    def btn_click(self,number):
        self.operator=self.operator+str(number)
        self.value.set(self.operator)

    def btn_eq_click(self):
        ans=str(eval(self.operator))
        print(ans)
        self.operator=''
        self.value.set(ans)
    def clear(self):
        self.value.set('')




wn=Tk()
c=Caculator(wn)
wn.mainloop()
