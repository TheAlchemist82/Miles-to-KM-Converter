import tkinter

def miles_input():
    mile = float(input_miles.get())
    mile_final = mile * 1.609
    label_final.config(text=f"{mile_final}")

window = tkinter.Tk()
window.title("Miles to KM converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_is_equal_to = tkinter.Label(text="is equal to")
label_is_equal_to.grid(column=0, row=1)

label_final = tkinter.Label(text="0")
label_final.grid(column=1, row=1)

label_km = tkinter.Label(text="Kilometers")
label_km.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=miles_input)
button.grid(column=1, row=2)

window.mainloop()
