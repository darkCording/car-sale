from tkinter import *
import tkinter as tk
from vehicalList import *
import vehicles as ve
#----------------All Vehicle functions starts--------------------#
"""
*   car functions
*   when click car in passenger window this function will appear
*   this function is using to categorize main cars with conditions
"""

def car():
    clear()
    #btnback is using to call previos function
    btnback = Button(frame,text = "back", bg = "#5352ed", fg = "#f1f2f6", font = ("Helvatical bold", 10), command = passenger)
    btnback.pack(side=TOP,anchor=NW)
    text = Label(frame, text="select your car", font=("Helvatical bold", 20), width =100,height=5,bg="#576574",fg="#f1f2f6").pack()
    text = Label(frame, text="select your car", font=("Helvatical bold", 20),bg="#576574",fg="#576574").pack()
    btn1 = Button(frame, text="ac car",font=("Helvatical bold", 12), bg="#40407a", fg="#f1f2f6",width =100,height=5, command=carAC)
    btn1.pack()
    btn2 = Button(frame, text="non ac car",font=("Helvatical bold", 12), bg="#40407a", fg="#f1f2f6",width =100,height=5, command=carnAc)
    btn2.pack()

    changeOnHover(btnback, "#34ace0", "#5352ed")
    changeOnHover(btn1, "#34ace0", "#40407a")
    changeOnHover(btn2, "#34ace0", "#40407a")
    text = Label(frame, text="developed by sandun tharaka", font=("Helvatical bold", 10), padx=155, pady=10, bg="black",fg="#00d2d3").pack(side=BOTTOM)
    return

"""
*   AC car function
*   when click ac car in car window this function will appear
*   this function is using to show main available cars
*   if customer want to rent one he can click hire vehicle
*   administrator wants to add or remove car he can do it when clicking add or remove
"""
def carAC():
    clear()
    #   all functions in queue class is assigned to A variable
    A = queue(ve.accars)
    #   queue class wanto pass one parameter of list, vehicles class has defines all list and dictionaries it is imported as ve
    B = ve.car

    btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=car)
    btnback.pack(side=TOP,anchor=NW)
    #   calling listdetailes function with parsing parameters(A and B) to get details of the queue list and equal details of dictionary.
    listDetails(A,B)

    vehiList(ve.accars)
    add_remove(A,B)

    changeOnHover(btnback, "#34ace0", "#5352ed")
    return
"""
*   None AC car function
*   when click None AC car in car window this function will appear
*   this function is using to show main available cars
*   if customer want to rent one he can click hire vehicle
*   administrator wants to add or remove car he can do it when clicking add or remove
"""
def carnAc():
    clear()

    A = queue(ve.noaccars)
    B = ve.car
    btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=car)
    btnback.pack(side=TOP,anchor=NW)
    listDetails(A,B)

    vehiList(ve.noaccars)
    add_remove(A, B)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return

"""
*   van functions
*   when click van in passenger window this function will appear
*   this function is using to categorize main vans with conditions
"""
def van():
    clear()
    btnback = Button(frame, text="back", bg = "#5352ed", fg = "#f1f2f6", font = ("Helvatical bold", 10), command=passenger)
    btnback.pack(side=TOP, anchor=NW)
    text = Label(frame, text="select your van", font=("Helvatical bold", 20), width =100,height=5,bg="#576574",fg="#f1f2f6").pack()
    text = Label(frame, text="select your van", font=("Helvatical bold", 20),bg="#576574",fg="#576574").pack()
    btn1 = Button(frame, text="ac van",font=("Helvatical bold", 12), bg="#40407a", fg="#f1f2f6",width =100,height=5, command=vanAC)
    btn1.pack()
    btn2 = Button(frame, text="none ac van",font=("Helvatical bold", 12), bg="#40407a", fg="#f1f2f6",width =100,height=5, command=vannAc)
    btn2.pack()
    changeOnHover(btnback, "#34ace0", "#5352ed")
    changeOnHover(btn1, "#34ace0", "#40407a")
    changeOnHover(btn2, "#34ace0", "#40407a")
    text = Label(frame, text="developed by sandun tharaka", font=("Helvatical bold", 10), padx=155, pady=10, bg="black",fg="#00d2d3").pack(side="bottom")
    return
