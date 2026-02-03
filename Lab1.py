# Brandon Knorr
# Mod 2 Lab 1 
# due: 1/28

# Functions 
    # store code
    # 1. def
    # 2. function_name
    # 3. () optional parameters
    #       parameters are variables used within the function
    # 4. : declare the scope of the function
    #       scope is a subset of code
    # 5. Body of the function (stored code)
    # 6. Optional return statement 
    #       sends value back to the function call
    #       once you hit a return statement the function ends

import tkinter as tk
from tkinter import messagebox


def get_area(length, width):
    return length * width

def calculate_area_from_user():
        l = float(entry_length.get())
        w = float(entry_width.get())
        
        area = get_area(l, w)
        
     
        label_result.config(text=f"The area is: {area}", fg="green")
        

# --- GUI Setup ---

root = tk.Tk()
root.title("Simple Area Calc")


tk.Label(root, text="Length:").pack(pady=2)
entry_length = tk.Entry(root)
entry_length.pack(pady=2)

tk.Label(root, text="Width:").pack(pady=2)
entry_width = tk.Entry(root)
entry_width.pack(pady=2)


btn_calculate = tk.Button(root, text="Calculate", command=calculate_area_from_user)
btn_calculate.pack(pady=10)


label_result = tk.Label(root, text="The area is: ", font=("Arial", 10, "bold"))
label_result.pack(pady=5)

root.mainloop()


