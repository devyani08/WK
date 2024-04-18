import os
import tkinter as tk
import customtkinter as ctk 
import shutil

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 
  
app = ctk.CTk() 
app.geometry("600x600") 
app.title("WEBKIT: Delete Component") 

component_name=""

with open("project_name.txt", 'r') as file:
  project_name = file.read()
  print(project_name)
def delete_component():
    global component_name
    component_name = component_name_entry.get()

    component_folder = f'./{project_name}/src/components/{component_name}'
    if not os.path.exists(component_folder):
        print(f"Component '{component_name}' does not exist.")
        return

    # Remove the component folder
    shutil.rmtree(component_folder)

    # Update app.js to remove the component import and usage
    app_js_path = f'./{project_name}/src/app.js'
    with open(app_js_path, 'r') as app_file:
        app_js = app_file.read()

    # Remove the import statement for the deleted component
    import_statement = f"import {component_name.title()} from './components/{component_name}/{component_name}'; \n"
    app_js = app_js.replace(import_statement, '')

    # Remove the component usage from the render method
    app_js = app_js.replace(f'<{component_name.title()} />', '')

    with open(app_js_path, 'w') as app_file:
        app_file.write(app_js)

    print(f"Component '{component_name}' deleted and app.js updated successfully.")
    app.destroy() 
 
label = ctk.CTkLabel(app,text="WEB KIT") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
label = ctk.CTkLabel(master=frame,text='Delete React Component') 
label.pack(pady=12,padx=10)

component_name_entry= ctk.CTkEntry(master=frame,placeholder_text="Component Name") 
component_name_entry.pack(pady=12,padx=10) 
  
button = ctk.CTkButton(master=frame,text='Delete Component ',command=delete_component) 
button.pack(pady=12,padx=10) 
app.mainloop()
