from tkinter import*
from tkinter import messagebox
import random
from tkinter import ttk as tko

no_of_round=[3,4,5,6,7,8,9,10]
rounds=3

user=0
comp=0

win=Tk()
win.geometry('700x500')
win.title('Rock,paper and Scissor')

main_frame=Frame(win,bg='grey',height=500,width=700)
main_frame.pack(fill='both',expand='True')

selection=StringVar()
backim=PhotoImage(file=r"back.png")         # back button image
backim2=backim.subsample(16,16)

def game_play(rounds):
    
    # the blue frame containing game elements
    rps=Frame(main_frame,bg='lightblue',height=450,width=650)
    rps.pack(side='top',expand='True')
    rps.pack_propagate(0)

    uptab=Frame(rps,height=50,width=650,bg='lightblue')                   # upper frame for the back button
    uptab.pack(side='top')
    uptab.pack_propagate(0)

    def play():
        rps.pack_forget()
        global user,comp
        user,comp=0,0
        round_choser()

    backbutton=Button(uptab,image=backim2,command=play)          #backbutton 
    backbutton.pack(side='left',padx=5)

    scoretab=Frame(rps,height=50,width=650,bg='pink')             # tab containing score of user and computer
    scoretab.pack()
    scoretab.pack_propagate(0)

    user_score=Label(scoretab,text='User : ',font=('times new roman',15),bg='pink')
    user_score.pack(side='left',expand="True")

    use_score=Label(scoretab,text=user,font=('times new roman',15),bg='pink')
    use_score.pack(side='left',expand="True")

    com_score=Label(scoretab,text=comp,font=('times new roman',15),bg='pink')

    comp_score=Label(scoretab,text='Computer : ',font=('times new roman',15),bg='pink')
    comp_score.pack(side='left',expand="True")
    com_score.pack(side='left',expand="True")

    gametab=Frame(rps,height=350,width=650)              #frame containing game elements
    gametab.pack()
    gametab.pack_propagate(0)

    match_area=Frame(gametab,height=150,width=650,bg='pink')        # inner frame of game tab that defines the match between user and computer 
    match_area.pack()
    match_area.pack_propagate(0)

    user_area=Frame(gametab,height=150,width=650,bg='pink')    # list of options to chose from , by the user

    user_area.pack_propagate(0)

    #match area buttons

    user_choice=Label(match_area)
    comp_choice=Label(match_area)
    indi_comp=Label(match_area,text="Computer ->",font=('Times new roman',20))
    indi_user=Label(match_area,text="<- User choice",font=('Times new roman',20))

    indi_comp.pack(side='left',expand='True')
    comp_choice.pack(side='left',expand='True')
    user_choice.pack(side='left',expand='True')
    indi_user.pack(side='left',expand='True')

    #image files

    rock_im=PhotoImage(file=r"rock.png")
    paper_im=PhotoImage(file=r"paper.png")
    scissor_im=PhotoImage(file=r"scissor.png")

    rock_im=rock_im.subsample(15,10)
    paper_im=paper_im.subsample(7,7)
    scissor_im=scissor_im.subsample(10,8)

    #winning announcer

    winframe=Frame(gametab,height=60,width=650,bg='pink')
    winframe.pack()
    winframe.pack_propagate(0)
    user_area.pack()

    result=Label(winframe,text="Let's Begin !",font=('brush script mt',20),bg='lightgreen')

    ops=[rock_im,paper_im,rock_im,rock_im,paper_im,rock_im,paper_im,rock_im,paper_im,scissor_im,scissor_im,scissor_im,paper_im,scissor_im,scissor_im]
    op1=['s','r','p']
    op2=['r','p','s']
    op3=['p','s','r']

    breaker=0

    def checker(comp1,user1):
        nonlocal breaker
        breaker+=1
        m=comp1
        n=user1
        global user,comp
        if(m=='r'):
            if(op1.index(m)>op1.index(n)):
                result.configure(text="Computer won")
                comp+=1
                com_score.configure(text=comp)
            elif(m==n):
                result.configure(text="It's a tie")
            else:
                result.configure(text="You won !")
                user+=1
                use_score.configure(text=user)
        elif(m=='p'):
            if(op2.index(m)>op2.index(n)):
                result.configure(text="Computer won")
                comp+=1
                com_score.configure(text=comp)
            elif(m==n):
                result.configure(text="It's a tie")
            else:
                result.configure(text="You won !")
                user+=1
                use_score.configure(text=user)
        else:
            if(op3.index(m)>op3.index(n)):
                result.configure(text="Computer won")
                comp+=1
                com_score.configure(text=comp)
            elif(m==n):
                result.configure(text="It's a tie")
            else:
                result.configure(text="You won !")
                user+=1
                use_score.configure(text=user)
        if(breaker==int(rounds)):
            rbutton.configure(state=DISABLED)
            sbutton.configure(state=DISABLED)
            pbutton.configure(state=DISABLED)
            if(user>comp):
                result.configure(text='Congratulations ! You have won ')
            elif(user==comp):
                result.configure(text='It\'s a draw !')
            else:
                result.configure(text='Oops, It seems I won ..Better luck next time ! ')
            def oknot():
                playagain=messagebox.askyesno('Play again','Do you want to play again?')
                if(playagain):
                    rps.pack_forget()
                    global user,comp
                    user,comp=0,0
                    round_choser()
                else:
                    win.destroy()
            ok=Button(winframe,text='okay',font=('calibri',15),command=oknot)
            ok.pack(side='left',padx=10,expand='True')
                
    def choice_fixer(choice,c):
        m=random.choice(ops)
        comp_choice.configure(image=m)
        user_choice.configure(image=choice)
        if(m==rock_im):
            checker('r',c)
        elif(m==paper_im):
            checker('p',c)
        else:
            checker('s',c)


    #user selection area

    rbutton=Button(user_area,image=rock_im,command=lambda:choice_fixer(rock_im,'r'))
    rbutton.pack(side='left',expand='True')

    pbutton=Button(user_area,image=paper_im,command=lambda:choice_fixer(paper_im,'p'))
    pbutton.pack(side='left',expand='True')

    sbutton=Button(user_area,image=scissor_im,command=lambda:choice_fixer(scissor_im,'s'))
    sbutton.pack(side='left',expand='True')

    result.pack(expand="True",side='left')

    

def round_choser():
    global selection

    first_frame=Frame(main_frame,bg='lightblue',height=450,width=650)
    first_frame.pack(fill='both',expand='True',padx=25,pady=25)             # the blue frame containing all the contents before game

    inframe=Frame(first_frame,height=500,bg='pink')
    inframe.pack(expand='True',side='top')              # the frame that contains widget 1 and 2+3

    mark=Label(inframe,text='Select the number of rounds ',bg='pink',font=('Times new roman',20))        # label widget
    mark.pack(side='top',expand='True',pady=5)

    texframe=Frame(inframe)
    texframe.pack(expand='True',side='top',pady=20)                             # frame that contains 2+3

    selection.set(3)

    list_op=tko.Combobox(texframe,state='readonly',font=('calibri',20),textvariable=selection,values=no_of_round)
    list_op.pack(side='left',expand='True',padx=5)

    def roundgetter():
        global rounds
        rounds=list_op.get()
        first_frame.pack_forget()
        game_play(rounds)

    okbut=Button(texframe,text='Confirm',font=('calibri',20),command=lambda:roundgetter())               #confirm button
    okbut.pack()



round_choser()

win.mainloop()
