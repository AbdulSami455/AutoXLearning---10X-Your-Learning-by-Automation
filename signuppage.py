import customtkinter as ctk
from PIL import ImageTk, Image
import authentication as auth1
#import mainwindow as w

def signuppage():
    signuppage = ctk.CTk()
    signuppage.geometry("1000x500")
    signuppage.title("AutoX Signing Up")
    signuppage.configure(bg="light blue")

    header_label = ctk.CTkLabel(signuppage, text="  Signup Now,if You are New User  ", font=("Montserrat", 22, "bold"))
    header_label.place(x=300, y=100)

    label1 = ctk.CTkLabel(signuppage, text="Enter Your Username:")
    label1.place(x=200, y=170)

    entry1 = ctk.CTkEntry(signuppage, width=300)
    entry1.place(x=200, y=200)

    label2 = ctk.CTkLabel(signuppage, text="Enter Your Password:")
    label2.place(x=200, y=230)

    # Password Label and Entry
    entry2 = ctk.CTkEntry(signuppage, width=300)
    entry2.place(x=200, y=260)
    def signupnow():
        auth1.signup(entry1.get(),entry2.get())
        signuppage.destroy()
    signbutton=ctk.CTkButton(signuppage,text="Sign Up now",command=signupnow)
    signbutton.place(x=200,y=350)


