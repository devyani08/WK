import tkinter as tk
from tkinter import messagebox
import os
component_name=""
component_content=""
def generate_component():
    global component_name
    global component_content
    component_name = component_name_entry.get()
    component_content = component_content_text.get("1.0", "end-1c")  # Get content from the Text widget

    # Create the React component directory
    component_directory = os.path.join("src", "components", component_name)
    os.makedirs(component_directory)

    with open("project_name.txt", 'r') as file:
        project_name = file.read()
        print(project_name)

    cssdata=" "

    if component_name == "nav":
        data = f''' 
        import React from 'react';
        import {{ Navbar, Nav, Container }} from 'react-bootstrap';
        import 'bootstrap/dist/css/bootstrap.min.css';

        function {component_name}() {{
        return (
            <div>
            <Navbar bg="dark" variant="dark" expand="lg">
                <Container>
                    <Navbar.Brand href="/">{project_name}</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="ml-auto">
                        <Nav.Link href="/about">About Us</Nav.Link>
                        <Nav.Link href="/contact">Contact Us</Nav.Link>
                    </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            </div>
            );
        }}
        export default {component_name};
        '''

    elif component_name=="hero":
        data = f""" 
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
        
        cssdata=""" 
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

    else:    
        data = f"""
        import React from 'react';

        function {component_name}() {{
            return (
                <div>
                    {component_content}
                </div>
                );
            }}
            
        export default {component_name};
        """
    # Create the React component JavaScript file
    with open(os.path.join(component_directory, f"{component_name}.js"), "w") as file:
        file.write(data)
    with open(os.path.join(component_directory, f"{component_name}.css"), "w") as file:
        file.write(cssdata)

    messagebox.showinfo("Component Created", f"React component '{component_name}' has been created!")
    root.destroy()
    
# Create the main window
root = tk.Tk()
root.title("React Component Generator")

# Component Name Label and Entry
component_name_label = tk.Label(root, text="Component Name:")
component_name_label.pack()
component_name_entry = tk.Entry(root)
component_name_entry.pack()

# Component Content Label and Textbox
component_content_label = tk.Label(root, text="Component Content:")
component_content_label.pack()
component_content_text = tk.Text(root, height=5, width=40)
component_content_text.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Component", command=generate_component)
generate_button.pack()

root.mainloop()

if component_name== "nav":
    with open("src/app.js", "r") as file:
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
        with open("src/app.js", "w") as file:
            file.writelines(lines)
        print(f"Inserted {component_name} into app.js.")
    else:
        print("Error: Could not find the insertion point in app.js.")

else:
    # Read the app.js file
    with open("src/app.js", "r") as file:
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
        with open("src/app.js", "w") as file:
            file.writelines(lines)
        print(f"Inserted {component_name} into app.js.")
    else:
        print("Error: Could not find the insertion point in app.js.")


with open("src/app.js", 'r') as file:
    old_content = file.read()


with open("src/app.js", 'w') as file:
    new_data = f"import {component_name.title()} from './components/{component_name}/{component_name}'; \n"
    file.write(new_data)
    file.write(old_content)
