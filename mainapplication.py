import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def mainapplication():
    mainapp = ctk.CTk()
    mainapp.geometry("1200x600")
    mainapp.title("AutoX App")
    mainapp.configure(bg='light blue')

    frame = ctk.CTkFrame(master=mainapp)
    frame.place(x=200, y=0, relwidth=1.0, relheight=0.15)

    mainapp.mainloop()

# Call the main application function
mainapplication()