"""
*   AC van function
*   when click ac van in van window this function will appear
*   this function is using to show main available vans
*   if customer want to rent one he can click hire vehicle
*   administrator wants to add or remove van he can do it when clicking add or remove
"""

def vanAC():
    clear()

    A = queue(ve.acvans)
    B = ve.van
    btnback = Button(frame,text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=van)
    btnback.pack(side=TOP, anchor=NW)
    listDetails(A,B)

    vehiList(ve.acvans)
    add_remove(A,B)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return

def vannAc():
    clear()

    A = queue(ve.noacvans)
    B = ve.van
    btnback = Button(frame,text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10), command=van)
    btnback.pack(side=TOP, anchor=NW)
    listDetails(A,B)

    vehiList(ve.noacvans)
    add_remove(A,B)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return

"""
*   threeweel functions
*   when click threeweel in passenger window this function will appear
*   this function is using to show and hire available three weels
"""
def threeweel():
    clear()
    A = queue(ve.threeWeels)
    B = ve.threeWeel
    btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10), command=passenger)
    btnback.pack(side=TOP, anchor=NW)
    listDetails(A,B)

    vehiList(ve.threeWeels)
    add_remove(A,B)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return

"""
*   truck functions
*   when click truck in commersial window this function will appear
*   this function is using to categorize main trucks with conditions
"""
def truck():
    clear()
    btnback = Button(frame, text="back",bg = "#5352ed", fg = "#f1f2f6", font = ("Helvatical bold", 10), command=carrier)
    btnback.pack(side=TOP, anchor=NW)

    text = Label(frame, text="select your truck",font=("Helvatical bold", 20), width =100,height=5,bg="#576574",fg="#f1f2f6").pack()
    text = Label(frame, text="select your truck", font=("Helvatical bold", 20),bg="#576574",fg="#576574").pack()
    btn1 = Button(frame, text="7ft truck",font=("Helvatical bold", 12), bg="#40407a", fg="#f1f2f6",width =100,height=5, command=truks7Ft)
    btn1.pack()
    btn2 = Button(frame, text="12ft truck",font=("Helvatical bold", 12), bg="#40407a", fg="#f1f2f6",width =100,height=5, command=truks12Ft)
    btn2.pack()
    changeOnHover(btnback, "#34ace0", "#5352ed")
    changeOnHover(btn1, "#34ace0", "#40407a")
    changeOnHover(btn2, "#34ace0", "#40407a")
    text = Label(frame, text="developed by sandun tharaka", font=("Helvatical bold", 10),padx=155, pady=10, bg="black",fg="#00d2d3").pack(side="bottom")
    return

"""
*   truks7Ft function
*   when click truks7Ft in car window this function will appear
*   this function is using to show main available truks 7Ft 
*   if customer want to rent one he can click hire vehicle
*   administrator wants to add or remove car he can do it when clicking add or remove
"""
def truks7Ft():

    clear()

    A = queue(ve.truks7ft)
    B = ve.truks
    btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10), command=truck)
    btnback.pack(side=TOP, anchor=NW)
    listDetails(A,B)

    vehiList(ve.truks7ft)

    add_remove(A,B)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return
"""
*   truks12Ft function
*   when click truks12Ft in car window this function will appear
*   this function is using to show main available truks 12Ft 
*   if customer want to rent one he can click hire vehicle
*   administrator wants to add or remove car he can do it when clicking add or remove
"""
def truks12Ft():
    clear()

    A = queue(ve.truks12ft)
    B = ve.truks
    btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10), command=truck)
    btnback.pack(side=TOP, anchor=NW)
    listDetails(A,B)

    vehiList(ve.truks12ft)
    add_remove(A,B)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return

"""
*   lorry functions
*   when click lorry in commercial window this function will appear
*   this function is using to categorize main lorry with conditions
"""

