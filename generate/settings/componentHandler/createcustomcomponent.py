import customtkinter as ctk 
import os
component_name=""
component_description=""

with open("project_name.txt", 'r') as file:
  project_name = file.read()
  print(project_name)

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

def generate_component():
    global component_name
    global component_description
    component_name = component_name_entry.get()
    component_description = component_description_entry.get().split(',')
    app.destroy()

app = ctk.CTk() 
app.geometry("500x400") 
app.title("WEBKIT: Custom Component Generator")

label = ctk.CTkLabel(app,text="WEB KIT") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

label3 = ctk.CTkLabel(master=frame,text="Field Items ( comma-separated ):") 
label3.pack(pady=12,ipady=5,padx=10) 

component_name_entry= ctk.CTkEntry(master=frame,placeholder_text="Component Name") 
component_name_entry.pack(pady=12, ipady=5,padx=10) 

 
component_description_entry= ctk.CTkEntry(master=frame,placeholder_text="Component Fields") 
component_description_entry.pack(pady=12,ipady=5,padx=10) 
button = ctk.CTkButton(master=frame,text='Generate Component',command=generate_component) 
button.pack(pady=12,ipady=5,padx=10) 
app.mainloop()


component_dir = f"./{project_name}/src/components/"+component_name.lower().replace(" ", "-")
os.makedirs(component_dir, exist_ok=True)

if component_name == 'nav':
  nav_js = f'''import React from 'react';
    import {{ Navbar, Nav }} from 'react-bootstrap';
    import 'bootstrap/dist/css/bootstrap.min.css';

    const MyNav = () => {{
      return (
        <Navbar bg="light" expand="lg">
          <Navbar.Brand>{project_name}</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              {"".join([f'<Nav.Link href="#">{item}</Nav.Link>' for item in component_description])}
            </Nav>
          </Navbar.Collapse>
        </Navbar>
      );
    }}

    export default MyNav;
    '''

  with open(f'{component_dir}/{component_name}.jsx', 'w') as nav_file:
    nav_file.write(nav_js)
elif component_name=="hero":
  hero_js = f""" 
  import React from 'react';
  import {{ Container, Row, Col }} from 'react-bootstrap';
  import 'bootstrap/dist/css/bootstrap.min.css';
  import image from '../../images/image3.png';
  import image2 from '../../images/image2.jpeg';
  import image3 from '../../images/image1.webp';
  import './{component_name}.css';
  const hero = () =>{{
  return (
      <div className="hero-section overlay2">
      <Container fluid>
          <Row>
          <Col className="image-container">
              <img src={{image}} alt="Image 1" className="image image1" />
              <img src={{image2}} alt="Image 2" className="image image2" />
              <img src={{image3}} alt="Image 3" className="image image3" />

              <div className="overlay"></div>
          </Col>

          <Col className="text-container">
              <h1 className="heading">hero</h1>
              <p className="subheading">hero section is here</p>
          </Col>
          </Row>
      </Container>
      </div>
      );
      }};
      export default {component_name};
      """
  hero_css=""" 
  .hero-section {
  background-color: #333; 
  color: white; 
  
  padding: 200px 0; 
  }

  .image-container {
  position: relative;
  }

  .image {
  position: absolute;
  width: 50%;
  height: 100%;
  object-fit: cover;
  z-index: -2;
  }

  .image2{
  top:100px;
  left: 100px;
  z-index: 0;
  } 
  .image1{
  z-index: 1;
  }
  .image3{
      z-index: 0;
      bottom:100px;
      left: 100px;;
  }
  .overlay {
  position: absolute;
  top: 0;
  left: 5%;
  width: 45%; 
  height: 100%;
  z-index: 2;
  background-color: rgba(96, 96, 96, 0.5); 
  }

  .text-container {
  padding: 20px; 
  }

  .heading {
  font-size: 36px; 
  margin-bottom: 10px;
  }

  .subheading {
  font-size: 24px; 
  }
  .overlay2 {
      width: 100%; 
      height: 100%;
      background-image: url("../../images/image2.jpeg"); 
      background-repeat: no-repeat;
      background-size: cover;
      }

  """
  with open(f'{component_dir}/{component_name}.jsx', 'w') as hero_file:
    hero_file.write(hero_js)
  with open(f'{component_dir}/{component_name}.css', 'w') as hero_file:
    hero_file.write(hero_css)

elif component_name == 'footer':
  pass


#   form_js = f'''import React from 'react';
# import {{ Form, Button }} from 'react-bootstrap';
# import 'bootstrap/dist/css/bootstrap.min.css';
# const MyForm = () => {{
#   return (
#     <Form>
#   {"".join([f'''
#   <Form.Group controlId="formBasic{field.capitalize()}">
#     <Form.Label>{field.capitalize()}</Form.Label>
#     <Form.Control type="text" placeholder={{"Enter {field}"}} />
#   </Form.Group>''' for field in component_description])}
  
#       <Button variant="primary" type="submit">
#         Submit
#       </Button>
#     </Form>
#   );
# }}

# export default MyForm;
# '''

#   with open(f'{component_dir}/{component_name}.jsx', 'w') as form_file:
#     form_file.write(form_js)


if component_name== "nav":
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

else:
    # Read the app.js file
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
