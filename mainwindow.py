import customtkinter as ctk
from PIL import ImageTk, Image
import authentication as auth
import signuppage as sp

# Main Window GUI
loginpage = ctk.CTk()
loginpage.geometry("1000x500")
loginpage.title("AutoX Login Now")

# Photo in Background
image = Image.open("6263767_3236267-removebg-preview.png")
image = image.resize((700, 400))

photo = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(loginpage, image=photo)
label.place(x=-60, y=50)

# Username Label and Entry
label1 = ctk.CTkLabel(loginpage, text="Username:")
label1.place(x=550, y=200)

entry1 = ctk.CTkEntry(loginpage, width=200)
entry1.place(x=650, y=200)

label2 = ctk.CTkLabel(loginpage, text="Password:")
label2.place(x=550, y=260)

# Password Label and Entry
entry2 = ctk.CTkEntry(loginpage, width=200, show="*")
entry2.place(x=650, y=260)

# Header Label
header_label = ctk.CTkLabel(loginpage, text="Login Now", font=("Montserrat", 22, "bold"))
header_label.place(x=650, y=100)

def login():
    if auth.login(entry1.get(), entry2.get()):
        print("Hello Everyone")
    else:
        print("Not Hello")

login_button = ctk.CTkButton(loginpage, text="Login", command=login)
login_button.place(x=700, y=320)

signup_label = ctk.CTkLabel(loginpage, text="Signup (If you are New)", font=("Montserrat", 11, "bold"))
signup_label.place(x=680, y=380)

def sip():
    sp.signuppage()

signup_button = ctk.CTkButton(loginpage, text="Signup Now", command=sip)
signup_button.place(x=700, y=420)

loginpage.mainloop()
