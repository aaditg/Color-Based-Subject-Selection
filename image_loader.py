from PIL import Image
import os

def delete_existing_txt_files():
    txt_files = [file for file in os.listdir() if file.endswith(".txt")]
    for txt_file in txt_files:
        try:
            os.remove(txt_file)
            print("Deleted existing file")
        except Exception as e:
            print("Could not delete file")

def load_image(image_path):
    try:
        image = Image.open(image_path)
        print("Image loaded successfully")
        return image
    except Exception as e:
        print("Error loading image")
        raise

def get_color_input():
    #Change colors here and below
    colors = ["red", "blue", "yellow", "green", "orange", "purple"]


    print("Enter a primary or secondary color from the following list:")
    print(", ".join(colors))
    
    while True:
        color = input("Color: ").strip().lower()
        if color in colors:
            print("Color selected: " + color)
            return color
        else:
            print("Invalid color. Please choose from: "+ ', '.join(colors))

def save_image_and_color(image, color):

    #Save the loaded image and the selected color for other files
    
    image.save("loaded_image.png")
    with open("selected_color.txt", "w") as color_file:
        color_file.write(color)
