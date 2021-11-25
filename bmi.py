#IMPORTING MUDULES
from tkinter import *
from tkinter import messagebox
#ROOT WINDOW CONFIGURATION

root=Tk()
root.title("Bmi Calculator")
root.config(bg="black")
root.iconbitmap(r'C:/Users/Administrator/Desktop/Projects/Bmi Calculator/Assets/bmi.ico')
root.resizable(False,False)

calcbt=PhotoImage(file="C:/Users/Administrator/Desktop/Projects/Bmi Calculator/Assets/calc.png")
calcbt=calcbt.subsample(x=20,y=30)


resetbt=PhotoImage(file="C:/Users/Administrator/Desktop/Projects/Bmi Calculator/Assets/reset.png")
resetbt=resetbt.subsample(x=20,y=30)


#ENTRY WIDGETS
height=Entry(root,relief=SUNKEN,bg="#ADFF2F",fg="black",font=("comicsans",15,"bold"))
height.grid(row=0,column=2)
weight=Entry(root,relief=SUNKEN,bg="#ADFF2F",fg="black",font=("comicsans",15,"bold"))
weight.grid(row=1,column=2)

#ABOUT FUNCTION
def info():
    messagebox.showinfo("About",f"This BMI calculator was made by Sabir Khan\n You can support him by followimg his social handles\nInstagram-@the_sigma_programmer\nFacebook-Sabir Khan\nTwitter-@sabir_khan58\nTelegram-@INFINIXEL")

#MENU WIDGET
menubar= Menu(root)
menubar.add_cascade(label="About",command=info)
root.config(menu=menubar)


#DEFINING BMI FUNCTION
def BMICALC():
    heightval=float(height.get())/100
    weightval=float(weight.get())
    bmival=weightval/(heightval*heightval)
    bmival=round(bmival,1)
    bmi_index(bmival)

#DEFINING BMI LOOP
def bmi_index(bmival):
    if bmival<18.5:
        bmilbl.config(text=(f'{bmival} Which is Underweight'))
    elif bmival>18.5 and bmival<24.9:
        bmilbl.config(text=(f'{bmival} Which is Normal'))
    elif bmival>24.9 and bmival<29.9:
       bmilbl.config(text=(f'{bmival} Which is Overweight'))
    elif bmival>29.9:
       bmilbl.config(text=(f'{bmival} is Obesity'))
    else:
        bmilbl.config(text=("Something Went Wrong"))

#DEFINING RESET FUNCTION
def reset_entry():
    height.delete(0,'end')
    weight.delete(0,'end')
    bmilbl.destroy()

#DEFINING LABELS
heightlbl=Label(root,text="Enter Your Height(in cms)",bg="black",fg="white",font=("comicsans",15,"bold")).grid(row=0,column=1)
waeghtlbl=Label(root,text="Enter Your Weight(in kgs)",bg="black",fg="white",font=("comicsans",15,"bold")).grid(row=1,column=1)
b1=Button(root,image=calcbt,command=BMICALC,borderwidth=0,bg="black",activebackground="black").grid(row=3,column=2)
b2=Button(root,image=resetbt,command=reset_entry,borderwidth=0,bg="black",activebackground="black").grid(row=3,column=3)
bmilbl=Label(root,fg="white",bg="black",font=("comicsans",18,"bold"))
bmilbl.grid(row=4,column=2)
displaylbl=Label(root,text="Your BMI Is : ",bg="black",fg="white",font=("comicsans",18,"bold")).grid(row=4,column=1)

#MAINLOOP FUNCTION
root.mainloop()
