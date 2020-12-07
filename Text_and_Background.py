import Tkinter
import csv
import random


r = lambda: random.randint(0,255)


main=Tkinter.Tk()

text = Tkinter.Label(main, text="Text")
text.pack()

def refresh():
    tcolor=('#%02X%02X%02X' % (r(),r(),r()))
    bcolor=('#%02X%02X%02X' % (r(),r(),r()))
    main.configure(bg=bcolor) 
    text.configure(bg=bcolor) 
    text.configure(fg=tcolor) 
    T.configure(text="Text: "+tcolor)
    BG.configure(text="Background: "+bcolor)



def good():
    print "good"
    refresh()


def bad():
    print "bad"

#G = Tkinter.Button(main, text ="Good", command = good).pack()
#B = Tkinter.Button(main, text ="Bad", command = bad).pack()
R = Tkinter.Button(main, text ="Refresh", command = refresh).pack()

BG = Tkinter.Label(main, text="Background Color")
BG.pack()


T = Tkinter.Label(main, text="Text Color")
T.pack()

main.mainloop()