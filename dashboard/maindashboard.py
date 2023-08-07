import dashboard.codewebsites as cw
import customtkinter as ctk
import os
import exceptiongroup
from PIL import ImageTk, Image
import webbrowser
import dashboard.downloadfiles as dd
import requests
API_KEY = 'a8ab6d9bd5684d27bab671e76c15eb91'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

# Define parameters for the request (you can customize these)
parameters = {
    'country': 'us',
     'category':'science',# Replace 'us' with the country code you want headlines from.
    'apiKey': API_KEY
}

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


     #all Sites for COding Learning
     site1=ctk.CTkButton(dash,text="CodeAcademy",command=cw.codeacademy)
     site1.place(x=90,y=120)
       
     site2=ctk.CTkButton(dash,text="FreeCodeCamp",command=cw.freecodecamp)
     site2.place(x=260,y=120)

     site3=ctk.CTkButton(dash,text="Coursera",command=cw.coursera)
     site3.place(x=430,y=120)

     site4=ctk.CTkButton(dash,text="W3Schools",command=cw.w3schools)
     site4.place(x=610,y=120)

     site5=ctk.CTkButton(dash,text="Udacity",command=cw.udacity)
     site5.place(x=780,y=120)


     #Heading for Docs Download
     heading_label2 = ctk.CTkLabel(dash, text="Top Docs To Download", font=("Helvetica", 22, "bold"))
     heading_label2.place(x=90, y=175)

     #Docs for All Programming Languages
     image2 = Image.open("python-7be70baaac.png")
     image2 = image2.resize((45, 40), Image.ANTIALIAS)
     image_tk2 = ImageTk.PhotoImage(image2)
     pythonbutton = ctk.CTkButton(dash, image=image_tk2, text="",command=dd.pythondownload)
     pythonbutton.place(x=110, y=220)
     pythonbutton.configure(width=45, height=40)

     image2 = Image.open("Java-Logo.png")
     image2 = image2.resize((45, 40), Image.ANTIALIAS)
     image_tk2 = ImageTk.PhotoImage(image2)
     javabutton = ctk.CTkButton(dash, image=image_tk2, text="", compound=ctk.TOP,command=dd.javadownload)
     javabutton.place(x=210, y=220)
     javabutton.configure(width=45, height=20)

     image3 = Image.open("javascript-542e10ea6e.png")
     image3 = image3.resize((45, 40), Image.ANTIALIAS)
     image_tk2 = ImageTk.PhotoImage(image3)
     javascriptbutton = ctk.CTkButton(dash, image=image_tk2, text="", compound=ctk.TOP,command=dd.javascriptdownload)
     javascriptbutton.place(x=310, y=220)
     javascriptbutton.configure(width=45, height=20)

     image4 = Image.open("Typescript.png")
     image4 = image4.resize((45, 40), Image.ANTIALIAS)
     image_tk2 = ImageTk.PhotoImage(image4)
     typescriptbutton = ctk.CTkButton(dash, image=image_tk2, text="", compound=ctk.TOP,command=dd.typescriptdownload)
     typescriptbutton.place(x=410, y=220)
     typescriptbutton.configure(width=45, height=20)

     image5 = Image.open("Go-Logo_Blue.png")
     image5 = image5.resize((45, 40), Image.ANTIALIAS)
     image_tk2 = ImageTk.PhotoImage(image5)
     gobutton = ctk.CTkButton(dash, image=image_tk2, text="", compound=ctk.TOP)
     gobutton.place(x=510, y=220)
     gobutton.configure(width=45, height=20)

     response = requests.get(NEWS_API_URL, params=parameters)
     topheadlines=[]
     # Check if the request was successful (status code 200)
     if response.status_code == 200:
          data = response.json()
          # Get the articles from the response
          articles = data['articles']
          # Extract and print the headlines
          for article in articles[:6]:
               topheadlines.append(article['title'])
     else:
          print('Failed to fetch headlines:', response.status_code)

     headlineframe = ctk.CTkFrame(master=dash)
     headlineframe.place(x=80, y=330, relwidth=0.85, relheight=0.20)

     frameheading = ctk.CTkLabel(dash, text="Top Tech Headlines", font=("Helvetica", 22, "bold"))
     frameheading.place(x=90, y=290)

     heading1 = ctk.CTkLabel(dash, text=topheadlines[0], font=("Helvetica", 10, "bold"))
     heading1.place(x=90, y=350)

     heading2 = ctk.CTkLabel(dash, text=topheadlines[1], font=("Helvetica", 10, "bold"))
     heading2.place(x=90, y=370)

     heading3 = ctk.CTkLabel(dash, text=topheadlines[2], font=("Helvetica", 10, "bold"))
     heading3.place(x=90, y=390)

     heading4 = ctk.CTkLabel(dash, text=topheadlines[3], font=("Helvetica", 10, "bold"))
     heading4.place(x=90, y=410)

     createfolder(folder_name,parent_directory)






