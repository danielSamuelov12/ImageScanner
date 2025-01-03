import pytesseract
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Set Tesseract location for Windows (replace with your path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to perform OCR on an image
def ocr_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='eng')
    return text

# Function to select an image file
def open_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        try:
            # Performing OCR on the selected image
            extracted_text = ocr_from_image(file_path)
            text_box.delete(1.0, tk.END)  # Clears the text box
            text_box.insert(tk.END, extracted_text)  # Displays the extracted text in the text box
        except Exception as e:
            pass  # No error message shown

# Creating the main window with Tkinter
root = tk.Tk()
root.title("Scanner.com")
root.geometry("850x750")  # Larger window size
root.config(bg="#ffffff")  # White background color

# Modern style with ttk
style = ttk.Style()
style.configure('TButton',
                font=("Arial", 14, "bold"),
                padding=12,
                relief="flat",
                background="#007bff",  # Blue color for the button
                foreground="#007bff",
                anchor="center",
                width=20)
style.map('TButton',
          background=[('active', '#0056b3'),  # Darker blue when the button is clicked
                      ('pressed', '#004085')])  # Even darker blue when pressed

style.configure('TText',
                font=("Arial", 14),
                background="#f0f8ff",  # Light blue background for the text box
                relief="sunken",
                height=15,
                width=70,
                wrap=tk.WORD,
                foreground="black",
                bd=2,
                highlightbackground="#ddd",
                highlightthickness=1)

style.configure('TLabel',
                font=("Arial", 18, "bold"),
                background="#ffffff",  # White background for the label
                foreground="#007bff")  # Blue text color for the label

# Create the "Select Image" button
open_button = ttk.Button(root, text="Choose Image", command=open_image)
open_button.pack(pady=30)

# Create a text box to display the extracted text
text_box = tk.Text(root, height=15, width=70, wrap=tk.WORD, bd=2, font=("Arial", 14), relief="groove", highlightthickness=1, highlightbackground="#ddd")
text_box.pack(padx=10, pady=20)

# Create a button to clear the extracted text
clear_button = ttk.Button(root, text="Clear Text", command=lambda: text_box.delete(1.0, tk.END))
clear_button.pack(pady=10)

# Function to display the logo as text
def show_logo():
    logo_label = ttk.Label(root, text="Scanner.com", font=("Arial", 36, "bold"), background="#ffffff", foreground="#007bff")
    logo_label.pack(pady=50)  # Logo text displayed at the top with blue color

# Call the function to add the logo
show_logo()

# Add gradient background
def add_gradient_background():
    canvas = tk.Canvas(root, height=700, width=850)
    canvas.pack(fill="both", expand=True)
    gradient = tk.PhotoImage(width=850, height=700)
    for i in range(700):
        gradient.put("#ffffff", (0, i, 850, i+1))  # Gradient background color (light blue)
    canvas.create_image(0, 0, image=gradient, anchor="nw")
    canvas.image = gradient

# Add gradient background to the window
add_gradient_background()

# Run the GUI loop
root.mainloop()
