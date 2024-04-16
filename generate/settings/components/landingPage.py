import customtkinter as ctk 
import os

print("Landing Page in progress...")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

with open("project_name.txt", 'r') as file:
  project_name = file.read()
  print(project_name)

component_name="landingpage"

component_dir = f"./{project_name}/src/components/"+component_name.lower().replace(" ", "-")
os.makedirs(component_dir, exist_ok=True)

def generate():
    theme=""
    if theme_var.get()==1:
        theme= "dark"
    if theme_var.get()==2:
        theme="light" 
    # Get navbar elements
    
    js = f'''import React from 'react';
    import logo from '../../images/logo.png';
    import {{ Navbar, Nav ,Container, NavDropdown }} from 'react-bootstrap';
    import 'bootstrap/dist/css/bootstrap.min.css';
    import Carousel from 'react-bootstrap/Carousel';
    import image1 from '../../images/image3.png';
    import image2 from '../../images/image2.jpeg';
    import image3 from '../../images/image1.webp';
    
    const LandingPage = () => {{
    return (
        <Carousel fade bg="{theme}" data-bs-theme="{theme}">
      <Carousel.Item>
        <img
          className="d-block w-100"
          src={{image1}}
          alt="First slide"
          fluid
        />
        <Carousel.Caption>
          <h3>First slide label</h3>
          <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
        </Carousel.Caption>
      </Carousel.Item>
      
      <Carousel.Item>
      <img
          className="d-block w-100"
          src={{image2}}
          alt="Second slide"
          fluid
        />
        <Carousel.Caption>
          <h3>Second slide label</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </Carousel.Caption>
      </Carousel.Item>
      
      <Carousel.Item>
      <img
          className="d-block w-100"
          src={{image3}}
          alt="Third slide"
          fluid
        />
        <Carousel.Caption>
          <h3>Third slide label</h3>
          <p>
            Praesent commodo cursus magna, vel scelerisque nisl consectetur.
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
    );
    }}

    export default LandingPage;
    '''

    with open(f'{component_dir}/{component_name}.jsx', 'w') as file:
        file.write(js)
        
    app.destroy()
    
app = ctk.CTk() 
app.geometry("600x600") 
app.title("WEBKIT: Custom Component Generator")

label = ctk.CTkLabel(app,text="Landing Page Generator") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

theme_var = ctk.IntVar(value=0)
dark_checkbox = ctk.CTkRadioButton(master=frame, text="Dark", variable=theme_var, value=1)
dark_checkbox.grid(row=0,column=0, padx=20,pady=20)

light_checkbox = ctk.CTkRadioButton(master=frame, text="Light", variable=theme_var, value=2)
light_checkbox.grid(row=0,column=1, padx=20,pady=20)

carousel_var = ctk.IntVar()
carouselButton = ctk.CTkCheckBox(master=frame,text='Carousel',variable=carousel_var) 
carouselButton.grid(row=1,column=0, padx=20,pady=20)

button = ctk.CTkButton(master=app,text='Generate',command=generate) 
button.pack(pady=12,ipady=5,padx=10) 

app.mainloop()

with open(f"./{project_name}/src/app.js", "r") as file:
    lines = file.readlines()

    # Find the line where you want to insert the component
insert_index = None
for i, line in enumerate(lines):
    if "</>" in line:
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