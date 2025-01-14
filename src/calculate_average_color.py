from PIL import Image

def calculate_average_hex(image_path):
    
    try:
        image = Image.open(image_path).convert("RGBA")
        pixels = image.load()
        total_r, total_g, total_b, pixel_count = 0, 0, 0, 0

        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = pixels[x, y]
                if a > 0:
                    total_r += r
                    total_g += g
                    total_b += b
                    pixel_count += 1

        if pixel_count == 0:
            raise ValueError("No subject detected")
        
        avg_r = total_r // pixel_count
        avg_g = total_g // pixel_count
        avg_b = total_b // pixel_count

        return "#{:02x}{:02x}{:02x}".format(avg_r, avg_g, avg_b).upper()

    except Exception as e:
        print("Error calculating average hex color")
        raise

def save_average_color(avg_hex):

    #Save the average color to a text file for use in other files and display

    with open("average_color.txt", "w") as output_file:
        output_file.write(avg_hex)
