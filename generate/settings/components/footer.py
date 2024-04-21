import customtkinter as ctk 
import os
import datetime

year = datetime.datetime.now()


print("Footer creation in process...")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

with open("project_name.txt", 'r') as file:
  project_name = file.read()
  print(project_name)

with open("project_desc.txt", 'r') as file:
  project_description = file.read()
  

component_name="footer"

component_dir = f"./{project_name}/src/components/"+component_name.lower().replace(" ", "-")
os.makedirs(component_dir, exist_ok=True)

def generate():
    
    theme=""
    text="white"
    if theme_var.get()==1:
        theme= "dark"
    if theme_var.get()==2:
        theme="light"
        text="dark" 
    if theme_var.get()==3:
        theme="primary" 
    if theme_var.get()==4:
        theme= "secondary"
    if theme_var.get()==5:
        theme="success"
        
    if theme_var.get()==6:
        theme="danger" 
    if theme_var.get()==7:
        theme="warning" 
        text="dark"
    if theme_var.get()==8:
        theme="info" 
        text="dark"
    
        
    # Get navbar elements
    products = products_entry.get().split(",") if products_entry.get() else []
    address = Address_entry.get()
    js = f'''import React from 'react';
            import {{ Container, Row, Col }} from 'react-bootstrap';

            const Footer = () => {{
            return (
            <footer className='bg-{theme} text-center text-lg-start text-{text} pt-5' data-bd-theme="{theme}">

                <section className=''>
                    <Container className='text-center text-md-start mt-5'>
                        <Row className='mt-3'>
                            <Col xs="9" sm="8" md="5" lg="6" xl="6" className='mx-auto mb-4'>
                                <h6 className='text-uppercase fw-bold mb-4'>
                                    {project_name}
                                </h6>
                                <p>
                                {project_description}
                                </p>
                            </Col>

                            <Col xs="8" sm="8" md="2" lg="2" xl="2"   className='mx-auto mb-4'>
                                <h6 className='text-uppercase fw-bold mb-4'>Products</h6>
                                {"".join([f'''<p>
                                    <a href='#!' className='text-reset'>
                                    {product}
                                    </a>
                                </p>''' for product in products])}    
                            </Col>

                            <Col xs="5" sm="5" md="5" lg="4" xl="3" className='mx-auto mb-md-0 mb-4'>
                                <h6 className='text-uppercase fw-bold mb-4'>Contact</h6>
                                <p>
                                {address}
                                </p>
                                <p>
                                    info@{project_name.lower()}.com
                                </p>
                            </Col>
                        </Row>
                    </Container>
                </section>

                <div className='text-center p-4'>
                    &copy; {year.year}: <a className='text-reset fw-bold' href=''>
                        www.{project_name.lower()}.com
                    </a>
                </div>
            </footer>
                );
            }}

        export default Footer;
        '''

    with open(f'{component_dir}/{component_name}.jsx', 'w') as file:
        file.write(js)
       
    app.destroy()
    
app = ctk.CTk() 
app.geometry("700x700") 
app.title("WEBKIT: Custom Component Generator")

label = ctk.CTkLabel(app,text="Footer generator") 
label.pack(padx=20, pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

theme_var = ctk.IntVar(value=0)
dark_checkbox = ctk.CTkRadioButton(master=frame, text="Dark", variable=theme_var, value=1)
dark_checkbox.grid(row=0,column=0, padx=20,pady=20)

light_checkbox = ctk.CTkRadioButton(master=frame, text="Light", variable=theme_var, value=2)
light_checkbox.grid(row=0,column=1, padx=20,pady=20)

blue_checkbox = ctk.CTkRadioButton(master=frame, text="Blue", variable=theme_var, value=3)
blue_checkbox.grid(row=0,column=2, padx=20,pady=20)

grey_checkbox = ctk.CTkRadioButton(master=frame, text="Grey", variable=theme_var, value=4)
grey_checkbox.grid(row=1,column=0, padx=20,pady=20)

green_checkbox = ctk.CTkRadioButton(master=frame, text="Green", variable=theme_var, value=5)
green_checkbox.grid(row=1,column=1, padx=20,pady=20)

red_checkbox = ctk.CTkRadioButton(master=frame, text="Red", variable=theme_var, value=6)
red_checkbox.grid(row=1,column=2, padx=20,pady=20)

yellow_checkbox = ctk.CTkRadioButton(master=frame, text="Yellow", variable=theme_var, value=7)
yellow_checkbox.grid(row=2,column=0, padx=20,pady=20)

Light_checkbox = ctk.CTkRadioButton(master=frame, text="Light Blue", variable=theme_var, value=8)
Light_checkbox.grid(row=2,column=1, padx=20,pady=20)


frame2 = ctk.CTkFrame(master=app) 
frame2.pack(pady=20,padx=40,fill='both',expand=True)

products_label = ctk.CTkLabel(master=frame2, text="Footer Products Elements (comma-separated):")
products_label.pack(padx=20, pady=20)
products_entry = ctk.CTkEntry(master=frame2, width=400, corner_radius=10,placeholder_text="e.g., 'Products1,Product2,etc'")
products_entry.pack(padx=20,pady=20)

Address_label = ctk.CTkLabel(master=frame2, text="Enter Address")
Address_label.pack(padx=20, pady=20)
Address_entry = ctk.CTkEntry(master=frame2, width=400, corner_radius=10,placeholder_text="e.g., A floor, B apartment, C Road")
Address_entry.pack(padx=20,pady=20)

button = ctk.CTkButton(master=app,text='Generate',command=generate) 
button.pack(padx=20,pady=20) 

app.mainloop()


with open(f"./{project_name}/src/app.js", "r") as file:
    lines = file.readlines()

    # Find the line where you want to insert the component
insert_index = None
for i, line in enumerate(lines):
    if "</div>" in line:
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