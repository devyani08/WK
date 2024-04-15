import customtkinter as ctk 
import os
import subprocess
import sys
component_name=""
component_description=""

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

def done():
    app.destroy()

def nav_generator():
    global component_name
    component_name = "nav"
    
    def run_another_file(file_path):
        try:
            subprocess.Popen([sys.executable, file_path])
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error occurred: {e}")

    run_another_file("generate/settings/components/nav.py")

app = ctk.CTk() 
app.geometry("600x600") 
app.title("WEBKIT: Custom Component Generator")

label = ctk.CTkLabel(app,text="WEB KIT") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

navButton = ctk.CTkButton(master=frame,text='Nav',command=nav_generator) 
navButton.pack(pady=12,ipady=5,padx=10) 

doneButton = ctk.CTkButton(master=frame,text='Done',command=done) 
doneButton.pack(pady=12,ipady=5,padx=10) 

app.mainloop()