import tkinter as tk
from tkinter import messagebox

TITLE_FONT = ('Nunito', 20, 'bold')
FONT = ('Nunito', 11, 'normal')

MODE = ('km', 'Miles')

MILE_IN_KM = 1.609347218694


def convert():

    try:
        if radio_state.get() == 0:
            out = float(in_entry.get()) * MILE_IN_KM
            out_label.config(text=f'Is equal to: {round(out, 2)} Km')
        else:
            out = float(in_entry.get()) / MILE_IN_KM
            out_label.config(text=f'Is equal to: {round(out, 2)} Miles')

    except ValueError:
        out_label.config(text=f'Is equal to: 0 {MODE[radio_state.get()]}')
        messagebox.showerror(title='Value Error', message="Enter only numbers")


def change_mode():

    if radio_state.get() == 0:
        title_label.config(text='Miles to Km Converter!')
        in_label.config(text='Miles')
    else:
        title_label.config(text='Km to Miles Converter!')
        in_label.config(text='Km')

    in_entry.delete(0, tk.END)
    in_entry.insert(tk.END, '0')

    out_label.config(text=f'Is equal to: 0 {MODE[radio_state.get()]}')


window = tk.Tk()
window.title('Converter')
window.config(pady=20, padx=20)

title_label = tk.Label(text='Miles to Km Converter!', font=TITLE_FONT)
title_label.grid(row=0, column=0, columnspan=2)

intro_label = tk.Label(text='Enter the number of units you want to convert:', font=FONT)
intro_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

in_entry = tk.Entry(width=10, justify=tk.CENTER)
in_entry.insert(tk.END, '0')
in_entry.grid(row=3, column=0, sticky="E")

in_label = tk.Label(text='Miles', font=FONT)
in_label.grid(row=3, column=1, sticky='W', padx=(10, 0))

out_label = tk.Label(text='Is equal to: 0 Km', font=FONT)
out_label.grid(row=4, column=0, columnspan=2, pady=(0, 15))

convert_button = tk.Button(text='Convert', command=convert)
convert_button.grid(row=5, column=0, sticky='E', padx=(10, 10))

mode_label = tk.Label(text="Mode:")
mode_label.grid(row=5, column=1, sticky='W', padx=(0, 10))

radio_state = tk.IntVar()
radio_state.set(0)

miles_to_km_button = tk.Radiobutton(text='Miles to Km', value=0, variable=radio_state, command=change_mode)
miles_to_km_button.grid(row=6, column=0, columnspan=2, pady=(10, 0))
km_to_miles_button = tk.Radiobutton(text='Km to Miles', value=1, variable=radio_state, command=change_mode)
km_to_miles_button.grid(row=7, column=0, columnspan=2)

window.mainloop()
