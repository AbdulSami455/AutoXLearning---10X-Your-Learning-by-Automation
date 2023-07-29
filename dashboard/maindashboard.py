import customtkinter as ctk
import os
import exceptiongroup
from PIL import ImageTk, Image
import webbrowser

folder_name="AutoX Learning"
parent_directory="/home/sami/Desktop/Working/"
def createfolder(folder_name,parent_directory):
    try:
      folder_path = os.path.join(parent_directory, folder_name)
      os.mkdir(folder_path)
      print(f"Folder '{folder_name}' created successfully in '{parent_directory}'.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists in '{parent_directory}'.")
    except Exception as e:
        print(f"An error occurred while creating folder '{folder_name}' in '{parent_directory}': {e}")
def dashboardf():
     dash=ctk.CTk()
     dash.geometry("1000x600")

     def searchnow():
        webbrowser.open(f"https://www.google.com/search?q={search.get()}")

     heading_label = ctk.CTkLabel(dash, text="Top Websites To Learn", font=("Helvetica", 22, "bold"))
     heading_label.place(x=90,y=70)
     # Pack the label to display it in the window

     image = Image.open("q8-vPggS_400x400-removebg-preview.png")
     image = image.resize((30, 30), Image.ANTIALIAS)
     image_tk = ImageTk.PhotoImage(image)

     # Search Button with Icon
     searchbutton = ctk.CTkButton(dash, text="Search Now", image=image_tk, compound=ctk.LEFT,command=searchnow)
     searchbutton.place(x=650, y=16)

     search = ctk.CTkEntry(dash, width=550, height=30)
     search.place(x=90, y=20)

     site1=ctk.CTkButton(dash,text="CodeAcademy",command=searchnow)
     site1.place(x=90,y=120)

     site2=ctk.CTkButton(dash)


     createfolder(folder_name,parent_directory)


