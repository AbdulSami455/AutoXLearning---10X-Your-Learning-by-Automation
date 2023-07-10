import customtkinter as ctk
from PIL import ImageTk, Image

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

    frame3=ctk.CTkFrame(master=mainapp)
    frame3.place(x=780,y=140,relwidth=0.3,relheight=0.3)

    frame4=ctk.CTkFrame(master=mainapp)
    frame4.place(x=25,y=370,relwidth=0.27,relheight=0.3)

    frame5=ctk.CTkFrame(master=mainapp)
    frame5.place(x=400,y=370,relwidth=0.27,relheight=.3)

    frame6 = ctk.CTkFrame(master=mainapp)
    frame6.place(x=800, y=370, relwidth=0.27, relheight=0.3)

    #image for frame 3
    image = Image.open("Add a heading (5).png")
    image = image.resize((380, 180), Image.ANTIALIAS)
    image_tk = ImageTk.PhotoImage(image)
    label = ctk.CTkLabel(frame3, image=image_tk)
    label.configure(text="")
    label.pack()

    image = Image.open("Add a heading.png")
    image= image.resize((700, 250), Image.ANTIALIAS)
    image_tk2 = ImageTk.PhotoImage(image)
    label2 = ctk.CTkLabel(frame2, image=image_tk2)
    label2.configure(text="")
    label2.pack()

    image = Image.open("Add a heading (3).png")
    image = image.resize((350, 250), Image.ANTIALIAS)
    image_tk2 = ImageTk.PhotoImage(image)
    label3 = ctk.CTkLabel(frame4, image=image_tk2)
    label3.configure(text="")
    label3.pack()


    image = Image.open("Add a heading (4).png")
    image = image.resize((350, 250), Image.ANTIALIAS)
    image_tk3 = ImageTk.PhotoImage(image)
    label4 = ctk.CTkLabel(frame5, image=image_tk3)
    label4.configure(text="")
    label4.pack()

    image = Image.open("Add a heading (2).png")
    image = image.resize((350, 250), Image.ANTIALIAS)
    image_tk4 = ImageTk.PhotoImage(image)
    label5 = ctk.CTkLabel(frame6, image=image_tk4)
    label5.configure(text="")
    label5.pack()




    mainapp.mainloop()


# Call the main application function just for test purpose
mainapplication()













