import tkinter as tk
import random
import string

def generate_password(label, length):
    password_characters = string.ascii_letters + string.digits + "[]@#-_"
    password = ''.join(random.choice(password_characters) for _ in range(length))
    label.config(text=password)

if __name__ == '__main__':
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the X and Y coordinates for the centered window
    x = (screen_width - 300) // 2
    y = (screen_height - 200) // 2

    # Set the window geometry
    root.geometry(f"{300}x{200}+{x}+{y}")
    
    # Define a beautiful font
    beautiful_font = ("Helvetica", 14)  # Change the font family and size as desired

    label = tk.Label(root, font=beautiful_font)
    label.pack(side="top", anchor="center", pady=20)

    button = tk.Button(root, text='Generate Password', command=lambda: generate_password(label, length=12), font=beautiful_font)
    button.pack(side="top", pady=10)

    root.mainloop()
