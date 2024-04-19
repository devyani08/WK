import customtkinter as ctk 
import os
import subprocess
import sys

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
    theme=""
    offCanvasCode=""
    sticky=""
    fixed=""
    if theme_var.get()==1:
        theme="dark"
    if theme_var.get()==2:
        theme="light"
    if theme_var.get()==3:
        theme= "primary"
    if offCanvas_var.get():
        offCanvasCode = f"""
        <Navbar.Offcanvas 
            bg="{theme if theme else ""}"  data-bs-theme="{theme if theme else ""}"
            id="offcanvasNavbar-expand-lg"
            aria-labelledby="offcanvasNavbarLabel-expand-lg"
            placement="end"
        >
        <Offcanvas.Header closeButton>
            <Offcanvas.Title id="offcanvasNavbarLabel-expand-lg">
                {project_name}
            </Offcanvas.Title>
            </Offcanvas.Header>
        <Offcanvas.Body>
        """
    if fixed_var.get()==2:
        fixed = "bottom"
    if fixed_var.get()==1:
        fixed = "top"
        
    if sticky_var.get()==1:
        sticky = "top"
    if sticky_var.get()==2:
        sticky = "bottom"
    if logo_var.get():
        def run_another_file(file_path):
            try:
                subprocess.Popen([sys.executable, file_path])
            except FileNotFoundError:
                print(f"Error: File '{file_path}' not found.")
            except Exception as e:
                print(f"Error occurred: {e}")
        run_another_file("generate/settings/components/logoSelector.py")

        
    # Get navbar elements
    elements = elements_entry.get().split(",") if elements_entry.get() else []

    js = f'''
    import React from 'react';
    {"".join("import Offcanvas from 'react-bootstrap/Offcanvas';" if offCanvasCode else "") }
    {"".join("import logo from '../../images/logo.png';" if logo_var.get() else "") }
    import {{ Navbar, Nav ,Container, NavDropdown }} from 'react-bootstrap';
    import 'bootstrap/dist/css/bootstrap.min.css';

    const MyNav = () => {{
    return (
        <Navbar expand="lg" bg="{theme}" fixed="{fixed}" sticky="{sticky}" data-bs-theme="{theme}"> 
        <Navbar.Brand>
        {"".join(f'''<img
            src={{logo}}
            width="35"
            height="35"
            className="d-inline-block align-top rounded-3 mx-4 fluid"
            alt="React Bootstrap logo"
            />''' if logo_var.get() else "") }
        
            {project_name}</Navbar.Brand>  
        
        <Navbar.Toggle aria-controls= 'basic-navbar-nav' />
        
        {"".join(str(offCanvasCode) if offCanvasCode else "") }
        
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
            {"".join([f'<Nav.Link href="/{item}">{item}</Nav.Link>   ' for item in elements])}
            </Nav>
        </Navbar.Collapse>
        {"".join("</Offcanvas.Body> </Navbar.Offcanvas>" if offCanvasCode else "") }
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
label.pack(padx=20, pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

theme_var = ctk.IntVar(value=0)
dark_checkbox = ctk.CTkRadioButton(master=frame, text="Dark", variable=theme_var, value=1)
dark_checkbox.grid(row=0,column=0, padx=20,pady=20)

light_checkbox = ctk.CTkRadioButton(master=frame, text="Light", variable=theme_var, value=2)
light_checkbox.grid(row=0,column=1, padx=20,pady=20)

primary_checkbox = ctk.CTkRadioButton(master=frame, text="Primary",variable=theme_var, value=3)
primary_checkbox.grid(row=0,column=2, padx=20,pady=20)

offCanvas_var = ctk.IntVar()
offCanvas_checkbox = ctk.CTkCheckBox(master=frame, text="OffCanvas", variable=offCanvas_var)
offCanvas_checkbox.grid(row=3,column=0, padx=20,pady=20)

logo_var = ctk.IntVar()
logo_checkbox = ctk.CTkCheckBox(master=frame, text="Logo", variable=logo_var)
logo_checkbox.grid(row=3,column=1, padx=20,pady=20)

sticky_var = ctk.IntVar(value=0)
stickybottom_checkbox = ctk.CTkRadioButton(master=frame, text="Sticky Bottom", variable=sticky_var,value=2)
stickybottom_checkbox.grid(row=1,column=1, padx=20,pady=20)

stickytop_checkbox = ctk.CTkRadioButton(master=frame, text="Sticky Top", variable=sticky_var,value=1)
stickytop_checkbox.grid(row=1,column=0, padx=20,pady=20)

fixed_var = ctk.IntVar(value=0)
fixedtop_checkbox = ctk.CTkRadioButton(master=frame, text="Fixed Top", variable=fixed_var, value=1)
fixedtop_checkbox.grid(row=2,column=0, padx=20,pady=20)

fixedbottom_checkbox = ctk.CTkRadioButton(master=frame, text="Fixed bottom", variable=fixed_var,value=2)
fixedbottom_checkbox.grid(row=2,column=1, padx=20,pady=20)

frame2 = ctk.CTkFrame(master=app) 
frame2.pack(pady=20,padx=40,fill='both',expand=True)

elements_label = ctk.CTkLabel(master=frame2, text="Navbar Elements (comma-separated):")
elements_label.pack(padx=20, pady=20)
elements_entry = ctk.CTkEntry(master=frame2, width=400, corner_radius=10,placeholder_text="e.g., 'Home, About Us, Contact'")
elements_entry.pack(padx=20,pady=20)

button = ctk.CTkButton(master=app,text='Generate',command=generate) 
button.pack(padx=20,pady=20) 

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