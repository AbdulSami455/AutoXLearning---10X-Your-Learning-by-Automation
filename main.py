import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import authentication as auth
# Main Window GUI
loginpage = tk.Tk()
loginpage.geometry("1000x500")
loginpage.title("AutoX Login Now")

# Photo in Background
image = Image.open("6263767_3236267-removebg-preview.png")
image = image.resize((700, 400))

photo = ImageTk.PhotoImage(image)
label = tk.Label(loginpage, image=photo)
label.place(x=-60, y=50)


#Username Label and Entry
label1 = tk.Label(loginpage, text="Username:")
label1.place(x=550, y=200)

entry1 = tk.Entry(loginpage, width=40)
entry1.place(x=650, y=200)

label2 = tk.Label(loginpage, text="Password:")
label2.place(x=550, y=260)

#Password Label and Entry
entry2 = tk.Entry(loginpage, width=40)
entry2.place(x=650, y=260)
#Header Label
header_label = tk.Label(loginpage, text="Login With Firebase", font=("Arial", 24, "bold"))
header_label.place(x=650, y=100)



login_button = tk.Button(loginpage, text="Login",command=login)
login_button.place(x=650, y=320)

loginpage.mainloop()






