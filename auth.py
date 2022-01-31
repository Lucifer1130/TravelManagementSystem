from tkinter import *
import os
from PIL import Image, ImageTk

global a
a = 0


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info + "", "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            screen.destroy()
            global a
            a = 1
        else:
            password_not_recognised()

    else:
        user_not_found()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("1024x768")
    screen.title("Tours and Travel Management System")
    screen.config(bg="RosyBrown")
    Label(text="Tours and Travel Management System", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="",bg="RosyBrown").pack()
    Label(screen, text="Please enter details below to login", bg="RosyBrown").pack()
    Label(screen, text="", bg="RosyBrown").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen, text="Username * ",bg="RosyBrown").pack()
    username_entry1 = Entry(screen, textvariable=username_verify)
    username_entry1.pack()
    Label(screen, text="", bg="RosyBrown").pack()
    Label(screen, text="Password * ", bg="RosyBrown").pack()
    password_entry1 = Entry(screen, textvariable=password_verify)
    password_entry1.pack()
    Label(screen, text="", bg="RosyBrown").pack()
    Button(screen, text="Login", width=10, height=1, command=login_verify).pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    load1 = Image.open("F:\image.JPG")
    render1 = ImageTk.PhotoImage(load1)
    Label(screen, image=render1).pack()

    screen.mainloop()
