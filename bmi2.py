from tkinter import *

window = Tk()
window.title ("BMI Calculator")

lab1 = Label (text="Weight (in kilograms)")
lab1.grid (column=0, row=1)

lab2 = Label (text="Height (in metres)")
lab2.grid (column=0, row=2)

lab3 = Label (text="", font=("Lucida", 10))
lab3.grid (column=1, row=4)

lab4 = Label (text="", font=("Lucida", 15, 'bold'))
lab4.grid (column=1, row=5)

entry1 = Entry ()
entry1.grid (column=1, row=1)

entry2 = Entry ()
entry2.grid (column=1, row=2)

def bmi():
    res = ""
    wt = float (entry1.get())
    ht = float (entry2.get())
    bmii = round (wt/(ht**2),2)
    if bmii <= 18.4:
        res = "Underweight"
    elif bmii >= 18.5 and bmii < 24.9:
        res = "Normal"
    elif bmii >= 25.0 and bmii < 39.9:
        res = "Overweight"
    else:
        res = "Obese"

    lab3.config (text=f"Your BMI is {bmii}kg/m2")
    lab4.config (text=f"You Are {res}.")
   

btn = Button (text="Calculate", command=bmi)
btn.grid (column=1, row=3)

mainloop()