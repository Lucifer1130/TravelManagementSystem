import tkinter

# from tkinter import scrolledtext
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import messagebox
import pyodbc
from PIL import Image, ImageTk

mydb= pyodbc.connect('Driver={SQL Server};'
                      'Server=CHIKU;'
                      'Database=tours;'
                      'Trusted_Connection=yes;')

cursor = mydb.cursor()

window = tkinter.Tk()
window.geometry("1024x768")
window.resizable(0, 0)
window.title("Vehicle Detailer")
window.config(bg="cyan")


# function ez
def ez():
    messagebox.showinfo("Alert", "Yay, Successful")
    cursor.execute("SELECT VehicleNo, COUNT(Vehicle No) AS MOST_FREQUENT from "
                   "dbo.projdset1 GROUP BY VehicleNo ORDER BY COUNT("
                   "VehicleNo) DESC")

    # Creating tkinter window
    win = tk.Tk()
    win.title("ToursNTravels")

    # Title Label
    tk.Label(win,
             text="OutPut",
             font=("Times New Roman", 15),
             background='green',
             foreground="white").grid(column=0,
                                      row=0)
    text_area = st.ScrolledText(win,
                                width=30,
                                height=8,
                                font=("Times New Roman",
                                      15))

    text_area.grid(column=10, pady=10, padx=10)

    for row in cursor:
        text_area.insert(tk.INSERT, row)
        text_area.insert(tk.INSERT, "\n")

    text_area.configure(state='disabled')


def close_window():
    window.destroy()


load = Image.open("F:\img.jpg")
render = ImageTk.PhotoImage(load)

a = tkinter.Label(window, justify="center", text="Tours and Travels Management System", bg="cyan", font=("Arial", 20))
a.config(justify='center')
a.pack()
b = tkinter.Label(window, image=render).pack()
c = tkinter.Button(window, text="Get most frequent vehicle used", fg="red", command=ez).pack()
d = tkinter.Button(window, text="Exit", command=close_window, height=2, width=30).pack()

window.mainloop()