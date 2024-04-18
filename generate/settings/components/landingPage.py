import customtkinter as ctk 
import os
import subprocess
import sys

print("Landing Page in progress...")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

with open("project_name.txt", 'r') as file:
  project_name = file.read()
  print(project_name)

def generate():
    global component_name
    theme=""
    if theme_var.get()==1:
        theme= "dark"
    if theme_var.get()==2:
        theme="light" 
    if theme_var.get()==3:
        theme="primary" 
    # Get navbar elements
    if content_var.get()==1: 
       
      component_name="carousel"
      component_dir = f"./{project_name}/src/components/"+component_name.lower().replace(" ", "-")
      os.makedirs(component_dir, exist_ok=True)
      
      def run_another_file(file_path):
        try:
            subprocess.Popen([sys.executable, file_path])
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error occurred: {e}")
            
      run_another_file("generate/settings/components/CarouselImageSelector.py")
        
      js = f'''import React from 'react';
        import 'bootstrap/dist/css/bootstrap.min.css';
        import Carousel from 'react-bootstrap/Carousel';
        import image1 from '../../images/CImage1.png';
        import image2 from '../../images/CImage2.png';
        import image3 from '../../images/CImage3.png';
        
        const Carousel = () => {{
        return (
            <Carousel className='container-lg p-5 w-50-lg'  fade h-80 bg="{theme}" data-bs-theme="{theme}">
          <Carousel.Item>
            <img
              className="container-lg d-block img-fluid"
              src={{image1}}
              style={{{{ width: '90vw', height: '80vh' }}}}
              alt="First slide"
              
            />
            <Carousel.Caption>
              <h3>First slide label</h3>
              <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
            </Carousel.Caption>
          </Carousel.Item>
          
          <Carousel.Item>
          <img
              className="container-lg d-block img-fluid"
              src={{image2}}
              style={{{{ width: '90vw', height: '80vh' }}}}
              alt="Second slide"
              
            />
            <Carousel.Caption>
              <h3>Second slide label</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </Carousel.Caption>
          </Carousel.Item>
          
          <Carousel.Item>
          <img
              className="container-lg d-block img-fluid"
              src={{image3}}
              style={{{{ width: '90vw', height: '80vh' }}}}
              alt="Third slide"
              
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

        export default Carousel;
        '''
      with open(f'{component_dir}/{component_name}.jsx', 'w') as file:
          file.write(js)
      app.destroy()
      
    if content_var.get()==2: 
       
      component_name="testimony"
      component_dir = f"./{project_name}/src/components/"+component_name.lower().replace(" ", "-")
      os.makedirs(component_dir, exist_ok=True)
      
      def run_another_file(file_path):
        try:
            subprocess.Popen([sys.executable, file_path])
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error occurred: {e}")
            
      run_another_file("generate/settings/components/TestimonyImageSelector.py")
        
      js = f"""import React from 'react';
        import 'bootstrap/dist/css/bootstrap.min.css';
        import image1 from '../../images/TImage1.png';
        import image2 from '../../images/TImage2.png';
        import image3 from '../../images/TImage3.png';
        import image4 from '../../images/TImage4.png';
        import Ratio from 'react-bootstrap/Ratio';
        import {{ Container, Row, Col, Card, Image }} from 'react-bootstrap';

        const Testimony = () => {{
        return (
          <Card className='bg-{theme}' data-bs-theme="{theme}">
            <Container>
            <Card.Body>
          <Row className="justify-content-center text-center mt-5">
              <h1>Testimonials</h1>
              <h2>Customer Experiences and Feedback of {project_name}</h2>
          </Row>
          <Row className='justify-content-center'>
          
          <Col sm={{3}} md={{2}}>
            <Card className='w-50 p-2 rounded-5 mt-5' >
                  <Ratio aspectRatio="1x1">
                    <Image src={{image1}} roundedCircle />
            </Ratio>
            </Card>
          </Col>
          <Col sm={{3}} >
            <Card className='w-50 p-2 rounded-5 mt-5'  >
            <Ratio aspectRatio="1x1">
                    <Image src={{image2}} roundedCircle />
            </Ratio>          </Card>
          </Col>
          <Col sm={{3}} >
            <Card className='w-50 p-2 rounded-5 mt-5' >
            <Ratio aspectRatio="1x1">
                    <Image src={{image3}} roundedCircle />
            </Ratio>          </Card>
          </Col>
          <Col sm={{3}} md={{2}}>
            <Card className='w-50 p-2 rounded-5 mt-5'>
            <Ratio aspectRatio="1x1">
                    <Image src={{image4}} roundedCircle />
            </Ratio>          
          </Card>
          </Col>
          </Row>
          
          <Row>
            <Col md={{6}}>
              <Card className='w-75 rounded-5 m-5'>
              <Card.Body>
                  <Card.Title>Ron</Card.Title>
                  <Card.Subtitle>Designer</Card.Subtitle>
                  <Card.Text>Insight helped us strengthen our business' online reputation in an incredible way! Thanks to their Al-powered analytics, we better understood our target audience and developed more effective communication strategies.</Card.Text>
                </Card.Body>
                <Card.Footer>
                <Card className='w-25 p-2 rounded-5' roundedCircle>
                <Ratio aspectRatio="1x1">
                    <Image className='img-fluid' src={{image2}} roundedCircle />
                </Ratio>
                </Card>
                </Card.Footer>
              </Card>
            </Col>
            <Col md={{6}}>
              <Card className='w-75 rounded-5 m-5'>
                <Card.Body>
                  <Card.Title>Harry Potter</Card.Title>
                  <Card.Subtitle>Designer</Card.Subtitle>
                  <Card.Text>Insight helped us strengthen our business' online reputation in an incredible way! Thanks to their Al-powered analytics, we better understood our target audience and developed more effective communication strategies.</Card.Text>
                </Card.Body>
                <Card.Footer>
                <Card className='w-25 p-2 rounded-5' roundedCircle>
                <Ratio aspectRatio="1x1">
                    <Image className='img-fluid' src={{image3}} roundedCircle />
                </Ratio>
                </Card>
                </Card.Footer>
              </Card>
            </Col>
          </Row>
            </Card.Body>
            </Container>
        </Card>
        );
        }}

        export default Testimony;
        """
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

primary_checkbox = ctk.CTkRadioButton(master=frame, text="Primary", variable=theme_var, value=3)
primary_checkbox.grid(row=0,column=2, padx=20,pady=20)

content_var = ctk.IntVar(value=0)
carouselButton = ctk.CTkRadioButton(master=frame,text='Carousel',variable=content_var, value=1) 
carouselButton.grid(row=1,column=0, padx=20,pady=20)

testimonyButton = ctk.CTkRadioButton(master=frame,text='Testimony',variable=content_var,value=2) 
testimonyButton.grid(row=1,column=1, padx=20,pady=20)

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