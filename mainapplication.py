import customtkinter as ctk
from PIL import ImageTk, Image
import dashboard.maindashboard as das


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def mainapplication():
    mainapp = ctk.CTk()
    mainapp.geometry("1200x600")
    mainapp.title("AutoX App")
    mainapp.configure(bg='light blue')

    def maindashboardopen(event):
        frame = event.widget
        mainapp.destroy()
        das.dashboardf()
    
    #all frames
    frame2=ctk.CTkFrame(master=mainapp)
    frame2.place(x=25,y=80,relwidth=0.6,relheight=0.4)
   #    frame2.bind("<Button-1>",frame_clicked)

    frame3=ctk.CTkFrame(master=mainapp)
    frame3.place(x=780,y=140,relwidth=0.3,relheight=0.3)

    frame4=ctk.CTkFrame(master=mainapp)
    frame4.place(x=25,y=370,relwidth=0.27,relheight=0.3)

    frame5=ctk.CTkFrame(master=mainapp)
    frame5.place(x=400,y=370,relwidth=0.27,relheight=.3)

    frame6 = ctk.CTkFrame(master=mainapp)
    frame6.place(x=800, y=370, relwidth=0.27, relheight=0.3)

    #Setting Images to Frame
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
    label2.bind("<Button-1>",maindashboardopen)

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

    #Warning Label
    labelcheck=ctk.CTkLabel(mainapp,text="Register Yourself and Check Other Credentials in Settings Tab",font=("Arial",14),fg_color="red")
    labelcheck.place(x=500,y=30)


    entry=ctk.CTkEntry(mainapp)
    entry.place(x=100,y=30)

    useridbutton=ctk.CTkButton(mainapp,text="Enter Your User Id")
    useridbutton.place(x=300,y=30)




    mainapp.mainloop()


# Call the main application function just for test purpose
mainapplication()













