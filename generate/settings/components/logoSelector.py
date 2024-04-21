import os
import shutil
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

def open_file_dialog():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.webp")])
    if file_path:
        entry.delete(0, "end")  # Clear the entry field
        entry.insert(0, file_path)  # Set the file path

def save_image_to_folder():
    image_path = entry.get()
    folder_path = "generate/settings/images/"  # Fixed folder path
    filename = "logo.png"
    # Check if the image path is provided
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    if image_path and filename:
        try:
            # Open the image file
            image = Image.open(image_path)
            # Construct the path to save the image
            save_path = os.path.join(folder_path, filename)
            # Save the image to the folder
            image.save(save_path)
            status_label.configure(text=f"Image saved to {save_path}")
        except Exception as e:
            status_label.configure(text=f"Error occurred: {e}")
    else:
        status_label.configure(text="Please select an image file")
    app.destroy()
    
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 
  
# Create main window
app = ctk.CTk()
app.geometry("700x700") 
app.title("Logo File Input")

# Create a ctk frame
label = ctk.CTkLabel(app,text="Select a image file for Website's Logo") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
# Create widgets

label = ctk.CTkLabel(master=frame,text='Select image in png, jpeg, webp format only') 
label.pack(pady=12,padx=10)

entry= ctk.CTkEntry(master=frame,placeholder_text="Example: C://Desktop/image.jpeg") 
entry.pack(pady=12,padx=10) 
  
browse_button = ctk.CTkButton(master=frame, text="Upload", command=open_file_dialog)
browse_button.pack(pady=12,padx=10)

save_button = ctk.CTkButton(master=frame, text="Save LOGO", command=save_image_to_folder)
save_button.pack(pady=12,padx=10)

status_label = ctk.CTkLabel(master=frame, text="")
status_label.pack(pady=12,padx=10)

# Start the GUI
app.mainloop()


with open("./project_name.txt", 'r') as file:
  project_name = file.read()

source_dir = 'generate/settings/images'
dest_dir = f'{project_name}/src/images'

try:
  # Copy the entire contents of the source directory to the destination directory
  shutil.copytree(source_dir, dest_dir)
  print(f"Images copied from '{source_dir}' to '{dest_dir}' successfully.")
except Exception as e:
  print(f"Error copying images: {e}")

