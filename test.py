import tkinter as tk
from tkinter import ttk

# แปลงค่าในหน่วยเมตร
conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.1,
        'millimeters': 0.01,
        'feet': 0.3048,
}

# หลักการแปลงค่า
def convert_units(amout, from_unit, to_unit):
    if from_unit in conversion_factors and to_unit in conversion_factors:
        amount_in_meters = amout * conversion_factors[from_unit]
        converted_amount = amount_in_meters / conversion_factors[to_unit]
        return converted_amount
    else:
        return None
    
# Function
def on_convert():
    try:
        amount = float(entry_amount.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        result = convert_units(amount, from_unit, to_unit)
        if result is not None:
            label_result.config(text=f"{result:.4f} {to_unit}")
        else:
            label_result.config(text="Conversion error")
    except ValueError:
        label_result.config(text="Invalid input")

# สร้างหน้าapp
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x200")

# widget
label_amount = ttk.Label(root, text="Amount:")
label_amount.grid(column=0, row=0, padx=10, pady=10)

entry_amount = ttk.Entry(root)
entry_amount.grid(column=1, row=0, padx=10, pady=10)

label_from = ttk.Label(root, text="From:")
label_from.grid(column=0, row=1, padx=10, pady=10)

combo_from = ttk.Combobox(root, values=list(conversion_factors.keys()), state="readonly")
combo_from.grid(column=1, row=1, padx=10, pady=10)
combo_from.current(0)

label_to = ttk.Label(root, text="To:")
label_to.grid(column=0, row=2, padx=10, pady=10)

combo_to = ttk.Combobox(root, values=list(conversion_factors.keys()), state="readonly")
combo_to.grid(column=1, row=2, padx=10, pady=10)
combo_to.current(1)

button_convert = ttk.Button(root, text="Convert", command=on_convert)
button_convert.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

label_result = ttk.Label(root, text="")
label_result.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
