import os
import shutil
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

with open("./project_name.txt", 'r') as file:
      project_name = file.read()

# Counter for naming images
imageCount = 1

def open_file_dialog():
    # Open file dialog to select multiple image files
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.webp")])
    if file_paths:
        entry.delete(0, "end")  # Clear the entry field
        entry.insert(0, ", ".join(file_paths))  # Set the file paths

def save_images_to_folder():
    global imageCount
    image_paths = entry.get().split(", ")
    folder_path = "generate/settings/images/"  # Fixed folder path
    
    # Remove the existing destination directory if it exists
    dest_dir = f'{project_name}/src/images/'
    if os.path.exists(dest_dir):
        try:
            shutil.rmtree(dest_dir)
        except Exception as e:
            print(f"Error removing existing destination directory: {e}")
    
    for image_path in image_paths:
        if image_path:
            try:
                # Open the image file
                image = Image.open(image_path)
                # Construct the filename
                filename = f"CImage{imageCount}.png"
                # Construct the path to save the image
                save_path = os.path.join(folder_path, filename)
                # Save the image to the folder
                image.save(save_path)
                status_label.configure(text=f"Image saved to {save_path}")
                imageCount += 1
            except Exception as e:
                status_label.configure(text=f"Error occurred: {e}")
        else:
            status_label.configure(text="Please select image files")
    
    app.destroy()

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 

# Create main window
app = ctk.CTk()
app.geometry("600x600") 
app.title("Carousel Image File Input")

# Create a ctk frame
label = ctk.CTkLabel(app,text="Select image files for Carousel") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
# Create widgets

label = ctk.CTkLabel(master=frame,text='Select images in png, jpeg, webp format only') 
label.pack(pady=12,padx=10)

entry= ctk.CTkEntry(master=frame,placeholder_text="Example: C://Desktop/image1.jpeg, C://Desktop/image2.png") 
entry.pack(pady=12,padx=10) 

browse_button = ctk.CTkButton(master=frame, text="Upload", command=open_file_dialog)
browse_button.pack(pady=12,padx=10)

save_button = ctk.CTkButton(master=frame, text="Save Images", command=save_images_to_folder)
save_button.pack(pady=12,padx=10)

status_label = ctk.CTkLabel(master=frame, text="")
status_label.pack(pady=12,padx=10)

# Start the GUI
app.mainloop()


source_dir = 'generate/settings/images'
dest_dir = f'{project_name}/src/images/'

try:
  # Copy the entire contents of the source directory to the destination directory
  shutil.copytree(source_dir, dest_dir)
  print(f"Images copied from '{source_dir}' to '{dest_dir}' successfully.")
except Exception as e:
  print(f"Error copying images: {e}")
