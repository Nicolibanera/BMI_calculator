from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#1E1E2E")

# Modern color scheme
COLORS = {
    "bg": "#1E1E2E",
    "card": "#2D3047", 
    "accent": "#FF6B6B",
    "text_light": "#E6E6FA",
    "success": "#81C784",
    "warning": "#FFB74D",
    "danger": "#E57373"
}

# Load category icons
def load_icon(path, size=(25, 25)):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return None

# Load all category icons
underweight_icon = load_icon("icons/underweight.png")
normal_icon = load_icon("icons/normal.png")
overweight_icon = load_icon("icons/overweight.png")
obese_icon = load_icon("icons/obese.png")
health_icon = load_icon("icons/health.png")

def BMI():
    try:
        h = float(Height.get())
        w = float(Weight.get())

        # Convert height into meter
        m = h/100
        bmi = round(float(w/m**2), 1)
        label1.config(text=bmi)

        # Color code the BMI result and set icons
        if bmi <= 18.5:
            label1.config(fg=COLORS["warning"])
            label2.config(text="Underweight!", fg=COLORS["warning"])
            label3.config(text="You're doing great! Let's work on building some healthy mass together!")
            if underweight_icon:
                icon_label.config(image=underweight_icon)
        elif bmi > 18.5 and bmi <= 25:
            label1.config(fg=COLORS["success"])
            label2.config(text="Normal!", fg=COLORS["success"])
            label3.config(text="Perfect! You're in the healthy range! Keep up the amazing work!")
            if normal_icon:
                icon_label.config(image=normal_icon)
        elif bmi > 25 and bmi <= 30:
            label1.config(fg=COLORS["warning"])
            label2.config(text="OverWeight!", fg=COLORS["warning"])
            label3.config(text="You've got this! Small changes can lead to big results!")
            if overweight_icon:
                icon_label.config(image=overweight_icon)
        else:
            label1.config(fg=COLORS["danger"])
            label2.config(text="Obese!", fg=COLORS["danger"])
            label3.config(text="Your health journey starts today! Every step counts!")
            if obese_icon:
                icon_label.config(image=obese_icon)

    except ValueError:
        # Show error for invalid input
        label1.config(text="Error", fg=COLORS["danger"])
        label2.config(text="Invalid Input!", fg=COLORS["danger"])
        label3.config(text="Please enter valid numbers only")
        icon_label.config(image='')

# icon
try:
    image_icon = PhotoImage(file="icons/calculator.png")
    root.iconphoto(False, image_icon)
except:
    pass

# top
try:
    top = PhotoImage(file="icons/top.png")
    top_image = Label(root, image=top, background=COLORS["bg"])
    top_image.place(x=-10, y=-10)
except:
    pass

# bottom box
Label(root, width=72, height=18, bg=COLORS["card"]).pack(side=BOTTOM)

# two boxes
try:
    box = PhotoImage(file="icons/box.png")
    Label(root, image=box).place(x=20, y=100)
    Label(root, image=box).place(x=240, y=100)
except:
    pass

# Add labels above entry boxes
Label(root, text="HEIGHT (cm)", fg=COLORS["text_light"], font=("Arial", 12, "bold"), bg=COLORS["bg"]).place(x=35, y=120)
Label(root, text="WEIGHT (kg)", fg=COLORS["text_light"], font=("Arial", 12, "bold"), bg=COLORS["bg"]).place(x=255, y=120)

# Add main title with health icon
title_frame = Frame(root, bg=COLORS["bg"])
title_frame.place(x=140, y=70)

if health_icon:
    title_icon = Label(title_frame, image=health_icon, bg=COLORS["bg"])
    title_icon.pack(side=LEFT, padx=(0, 10))

title_label = Label(title_frame, text="ENTER YOUR DETAILS", fg=COLORS["accent"], font=("Arial", 16, "bold"), bg=COLORS["bg"])
title_label.pack(side=LEFT)

# scale
try:
    scale = PhotoImage(file="icons/scale.png")
    Label(root, image=scale, bg=COLORS["card"]).place(x=20, y=310)
except:
    pass


def resetButton():
    print('hello')


####################Slider1###################
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open("icons/man.png"))

    current_weight = int(float(Weight.get()))

    new_height = 10 + size
    new_width = (current_weight // 2) + 50

    resized_image = img.resize((new_width, new_height))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - new_height)
    secondimage.image = photo2

# Command to change background color of scale
style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale",
                  command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

# Slider2
current_value2 = tk.DoubleVar()#i will changtr

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

    size = int(float(get_current_value2()))
    img = (Image.open("icons/man.png"))

    current_height = int(float(Height.get())) if Height.get() else 100

    new_width = 50 + (size // 2)
    new_height = current_height + 10

    resized_image = img.resize((new_width, new_height))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - new_height)
    secondimage.image = photo2

# Command to change background color of scale
style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale",
                   command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

# Entry box
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# man image
secondimage = Label(root, bg=COLORS["card"])
secondimage.place(x=70, y=350)

# View Report button
Button(root, text="View Report", width=15, height=2, font="arial 10 bold", 
       bg=COLORS["accent"], fg="white", command=BMI).place(x=280, y=340)






# BMI result section with icon
label1 = Label(root, font="arial 30 bold", bg=COLORS["card"], fg=COLORS["text_light"])
label1.place(x=300, y=400)

# Create a frame for category with icon
category_frame = Frame(root, bg=COLORS["card"])
category_frame.place(x=280, y=440)

# Icon label for category
icon_label = Label(category_frame, bg=COLORS["card"])
icon_label.pack(side=LEFT, padx=(0, 10))

label2 = Label(category_frame, font="arial 16 bold", bg=COLORS["card"], fg=COLORS["text_light"])
label2.pack(side=LEFT)

label3 = Label(root, font="arial 10", bg=COLORS["card"], fg=COLORS["text_light"], wraplength=180, justify=LEFT)
label3.place(x=280, y=470)

# Set default health icon
if health_icon:
    icon_label.config(image=health_icon)

root.mainloop()