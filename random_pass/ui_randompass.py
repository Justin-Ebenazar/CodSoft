#new update
from tkinter import*
from tkinter import ttk as tko
import random
from tkinter import messagebox

levels=['EASY','MEDIUM','HARD']

win=Tk()
win.geometry('700x400')
win.wm_title("Random password generator")

main_frame=Frame(win,height=399,width=700)                              #main frame
main_frame.pack(expand='True')

frame1=Frame(main_frame,height=133,width=700,bg='pink')                        # password length specifier
frame1.pack()
frame1.pack_propagate(0)

size=Label(frame1,text="Enter length(max limit 25) :",font=('times new roman',20),bg='pink')               
size.pack(side='left',expand='True')

size_enter=Entry(frame1,font=('times new roman',20))
size_enter.pack(side='left',expand='True')
size_enter.focus_set()

frame2=Frame(main_frame,height=133,width=700,bg='pink')                  # difficulty level choser
frame2.pack()
frame2.pack_propagate(0)

size=Label(frame2,text="Choose password difficulty :",font=('times new roman',20),bg='pink')               
size.pack(side='left',expand='True')

select_lev=StringVar(frame2)  
select_lev.set(levels[2])
list_op=tko.Combobox(frame2,state='readonly',font=('calibri',15,'bold'),textvariable=select_lev,values=levels)
list_op.pack(side='left',expand='True')


frame3=Frame(main_frame,height=133,width=700,bg='pink')             #pass generator
frame3.pack()
frame3.pack_propagate(0)

gen_password=Label(frame3,text='                                    ',font=('times new roman',25,'bold'),bg='black',fg='white')
password=''
def pass_gen(difficulty,pass_len):
    global password
    password=''
    alpha=[chr(i) for i in list(range(65,91))+list(range(97,123))]
    num=list(map(str,list(range(10))))
    sym=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    sym.sort()

    if(difficulty=='EASY'):
        for i in range(pass_len):
            password+=random.choice(alpha)
        gen_password.configure(text=password)
    elif(difficulty=='MEDIUM'):
        for i in range(pass_len):
            password+=random.choice(alpha+num)
        if(any(i.isnumeric() for i in password)):
            print(password)
        else:
            rem=random.randint(2,pass_len-1)
            ku=list(password)
            for i in range(rem):
                ku[random.choice(list(range(pass_len)))]=random.choice(num)
            gen_password.configure(password:=''.join(ku))
    else:
        for i in range(pass_len):
            li=random.choice([alpha,num,sym,alpha,alpha,alpha,num,sym,num,num,sym,sym,alpha,num,sym,alpha,num,sym])
            password+=random.choice(li)
        gen_password.configure(text=password)
    
def pass_parser(event):                                                             #exception handling for invalid length
    if((size_enter.get()).isdigit() and int(size_enter.get())<=25):
        pass_gen(list_op.get(),int(size_enter.get()))
    else:
       messagebox.showinfo('Warning !','Kindly enter a valid password length') 

gen=Button(frame3,text='Generate',font=('times new roman',15),command=lambda:pass_parser('<Return>'),bg='lightblue') # generate button
gen.pack(side='top',pady=15)    

gen_password.pack(side='left',expand="True")

copy=Button(frame3,text='Copy',font=('times new roman',15),bg='lightgreen',fg='white',command=lambda:win.clipboard_append(password))
copy.pack(side='right',padx=40)         #copy button

win.bind('<Return>',pass_parser)

win.mainloop()
