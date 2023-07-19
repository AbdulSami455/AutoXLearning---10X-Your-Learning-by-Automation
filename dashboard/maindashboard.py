import customtkinter as ctk
def dashboardf():
     dash=ctk.CTk()
     dash.geometry("1000x600")
     search=ctk.CTkEntry(dash,width=500,height=10)
     search.place(x=80,y=20)