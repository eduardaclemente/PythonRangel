import tkinter as tk

app = tk.Tk()
app.geometry("400x300")
app.configure(bg="#777")

visor_value = 0
result = 0

def btn_0():
    global visor_value
    visor_value *= 10
    visor_value += 0
    visor.configure(text=visor_value)

def btn_1():
    global visor_value
    visor_value *= 10
    visor_value += 1
    visor.configure(text=visor_value)

def btn_2():
    global visor_value
    visor_value *= 10
    visor_value += 2
    visor.configure(text=visor_value)

def btn_3():
    global visor_value
    visor_value *= 10
    visor_value += 3
    visor.configure(text=visor_value)

def btn_4():
    global visor_value
    visor_value *= 10
    visor_value += 4
    visor.configure(text=visor_value)

def btn_5():
    global visor_value
    visor_value *= 10
    visor_value += 5
    visor.configure(text=visor_value)

def btn_6():
    global visor_value
    visor_value *= 10
    visor_value += 6
    visor.configure(text=visor_value)

def btn_7():
    global visor_value
    visor_value *= 10
    visor_value += 7
    visor.configure(text=visor_value)

def btn_8():
    global visor_value
    visor_value *= 10
    visor_value += 8
    visor.configure(text=visor_value)

def btn_9():
    global visor_value
    visor_value *= 10
    visor_value += 9
    visor.configure(text=visor_value)

def btn_equal():
    pass

def btn_plus():
    pass

def btn_minus():
    pass

def btn_mult():
    pass

def btn_div():
    pass


visor = tk.Label(app, text="", bg="white", width=30, height=2)
visor.grid(columnspan=4, column=0, row=0, pady=10)

btn_plus = tk.Button(app, text="+", bg="silver", command=btn_plus, width=5, height=2)
btn_plus.grid(column=0, row=1, padx=5, pady=5)

btn_div = tk.Button(app, text="/", bg="silver", command=btn_div, width=5, height=2)
btn_div.grid(column=0, row=2, padx=5, pady=5)

btn_mult = tk.Button(app, text="*", bg="silver", command=btn_mult, width=5, height=2)
btn_mult.grid(column=0, row=3, padx=5, pady=5)

btn_minus = tk.Button(app, text="-", bg="silver", command=btn_minus, width=5, height=2)
btn_minus.grid(column=0, row=4, padx=5, pady=5)

btn_equal = tk.Button(app, text="=", bg="silver", command=btn_equal, width=5, height=2)
btn_equal.grid(column=0, row=5, padx=5, pady=5)

btn_1 = tk.Button(app, text="1", bg="silver", command=btn_1, width=5, height=2)
btn_1.grid(column=1, row=1, padx=5, pady=5)

btn_2 = tk.Button(app, text="2", bg="silver", command=btn_2, width=5, height=2)
btn_2.grid(column=2, row=1, padx=5, pady=5)

btn_3 = tk.Button(app, text="3", bg="silver", command=btn_3, width=5, height=2)
btn_3.grid(column=3, row=1, padx=5, pady=5)

btn_4 = tk.Button(app, text="4", bg="silver", command=btn_4, width=5, height=2)
btn_4.grid(column=1, row=2, padx=5, pady=5)

btn_5 = tk.Button(app, text="5", bg="silver", command=btn_5, width=5, height=2)
btn_5.grid(column=2, row=2, padx=5, pady=5)

btn_6 = tk.Button(app, text="6", bg="silver", command=btn_6, width=5, height=2)
btn_6.grid(column=3, row=2, padx=5, pady=5)

btn_7 = tk.Button(app, text="7", bg="silver", command=btn_7, width=5, height=2)
btn_7.grid(column=1, row=3, padx=5, pady=5)

btn_8 = tk.Button(app, text="8", bg="silver", command=btn_8, width=5, height=2)
btn_8.grid(column=2, row=3, padx=5, pady=5)

btn_9 = tk.Button(app, text="9", bg="silver", command=btn_9, width=5, height=2)
btn_9.grid(column=3, row=3, padx=5, pady=5)

btn_0 = tk.Button(app, text="0", bg="silver", command=btn_0, width=5, height=2)
btn_0.grid(column=2, row=4, padx=5, pady=5)


app.mainloop()