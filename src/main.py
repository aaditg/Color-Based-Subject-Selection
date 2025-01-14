import os
from image_loader import delete_existing_txt_files, load_image, get_color_input, save_image_and_color
from isolate_subject import delete_existing_output, load_color, isolate_color
from calculate_average_color import calculate_average_hex, save_average_color
from PIL import Image

def delete_all_files(exclude_file):
  
    files_to_delete = [f for f in os.listdir() if f.endswith(('.txt', '.png')) and f != exclude_file]
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Deleted file: {file}")
        except Exception as e:
            print(f"Could not delete file {file}: {e}")

def main():
    try:
        #Get the image file path from the user and clean up existing files (except the specified image file)
        image_path = input("Enter the path to the image file: ").strip()
        delete_all_files(exclude_file=os.path.basename(image_path))  # Exclude the specified image file

        #Load the image
        image = load_image(image_path)

        #Get user input for color
        color = get_color_input()
        save_image_and_color(image, color)

        #Subject Selection
        delete_existing_output()
        loaded_image = Image.open("loaded_image.png")
        selected_color = load_color()
        isolated_image = isolate_color(loaded_image, selected_color)
        isolated_image.save("isolated_subject.png")

        #Calculate the average hex color of the isolated subject
        avg_hex = calculate_average_hex("isolated_subject.png")
        save_average_color(avg_hex)
        print("Pipeline complete! Average hex color of the subject: " + avg_hex)

    except Exception as e:
        print("An error occurred: "+ e)

if __name__ == "__main__":
    main()
