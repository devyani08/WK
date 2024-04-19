import customtkinter as ctk 
import os
import subprocess
import sys
component_name=""
component_description=""

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

########################### DONE METHOD #####################################

def done():
    app.destroy()

############################# NAV GENERATOR ####################################

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

################################ LANDING PAGE GENERATOR ###########################################


def landingPage_generator():
    global component_name
    component_name = "landingPage"
    
    def run_another_file(file_path):
        try:
            subprocess.Popen([sys.executable, file_path])
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error occurred: {e}")

    run_another_file("generate/settings/components/landingpage.py")
  
############################# FORM GENERATOR ####################################
  
def form_generator():
    global component_name
    component_name = "form"
    
    def run_another_file(file_path):
        try:
            subprocess.Popen([sys.executable, file_path])
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error occurred: {e}")

    run_another_file("generate/settings/components/form.py")


############################# FOOTER GENERATOR ####################################

def footer_generator():
    global component_name
    component_name = "footer"
    
    def run_another_file(file_path):
        try:
            subprocess.Popen([sys.executable, file_path])
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error occurred: {e}")

    run_another_file("generate/settings/components/footer.py")

################################ GUI SETUP ###########################################

app = ctk.CTk() 
app.geometry("600x600") 
app.title("WEBKIT: Custom Component Generator")

label = ctk.CTkLabel(app,text="WEB KIT") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

navButton = ctk.CTkButton(master=frame,text='Nav',command=nav_generator) 
navButton.grid(row=0,column=0,pady=20,ipady=5,padx=20) 

landingPageButton = ctk.CTkButton(master=frame,text='Landing Page',command=landingPage_generator) 
landingPageButton.grid(row=0,column=1,pady=12,ipady=5,padx=10) 

formButton = ctk.CTkButton(master=frame,text='Forms',command=form_generator) 
formButton.grid(row=1,column=0,pady=12,ipady=5,padx=10) 

footerButton = ctk.CTkButton(master=frame,text='Footer',command=footer_generator) 
footerButton.grid(row=0,column=3,pady=12,ipady=5,padx=10) 

frame2 = ctk.CTkFrame(master=app) 
frame2.pack(pady=20,padx=40,fill='both')

doneButton = ctk.CTkButton(master=frame2,text='Done',command=done) 
doneButton.pack(pady=20,padx=40,ipady=5) 

app.mainloop()