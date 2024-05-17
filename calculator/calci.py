from tkinter import*
from tkinter import ttk

win=Tk()
win.geometry('300x420')
win.title('Calculator')

bx=Label(win,text='',font=('calibri',30))           # equation input indicator label
bx.place(x=280,y=50,anchor='e')

stex=Label(win,text='0',font=('calibri',15),fg='grey')      # answer indicator label
stex.place(x=280,y=20,anchor='e')

eq=''
ans=123

def resizeimage(img, newWidth, newHeight):          # resize function for images
        oldWidth = img.width()
        oldHeight = img.height()
        newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
        for x in range(newWidth):
            for y in range(newHeight):
                xOld = int(x*oldWidth/newWidth)
                yOld = int(y*oldHeight/newHeight)
                rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
                newPhotoImage.put(rgb, (x, y))
        return newPhotoImage


def func(a):                    # function used for backspace button
    global eq,stex
    if(a=='b' and eq!=''):
        eq=eq[:len(eq)-1]
    elif(a=='b'):
        pass
    else:
        eq+=str(a)
    stex.configure(text=eq)
    stex.place(x=280,y=20,anchor='e')

def canc():                 # function used for cancel button
    global eq
    eq=''
    stex.configure(text='0')
    stex.place(x=280,y=20,anchor='e')
    bx.configure(text='')
    bx.place(x=280,y=50,anchor='e')

def equal():                    # function used for equal , which evaluates the answer
    global ans,eq
    try:
        ans=eval(eq)
        if(isinstance(ans,float)):          # if the answer is float , it rounds it off to 7 decimals
            ans=round(ans,7)
        bx.configure(text=str(ans))
        bx.place(x=280,y=50,anchor='e')
    except:                                    # exception handles if the equation is not a valid one 
        if(eq==''):
            bx.configure(text='')
            bx.place(x=280,y=50,anchor='e')
            return
        bx.configure(text='Invalid equation')
        bx.place(x=280,y=50,anchor='e')
    eq=''
    
n1=PhotoImage(file = r"zero.png")               # images for the calculator buttons...
n2=PhotoImage(file = r"two.png")
n3=PhotoImage(file = r"three.png")
n4=PhotoImage(file = r"four.png")
n5=PhotoImage(file = r"five.png")
n6=PhotoImage(file = r"six.png")
n7=PhotoImage(file = r"seven.png")
n8=PhotoImage(file = r"eight.png")
n9=PhotoImage(file = r"nine.png")
n0=PhotoImage(file = r"one.png")
nb=PhotoImage(file = r"backs.png")
nc=PhotoImage(file = r"canac.png")
nlb=PhotoImage(file = r"lefb.png")
nrb=PhotoImage(file = r"rigb.png")
n00=PhotoImage(file = r"doubze.png")

npl=PhotoImage(file = r"plus.png")
nmi=PhotoImage(file = r"minus.png")
nin=PhotoImage(file = r"into.png")
ndiv=PhotoImage(file = r"div.png")
neq=PhotoImage(file = r"equal.png")
nflo=PhotoImage(file = r"flo.png")

imone=resizeimage(n1,70,62)                 # resizing the images for to fit the right size of buttons 
imtwo=resizeimage(n2,70,62)
imthree=resizeimage(n3,70,62)
imfour=resizeimage(n4,70,62)
imfive=resizeimage(n5,70,62)
imsix=resizeimage(n6,70,62)
imseven=resizeimage(n7,70,62)
imeight=resizeimage(n8,70,62)
imnine=resizeimage(n9,70,62)
imzero=resizeimage(n0,70,62)
imdz=resizeimage(n00,70,62)

imbacks=resizeimage(nb,70,62)
imcancu=resizeimage(nc,70,62)
imlb=resizeimage(nlb,40,62)
imrb=resizeimage(nrb,40,62)

imequa=resizeimage(neq,70,62)
imflo=resizeimage(nflo,70,62)
implu=resizeimage(npl,70,62)
immin=resizeimage(nmi,70,62)
imdiv=resizeimage(ndiv,70,62)
immul=resizeimage(nin,70,62)

one=Button(win,image=imone,command=lambda:func(1))          # creating buttons and assiginig the regarding images to it
two=Button(win,image=imtwo,command=lambda:func(2))
three=Button(win,image=imthree,command=lambda:func(3))
four=Button(win,image=imfour,command=lambda:func(4))
five=Button(win,image=imfive,command=lambda:func(5))
six=Button(win,image=imsix,command=lambda:func(6))
seven=Button(win,image=imseven,command=lambda:func(7))
eight=Button(win,image=imeight,command=lambda:func(8))
nine=Button(win,image=imnine,command=lambda:func(9))
zero=Button(win,image=imzero,command=lambda:func(0))
doublezero=Button(win,image=imdz,command=lambda:func('00'))
point=Button(win,image=imflo,command=lambda:func('.'))

equa=Button(win,image=imequa,command=equal)
cancel=Button(win,image=imcancu,command=canc)

minus=Button(win,image=immin,command=lambda:func('-'))
plus=Button(win,image=implu,command=lambda:func('+'))
multi=Button(win,image=immul,command=lambda:func('*'))
div=Button(win,image=imdiv,command=lambda:func('/'))
backsp=Button(win,image=imbacks,command=lambda:func('b'))

lefb=Button(win,image=imlb,command=lambda:func('('))
rigb=Button(win,image=imrb,command=lambda:func(')'))

one.place(x=0,y=287)
two.place(x=75,y=287)
three.place(x=150,y=287)

four.place(x=0,y=219)
five.place(x=75,y=219)
six.place(x=150,y=219)

seven.place(x=0,y=151)
eight.place(x=75,y=151)
nine.place(x=150,y=151)

doublezero.place(x=0,y=355)
zero.place(x=75,y=355)
point.place(x=150,y=355)

minus.place(x=225,y=219)
plus.place(x=225,y=287)
multi.place(x=225,y=151)
div.place(x=225,y=83)

backsp.place(x=149,y=83)
cancel.place(x=0,y=83)
equa.place(x=225,y=355)

lefb.place(x=73,y=83)
rigb.place(x=106,y=83)

win.mainloop()
