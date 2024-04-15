import customtkinter as ctk 
import os

print("nav creation in process...")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

with open("project_name.txt", 'r') as file:
  project_name = file.read()
  print(project_name)

component_name="nav"

component_dir = f"./{project_name}/src/components/"+component_name.lower().replace(" ", "-")
os.makedirs(component_dir, exist_ok=True)

def generate():
    position = ""
    theme=""
    if dark_var.get():
        theme= "dark"
    if light_var.get():
        theme="light"
    if primary_var.get():
        theme= "primary"
    if stickytop_var.get():
        position = "sticktop"
    if stickybottom_var.get():
        position = "sticky-bottom"
    
    # Get navbar elements
    elements = elements_entry.get().split(",") if elements_entry.get() else []

    js = f'''import React from 'react';
    import logo from '../../images/logo.png';
    import {{ Navbar, Nav ,Container, NavDropdown }} from 'react-bootstrap';
    import 'bootstrap/dist/css/bootstrap.min.css';

    const MyNav = () => {{
    return (
        <Navbar expand="lg" bg="{theme}" data-bs-theme="{theme}"> 
        <Navbar.Brand>
        <img
            src={{logo}}
            width="35"
            height="35"
            className="d-inline-block align-top rounded-3 mx-4 fluid"
            alt="React Bootstrap logo"
            />
            {project_name}</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
            {"".join([f'<Nav.Link href="/{item}">{item}</Nav.Link> \n' for item in elements])}
            </Nav>
        </Navbar.Collapse>
        </Navbar>
    );
    }}

    export default MyNav;
    '''

    with open(f'{component_dir}/{component_name}.jsx', 'w') as file:
        file.write(js)
        
    app.destroy()
    
app = ctk.CTk() 
app.geometry("600x600") 
app.title("WEBKIT: Custom Component Generator")

label = ctk.CTkLabel(app,text="Nav generator") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

dark_var = ctk.IntVar()
dark_checkbox = ctk.CTkCheckBox(master=frame, text="Dark", variable=dark_var)
dark_checkbox.pack(pady=12,ipady=5,padx=10)

light_var = ctk.IntVar()
light_checkbox = ctk.CTkCheckBox(master=frame, text="Light", variable=light_var)
light_checkbox.pack(pady=12,ipady=5,padx=10)

primary_var = ctk.IntVar()
primary_checkbox = ctk.CTkCheckBox(master=frame, text="Primary", variable=primary_var)
primary_checkbox.pack(pady=12,ipady=5,padx=10)

stickytop_var = ctk.IntVar()
stickytop_checkbox = ctk.CTkCheckBox(master=frame, text="Stick Top", variable=stickytop_var)
stickytop_checkbox.pack(pady=12,ipady=5,padx=10)


stickybottom_var = ctk.IntVar()
stickybottom_checkbox = ctk.CTkCheckBox(master=frame, text="Sticky Bottom", variable=stickybottom_var)
stickybottom_checkbox.pack(pady=12,ipady=5,padx=10)

elements_label = ctk.CTkLabel(master=frame, text="Navbar Elements (comma-separated):")
elements_label.pack(pady=12,ipady=5,padx=10)
elements_entry = ctk.CTkEntry(master=frame)
elements_entry.pack(pady=12,ipady=5,padx=10)

button = ctk.CTkButton(master=frame,text='Generate',command=generate) 
button.pack(pady=12,ipady=5,padx=10) 

app.mainloop()

with open(f"./{project_name}/src/app.js", "r") as file:
    lines = file.readlines()
    
insert_index = None

for i, line in enumerate(lines):
    if "<Routes>" in line:
        insert_index = i
        break
if insert_index is not None:
    # Insert the new component content
    lines.insert(insert_index, f"      <{component_name.title()} />\n")

    # Write the modified content back to app.js
    with open(f"./{project_name}/src/app.js", "w") as file:
        file.writelines(lines)
    print(f"Inserted {component_name} into app.js.")
else:
    print("Error: Could not find the insertion point in app.js.")

with open(f"./{project_name}/src/app.js", 'r') as file:
    old_content = file.read()

with open(f"./{project_name}/src/app.js", 'w') as file:
    new_data = f"import {component_name.title()} from './components/{component_name}/{component_name}'; \n"
    file.write(new_data)
    file.write(old_content)