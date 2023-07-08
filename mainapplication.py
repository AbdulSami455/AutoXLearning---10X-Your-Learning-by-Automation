import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def mainapplication():
    mainapp = ctk.CTk()
    mainapp.geometry("1200x600")
    mainapp.title("AutoX App")
    mainapp.configure(bg='light blue')

    frame = ctk.CTkFrame(master=mainapp)
    frame.place(x=10, y=0, relwidth=0.4, relheight=0.05)

    button = ctk.CTkButton(frame, text="Button",width=10,height=2)
    button.place(x=0, y=1)

    button2 = ctk.CTkButton(frame, text="Button", width=10, height=2)
    button2.place(x=100, y=1)

    button3 = ctk.CTkButton(frame, text="Button", width=10, height=2)
    button3.place(x=200, y=1)

    button4 = ctk.CTkButton(frame, text="Button", width=10, height=2)
    button4.place(x=300, y=1)
    
    button5 = ctk.CTkButton(frame, text="Button", width=10, height=2)
    button5.place(x=400, y=1)

    frame2=ctk.CTkFrame(master=mainapp)
    frame2.place(x=25,y=80,relwidth=0.6,relheight=0.4)



    mainapp.mainloop()


# Call the main application function just for test purpose
mainapplication()













