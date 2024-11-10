from tkinter import *
import random


# FUNCTION
def generate():
    output.delete(0, END)
    characters = "ABCDEFGHIJKLMNOPRSTUVWZXYQabcdefghijklmnoprstuvzyxw}q0123456789[]{:;?\?+#" 
    length = 20
    for x in range(1):
        password = "".join(random.sample(characters, length))
    output.insert(0, password)


# ROOT  (WINDOW)
window = Tk()
window.title("Password Generator")
window.minsize(500,500)
window.resizable(width=False,height=False)
window.config(bg="#0492C2")


# BACKGROUND
background_img = PhotoImage(file="background.png")
canvas = Canvas(window, width=500, height=500)
canvas.create_image(0, 0, anchor=NW, image=background_img)
canvas.pack()


# ENTRY - Output for generated password
output = Entry(bg="#B0E0E6",fg="black",font=("Helvetica",20,"bold"),width=22,borderwidth=5)
output.focus()
output.place(x=80,y=250)


# BUTTON - For generate
button_gen = Button(text="Generate",bg="#1F456E",fg="#AEF359",font=("Helvetica",15, "bold"), borderwidth=10, relief="raised", activebackground="#004F98", activeforeground="#AEF359", command=generate,cursor="hand2")
button_gen.place(x=185,y=320)


window.mainloop()