def lorrie():
    clear()
    btnback = Button(frame, text="back",bg = "#5352ed", fg = "#f1f2f6", font=("Helvatical bold", 10), command=carrier)
    btnback.pack(side=TOP, anchor=NW)

    text = Label(frame, text="select your lorry", font=("Helvatical bold", 20), width=100, height=5,bg="#576574",fg="#f1f2f6").pack()
    text = Label(frame, text="select your lorry", font=("Helvatical bold", 20), bg="#576574",fg="#576574").pack()

    btn1 = Button(frame, text="2500kg lorry",font=("Helvatical bold", 12), bg="#40407a", fg="#f1f2f6",width =100,height=5, command=lorrietwoFive)
    btn1.pack()
    btn2 = Button(frame, text="3500kg lorry",font=("Helvatical bold", 12), bg="#40407a", fg="#f1f2f6",width =100,height=5, command=lorrietreeFive)
    btn2.pack()
    changeOnHover(btnback, "#34ace0", "#5352ed")
    changeOnHover(btn1, "#34ace0", "#40407a")
    changeOnHover(btn2, "#34ace0", "#40407a")
    text = Label(frame, text="developed by sandun tharaka", font=("Helvatical bold", 10), padx=155, pady=10, bg="black",fg="#00d2d3").pack(side="bottom")

    return
"""
*   lorrietwoFive function
*   when click 2500kg lorry  in car window this function will appear
*   this function is using to show main available 2500kg lorries
*   if customer want to rent one he can click hire vehicle
*   administrator wants to add or remove lorry he can do it when clicking add or remove
"""

def lorrietwoFive():
    clear()

    A = queue(ve.lorrietwofive)
    B = ve.lorry
    btnback = Button(frame, text="back",bg="#5352ed", fg="white", font=("Helvatical bold", 10), command=lorrie)
    btnback.pack(side=TOP, anchor=NW)
    listDetails(A,B)

    vehiList(ve.lorrietwofive)

    add_remove(A,B)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return
"""
*   lorrietreeFive function
*   when click 3500kg lorry  in car window this function will appear
*   this function is using to show main available 3500kg lorries
*   if customer want to rent one he can click hire vehicle
*   administrator wants to add or remove lorry he can do it when clicking add or remove
"""
def lorrietreeFive():
    clear()

    A = queue(ve.lorriethreefive)
    B = ve.lorry
    btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10), command=lorrie)
    btnback.pack(side=TOP, anchor=NW)
    listDetails(A,B)

    vehiList(ve.lorriethreefive)
    add_remove(A,B)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return


"""
*   second window opens when click passenger in main window
*   this window is used to categorize main vehicles for passenger purpose
"""
def passenger():
    #clear all widgets in previous window
    clear()
    text = Label(frame, text="select your choice", font=("Helvatical bold", 20),width =100,height=5,bg="#576574",fg="#c8d6e5").pack()
    text = Label(frame, text="select your vehicle type", font=("Helvatical bold", 10), bg="#576574",fg="#576574").pack()

    btn1 = Button(frame, text="Cars", bg="#40739e", fg="#c8d6e5", width =100,height=2,font=("Helvatical bold",15),command=car)
    btn1.pack()
    btn2 = Button(frame, text="Vans", bg="#40739e", fg="#c8d6e5", width =100,height=2,font=("Helvatical bold",15),command=van)
    btn2.pack()
    btn3 = Button(frame, text="Three wheelers", bg="#40739e", fg="#c8d6e5", width =100,height=2,font=("Helvatical bold",15),command=threeweel)
    btn3.pack()

    changeOnHover(btn1, "#7f8fa6", "#40739e")
    changeOnHover(btn2, "#7f8fa6", "#40739e")
    changeOnHover(btn3, "#7f8fa6", "#40739e")

    text = Label(frame, text="developed by sandun tharaka", font=("Helvatical bold", 10), padx=155, pady=10, bg="black",fg="#00d2d3").pack(side="bottom")
    return

