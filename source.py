from tkinter import *
from tkinter import messagebox

import random
timeleft=60
def timer():
    global timeleft,i
    if timeleft>0:
        timeleft -= 1
        time_countlabel.config(text=timeleft)
        time_countlabel.after(1000, timer)
    else:
        wordEntry.config(state=DISABLED)
        result=correct_word-wrong_word
        instructionlabel.config(text=f'         Correct Words {correct_word}\n         Wrong Words {wrong_word}\n         Final Score {result}')
        if result<10:
            emoji1Label.config(image=poorpic)
            emoji2Label.config(image=poorpic)
        if result>10:
            emoji1Label.config(image=happypic)
            emoji2Label.config(image=happypic)
        if result>15:
            emoji1Label.config(image=propic)
            emoji2Label.config(image=propic)
        res=messagebox.askyesno('Confirm','Do you want to play again?')
        if res:
            i=0
            timeleft=60
            countlabel.config(text='0')
            time_countlabel.config(text='60')
            wordEntry.config(state=NORMAL)
            instructionlabel.config(text='Type The Word & Hit Enter')
            emoji1Label.config(image='')
            emoji2Label.config(image='')

correct_word=0
wrong_word=0
i=0
def play_game(event):
    if wordEntry.get()!='':
        global i, correct_word, wrong_word
        i += 1
        countlabel.config(text=i)
        instructionlabel.config(text='')
        if timeleft == 60:
            timer()

        if wordEntry.get() == word_list_Label['text']:
            correct_word += 1
        else:
            wrong_word += 1

        random.shuffle(word_list)
        word_list_Label.config(text=word_list[0])
        wordEntry.delete(0, END)

word_list=['regulator', 'design', 'object', 'ink', 'aid', 'bad', 'cat', 'software', 'dog', 'book','speed',
          'game','eat','God', 'hat', 'jug','technology', 'kit', 'let', 'may', 'net', 'pet', 'engineering']

#Functionality Part
slidewords=''
count=0
def slider():
    global slidewords,count
    text='Welcome To Typing Speed Game!'
    if count>=len(text):
        count=0
        slidewords=''
    slidewords=slidewords+text[count]#W
    movingLabel.config(text=slidewords)
    count+=1
    movingLabel.after(250,slider)

#GUI Part
root = Tk()
root.title('Typing Speed Game')
root.wm_iconbitmap('icon.ico')
root.geometry('700x600+420+100')
root.config(bg='RosyBrown2')
root.resizable(0,0)

logoImage=PhotoImage(file='stopwatch.png')
logoLabel=Label(root,image=logoImage,bg='RosyBrown2')
logoLabel.place(x=220,y=55)

movingLabel=Label(root,text='Welcome To Typing Speed Game!',bg='RosyBrown2',font=('times new roman',25,'bold italic'),
                  width=42,fg='red')
movingLabel.place(x=-45,y=10)
slider()
random.shuffle(word_list)
word_list_Label=Label(root,text=word_list[0],font=('bookman old style',40,'italic bold'),bg='RosyBrown2')
word_list_Label.place(x=350,y=350,anchor=CENTER)

wordlabel=Label(root, text='Words',font=('Castellar',28,'bold'),bg='RosyBrown2')
wordlabel.place(x=30,y=150)

countlabel=Label(root, text='0',font=('Castellar',28,'bold'),bg='RosyBrown2',fg='green')
countlabel.place(x=95,y=200)

timelabel=Label(root, text='Timer',font=('Castellar',28,'bold'),bg='RosyBrown2')
timelabel.place(x=520,y=150)

time_countlabel=Label(root, text='60',font=('Castellar',28,'bold'),bg='RosyBrown2',fg='red')
time_countlabel.place(x=562,y=200)

wordEntry=Entry(root,font=('times new roman',25,'bold'),bd=5,justify=CENTER)
wordEntry.place(x=175,y=390)
wordEntry.focus_set()

instructionlabel=Label(root, text='Type The Word & Hit Enter',font=('times new roman',20,'bold'),bg='RosyBrown2',fg='red')
instructionlabel.place(x=182,y=460)

poorpic=PhotoImage(file='sad.png')
happypic=PhotoImage(file='happy.png')
propic=PhotoImage(file='pro.png')

emoji1Label=Label(root,bg='RosyBrown2')
emoji1Label.place(x=80,y=470)
emoji2Label=Label(root,bg='RosyBrown2')
emoji2Label.place(x=550,y=470)

root.bind('<Return>',play_game)
root.mainloop()

