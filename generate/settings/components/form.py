import customtkinter as ctk 
import os

print("Form creation in process...")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

component_name = ""
with open("project_name.txt", 'r') as file:
    project_name = file.read()
    print(project_name)


def generate():
    global component_name
    theme = ""
    text="dark"
    form_type = ""
    if theme_var.get()==1:
        theme= "dark"
        text="light"
    if theme_var.get()==2:
        theme="light" 
    if theme_var.get()==3:
        theme="primary" 
    if theme_var.get()==4:
        theme= "secondary"
    if theme_var.get()==5:
        theme="success"
        text="light" 
    if theme_var.get()==6:
        theme="danger" 
    if theme_var.get()==7:
        theme="warning" 
    if theme_var.get()==8:
        theme="info" 
    
    
    if login_var.get():
        form_type = "login"
    elif registration_var.get():
        form_type = "registration"

    elements = elements_entry.get().split(",") if elements_entry.get() else []

    
    js = f"""
    import React from 'react';
    import {{ Form, Button,Container, Card}} from 'react-bootstrap';
    import 'bootstrap/dist/css/bootstrap.min.css';

    const MyForm = () =>{{
        return (
        <div className=" p-5 m-4 ">
        <Container style={{{{maxWidth:'55vw'}}}} >
            <Card className="bg-{theme} text-{text} p-5 rounded-4 " >
            <Form expand="lg">
            <h2>{form_type.title()} Form</h2>
            {"".join([f'''<Form.Group className="mb-3" controlId="formBasic{item}">
                <Form.Label>{item}</Form.Label>
                <Form.Control type="{item}" placeholder="Enter {item}" />
            </Form.Group>''' for item in elements])}
            
            <Button variant="{text}"  type="submit" >Submit</Button>
            </Form>
        </Card>
        </Container>
        </div>
        );
    }}

    export default MyForm;
    """

    component_name = f"{form_type}form"

    component_dir = f"./{project_name}/src/components/"+component_name.lower().replace(" ", "-")
    os.makedirs(component_dir, exist_ok=True)

    with open(f'{component_dir}/{component_name}.jsx', 'w') as file:
        file.write(js)
        
    app.destroy()

app = ctk.CTk() 
app.geometry("700x700") 
app.title("WEBKIT: Custom Form Generator")

label = ctk.CTkLabel(app,text="Form generator") 
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

login_var = ctk.IntVar()
login_checkbox = ctk.CTkCheckBox(master=frame, text="Login Form", variable=login_var)
login_checkbox.grid(row=3,column=0, padx=20,pady=20)

registration_var = ctk.IntVar()
registration_checkbox = ctk.CTkCheckBox(master=frame, text="Registration Form", variable=registration_var)
registration_checkbox.grid(row=3,column=1, padx=20,pady=20)

frame2 = ctk.CTkFrame(master=app) 
frame2.pack(pady=20,padx=40,fill='both',expand=True)


elements_label = ctk.CTkLabel(master=frame2, text="Form Elements (comma-separated):")
elements_label.pack(padx=20, pady=20)
elements_entry = ctk.CTkEntry(master=frame2, width=300, corner_radius=5,placeholder_text="e.g., 'Name, Email, Password'")
elements_entry.pack(padx=20,pady=20)

button = ctk.CTkButton(master=app,text='Generate',command=generate) 
button.pack(padx=20,pady=20) 

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