def carrier():
    clear()
    text = Label(frame, text="select your choice", font=("Helvatical bold", 20),width =100,height=5,bg="#576574",fg="#c8d6e5").pack()
    text = Label(frame, text="select your vehicle type", font=("Helvatical bold", 10), bg="#576574",fg="#576574").pack()
    btn1 = Button(frame, text="Truck", bg="#40739e", fg="#c8d6e5", width =100,height=2,font=("Helvatical bold",15),command=truck)
    btn1.pack()
    btn2 = Button(frame, text="Lorry ", bg="#40739e", fg="#c8d6e5", width =100,height=2,font=("Helvatical bold",15),command=lorrie)
    btn2.pack()

    changeOnHover(btn1, "#7f8fa6", "#40739e")
    changeOnHover(btn2, "#7f8fa6", "#40739e")

    text = Label(frame, text="developed by sandun tharaka", font=("Helvatical bold", 10), padx=155, pady=10, bg="black",fg="#00d2d3").pack(side="bottom")
    return

#----------------All Vehicle functions ends--------------------#



#clear function is using to clear all widgets in window
def clear():
    for wigets in frame.winfo_children():
        wigets.destroy()
    return
"""
*   when click remove button in the remove vehicle window this function will execute
*   this function needs  only key that user inputs and access to dictionary
"""

def remove(key_var, A, B):
    # assign user inputs to the variables
    key = key_var.get()
    #delete dictionary element using key
    del B[key]
    #delete queue elemet using delete function in queue
    A.delete(key)

    text = Label(frame, text="successfully removed", font=("Helvatical bold", 20), width=100, height=2,bg="#6D214F",fg="#dff9fb").pack()

"""
*   when click add button in the add vehicle window this function will execute
*   this function needs to for parameters that user inputs and access to lists
"""

def add(key_var, value_var, A, B):
    # assign user inputs to the variables
    key = key_var.get()
    value = value_var.get()
    # append dictionary to using key and value

    B[key]=value
    print(B)
    # to add new element to queue using enqueue function
    A.enqueue(key)
    A.display()

    key_var.set("")
    value_var.set("")
    text = Label(frame, text="successfully added", font=("Helvatical bold", 20), width=100, height=2,bg="#6D214F",fg="#dff9fb").pack()

"""
*   addvehicle function to use get details for add vehicle to the system
*   key of the dictionary and value must be insert 
"""
def addvehicle(A,B):

    clear()
    # assigning string variables
    key_var = tk.StringVar()
    value_var = tk.StringVar()

    dec = A.displayNext(-1)
    backbtn(dec)
    text = Label(frame, text="add new vehicle", font=("Helvatical bold", 20), width=100, height=5,bg="#576574",fg="#dff9fb").pack()
    text = Label(frame, text="Add new vehicle", font=("Helvatical bold", 20), width=100, height=1,bg="#576574",fg="#576574").pack()
    lbl1=Label(frame,text="type key", font=("Helvatical bold", 14),bg="#2C3A47",fg="#9AECDB").pack(fill=X)
    # Entry wiget is using to get user inputs
    entry1 =Entry(frame,textvariable=key_var,bd=1,font=("Helvatical bold", 12))
    entry1.pack(fill=X)
    text = Label(frame, text="Add new vehicle", font=("Helvatical bold", 20), width=100, height=1,bg="#576574",fg="#576574").pack()
    lbl1 = Label(frame, text="type details", font=("Helvatical bold", 14),bg="#2C3A47",fg="#9AECDB").pack(fill=X)
    entry2 = Entry(frame,textvariable=value_var, bd=1,font=("Helvatical bold", 12))
    entry2.pack(fill=X)
    text = Label(frame, text="Add new vehicle", font=("Helvatical bold", 20), width=100, height=1, bg="#576574",fg="#576574").pack()
    btnAdd = Button(frame, text="Add",bg="#2c2c54", fg="#dff9fb", font=("Helvatical bold", 14), width=25, height=2,command=lambda:add(key_var,value_var,A,B) )
    btnAdd.pack(fill=X)
    changeOnHover(btnAdd, "#34ace0", "#2c2c54")
    text = Label(frame,text="developed by sandun tharaka",font=("Helvatical bold",10),padx=155,pady=10,bg="black",fg="#00d2d3").pack(side="bottom")
    return
