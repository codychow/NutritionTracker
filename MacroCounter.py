import tkinter as tk
from tkinter import messagebox, Text, IntVar

import os

calories = []
protein = []

def enterMacros(cal,pro):

    calories.append(cal)
    print("cal:", cal)
    protein.append(pro)
    print("pro:",pro)
    calorieInput.delete(0,'end')
    proteinInput.delete(0,'end')
    """
    # ADD ERROR CHECKiNG L8R
    if(cal and pro):    
    else:
        errorLabel = tk.Label(frame, text="Fill in both fields", fg="black", bg="#3483EB")
        errorLabel.place(relx=0.5, rely=0.5, relwidth = 0.25, relheight=0.05, anchor='n')
    """

def calculateMacros():
    totalCal = 0
    totalPro = 0
    for cal in calories:
        totalCal = cal + totalCal
        print(cal, ",")
    for pro in protein:
        totalPro = pro + totalPro
        print(pro, ",")
    calorieCalcLabel = tk.Label(frame, text="Calories: " + str(totalCal) + " cal", fg="black", bg="#3483EB")
    calorieCalcLabel.place(relx=0.5, rely=0.5, relwidth = 0.25, relheight=0.05, anchor='n')
    proteinCalcLabel = tk.Label(frame, text="Protein: " + str(totalPro) + " g", fg="black", bg="#3483EB")
    proteinCalcLabel.place(relx=0.5, rely=0.55, relwidth = 0.25, relheight=0.05, anchor='n')

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

frame = tk.Frame(root, bg="#3483EB")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

calorieLabel = tk.Label(frame, text="Enter calories here:", fg="black", bg="#3483EB")
calorieLabel.place(relx=0.25, rely=0.3, relwidth = 0.25, relheight=0.05, anchor='n')

calorieInput = tk.Entry(frame, bg="white")
calorieInput.place(relx=0.35, rely=0.3, relwidth = 0.0625, relheight=0.05)

proteinLabel = tk.Label(frame, text="Enter protein here:", fg="black", bg="#3483EB")
proteinLabel.place(relx=0.25, rely=0.375, relwidth = 0.25, relheight=0.05, anchor='n')

proteinInput = tk.Entry(frame, bg="white")
proteinInput.place(relx=0.35, rely=0.375, relwidth = 0.0625, relheight=0.05)

enterButton = tk.Button(frame, text="Enter", padx=50, pady=5, fg="black",
                      command=lambda:enterMacros(int(calorieInput.get()), int(proteinInput.get())))
enterButton.place(relx=0.7, rely=0.3, relwidth=0.5, relheight=0.125, anchor='n')

runButton = tk.Button(frame, text="End Day", padx=50, pady=5, fg="black",
                      command=lambda: calculateMacros())
runButton.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.125, anchor='n')

root.mainloop()

