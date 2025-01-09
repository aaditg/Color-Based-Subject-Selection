from PIL import Image, ImageFilter
import os

def delete_existing_output():

    output_file = "isolated_subject.png"
    if os.path.exists(output_file):
        try:
            os.remove(output_file)
        except Exception as e:
            print("Could not delete file, check naming")

def load_color():
    try:
        with open("selected_color.txt", "r") as color_file:
            return color_file.read().strip().lower()
    except Exception as e:
        print("Error loading color file")
        raise

def is_within_range(pixel_color, min_color, max_color):
   
    r, g, b = pixel_color
    min_r, min_g, min_b = min_color
    max_r, max_g, max_b = max_color

    return (
        min_r <= r <= max_r and
        min_g <= g <= max_g and
        min_b <= b <= max_b
    )

def reduce_noise(image):
    filter_size = 7
    return image.filter(ImageFilter.MedianFilter(filter_size))  # Adjust filter size for different levels of noise reduction

def isolate_color(image, target_color_name):
    #add colors here, view range sizes for description
    color_ranges = {
        "red": ((120, 0, 0), (255, 130, 130)),       # Slightly smaller Red range
        "blue": ((0, 0, 120), (130, 130, 255)),      # Slightly smaller Blue range
        "yellow": ((120, 120, 0), (255, 255, 120)),  # Slightly smaller Yellow range
        "green": ((0, 120, 0), (130, 255, 130)),     # Slightly smaller Green range
        "orange": ((120, 60, 0), (255, 180, 90)),    # Slightly smaller Orange range
        "purple": ((90, 0, 90), (190, 110, 190)),    # Slightly smaller Purple range
    }

    if target_color_name not in color_ranges:
        raise ValueError("Invalid color")

    min_color, max_color = color_ranges[target_color_name]
    img = image.convert("RGBA")
    pixels = img.load()

    subject_found = False
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y] #a is alpha, alpha is opacity, if alpha is zero, it messes with selection

            # Check if the pixel is within the color range is not transparent (needed for certain filetypes)
            if a > 0 and is_within_range((r, g, b), min_color, max_color):
                subject_found = True
            else:
                pixels[x, y] = (0, 0, 0, 0)  # Set background to white transparent (alpha of zero)

    if not subject_found:
        print("No subject detected based on the selected color")
        #if there is a subject in the color, change the ranges above
    
    img = reduce_noise(img)
    

    return img