"""
*   removeVehicle function to use get details for remove vehicle to the system
*   key of the dictionary  must be insert 
"""
def removeVehicle(A,B):
    clear()
    key_var = tk.StringVar()
    dec = A.displayNext(-1)
    backbtn(dec)
    text = Label(frame, text="Remove vehicle", font=("Helvatical bold", 20), width=100, height=5,bg="#576574",fg="#dff9fb").pack()
    text = Label(frame, text="vehicle", font=("Helvatical bold", 20), width=100, height=1,bg="#576574",fg="#576574").pack()
    lbl1 = Label(frame, text="type key", font=("Helvatical bold", 14),bg="#2C3A47",fg="#9AECDB").pack(fill=X)
    entry1 = Entry(frame, textvariable=key_var, bd=1,font=("Helvatical bold", 12))
    entry1.pack(fill=X)
    text = Label(frame, text="vehicle", font=("Helvatical bold", 20), width=100, height=1, bg="#576574",fg="#576574").pack()
    btnAdd = Button(frame, text="Remove", font=("Helvatical bold", 14), bg="#2c2c54", fg="black", width=25, height=2,command=lambda: remove(key_var, A, B))
    btnAdd.pack(fill=X)
    changeOnHover(btnAdd, "#34ace0", "#2c2c54")
    text = Label(frame,text="developed by sandun tharaka",font=("Helvatical bold",10),padx=155,pady=10,bg="black",fg="#00d2d3").pack(side="bottom")
    return

"""
*   add_remove function is using to implement add or remove buttons
"""
def add_remove(A,B):

    btnAdd = Button(frame, text="Add", bg="#2C3A47", fg="#dff9fb", width=25, height=2, command=lambda:addvehicle(A,B))
    btnAdd.pack(side=LEFT,padx=5,pady=5)
    btnRemove =Button(frame, text="Remove", bg="#2C3A47", fg="#dff9fb", width=50, height=2, command=lambda:removeVehicle(A,B))
    btnRemove.pack(side=LEFT,padx=5,pady=5)
    changeOnHover(btnAdd, "#34ace0", "#2C3A47")
    changeOnHover(btnRemove, "#34ace0", "#2C3A47")
    return

"""
*   listDetails function is using to get next element of queue list
"""
def vehiList(list):
    for i in range(1, len(list)):
        text = Label(frame, text=list[i], font=("Helvatical bold", 14),width =100,height=2,bg="#40407a",fg="#dff9fb").pack()

    return

def releace(A,dec):
    A.enqueue(dec)
    text = Label(frame, text="Thank you....", font=("Helvatical bold", 20), width=100, height=5, bg="#576574",fg="#00d2d3").pack()

    return

"""
*   when customer click hire vehicle button in vehical list window this function will execute
*   select vehicle is working with only queue list 
"""
def backbtn(dec):

    if (dec.startswith("ac") & dec.find("car")):
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=lambda: carAC())
    elif (dec.startswith("normal") & dec.find("car")):
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10), command=lambda: carnAc())
    elif (dec.startswith("ac") & dec.find("van")):
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=lambda: vanAC())
    elif (dec.startswith("normal") & dec.find("van")):
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=lambda: vannAc())
    elif (dec.startswith("Three")):
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=lambda: threeweel())

    elif (dec.startswith("short")):
        print("found")
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=lambda: truks7Ft())
    elif (dec.startswith("long")):
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10), command=lambda: truks12Ft())
    elif (dec.startswith("low")):
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=lambda: lorrietwoFive())
    elif (dec.startswith("high")):
        btnback = Button(frame, text="back", bg="#5352ed", fg="white", font=("Helvatical bold", 10),command=lambda: lorrietreeFive())

    btnback.pack(side=TOP, anchor=NW)
    changeOnHover(btnback, "#34ace0", "#5352ed")
    return

