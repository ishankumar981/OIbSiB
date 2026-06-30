from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal Weight"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        result.config(text=f"BMI = {bmi:.2f}\nStatus: {status}")

    except:
        messagebox.showerror("Error", "Enter valid values.")

root = Tk()
root.title("BMI Calculator")
root.geometry("350x300")

Label(root, text="Weight (kg)").pack(pady=5)
weight_entry = Entry(root)
weight_entry.pack()

Label(root, text="Height (cm)").pack(pady=5)
height_entry = Entry(root)
height_entry.pack()

Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=15)

result = Label(root, text="", font=("Arial", 12))
result.pack()

root.mainloop()