def selectVehical(A):
    clear()
    #asign availbe vahical to the variable under FIFO method
    #popvehicle = A.displayNext(0)
    dec = A.dequeue()
    backbtn(dec)
    text = Label(frame, text=dec, font=("Helvatical bold", 20), width =100,height=5,bg="#576574",fg="#dff9fb").pack()
    btnreleace = Button(frame, text="release vehicle", bg="#2C3A47",fg="#dff9fb", font=("Helvatical bold", 14), height=2,command=lambda: releace(A,dec))
    btnreleace.pack(fill=X)
    changeOnHover(btnreleace, "#0652DD", "#2C3A47")
    text = Label(frame, text="developed by sandun tharaka", font=("Helvatical bold", 10), padx=155, pady=10, bg="black",fg="#00d2d3").pack(side="bottom")

    return

"""
*   and get dictionary value to applicable to queue element
*   queue list elements are define as same value of dictionary keys 
"""
def listDetails(A,B):
    # to get next available
    available=A.displayNext(0)
    # check every key in the dictionary is equal to queue list element
    for key in B:
        # if element is equal to dictionary key detvehi variable will assign applicable values
        if(key==available):
            detvehi = B[key]

    text = Label(frame, text="available are showing", font=("Helvatical bold", 20), width=100, height=2,bg="#576574",fg="#dff9fb").pack()
    Showtext = Label(frame, text="        " +available , font=("Helvatical bold", 14), width=20, height=5,bg="#f7f1e3",fg="#130f40").pack(fill=X)
    text = Text(frame,wrap=WORD, font=("Helvatical bold", 20), width=100, height=2,bg="#f7f1e3",fg="#130f40")
    text.tag_configure("tag_name",justify="center")
    text.insert("1.0",detvehi,)
    text.tag_add("tag_name", "1.0", "end")
    text.pack()
    btnhire = Button(frame, text="Hire vehicle", bg="#2c2c54", fg="#dff9fb", font=("Helvatical bold", 14), width=10,height=2, command=lambda: selectVehical(A))
    btnhire.pack(fill=X)
    changeOnHover(btnhire, "#34ace0", "#2c2c54")
    return

#function is using to hover in buttons
def changeOnHover(button, colorOnHover, colorOnLeave):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))
    return

if __name__ == '__main__':
    """
    *GUI is making with tkinter 
    """
    #assigning TK functions to root variable
    root = Tk()
    #main window size(width=400 heigth=600)
    root.geometry("400x600")
    #title of the program
    root.title("safe drive")
    # window icon
    root.iconbitmap('icon.ico')
    #dissble maximize option in window
    root.resizable(0,0)
    # new frame assign to frame variable
    frame = Frame(root,bg="#576574")
    # positions and alighments of frame
    frame.pack(side="top",expand=True,fill="both")
    #background color for root
    root.configure(background="#576574")
    #main labels are define as same variable

    text = Label(frame,text="select your vehicle type",font=("Helvatical bold",20),width =100,height=5,bg="#576574",fg="#c8d6e5").pack()
    # to get space between two wigets is using label wigets its background color is same as frame bg color
    text = Label(frame, text="select your vehicle type", font=("Helvatical bold", 10),bg="#576574",fg="#576574").pack()
    #main two buttons in main window
    myButton1 = Button(frame,text="passenger",bg="#222f3e",fg="#c8d6e5",command=passenger,width =100,height=5,font=("Helvatical bold",15))
    myButton1.pack(fill=X)
    myButton2 = Button(frame,text="goods to delivery",bg="#222f3e",fg="#c8d6e5",command=carrier,width =100,height=5,font=("Helvatical bold",15))
    myButton2.pack(fill=X)


    # colors as argument
    changeOnHover(myButton1, "#341f97", "#222f3e")
    changeOnHover(myButton2, "#341f97", "#222f3e")
    #changeOnHover(btn2, "red", "yellow")

    text = Label(frame,text="developed by sandun tharaka",font=("Helvatical bold",10),padx=155,pady=10,bg="black",fg="#00d2d3").pack(side="bottom")

    root.mainloop()
