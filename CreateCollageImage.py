from PIL import Image

def create_collage(image_paths, output_path, output_format):
    try:
        # Load the four images
        images = [Image.open(image_path) for image_path in image_paths]

        # Resize images to have the same size (smallest width and height among the images)
        min_width = min(img.width for img in images)
        min_height = min(img.height for img in images)
        resized_images = [img.resize((min_width, min_height)) for img in images]

        # Create a blank canvas for the collage
        collage_width = min_width * 2
        collage_height = min_height * 2
        collage = Image.new('RGB', (collage_width, collage_height))

        # Paste the images onto the collage canvas
        collage.paste(resized_images[0], (0, 0))                      # Top-left
        collage.paste(resized_images[1], (min_width, 0))              # Top-right
        collage.paste(resized_images[2], (0, min_height))             # Bottom-left
        collage.paste(resized_images[3], (min_width, min_height))     # Bottom-right

        # Save the collage
        collage.save(output_path, format=output_format.upper())
        print("Collage created and saved as",output_path)

    except FileNotFoundError:
        print("Error: One or more image files not found. Please check the file paths.")
    except Exception as e:
        print("An unexpected error occurred:",e)

print("Enter the paths for four images:")
image1 = input("Path for Image 1: ").strip()
image2 = input("Path for Image 2: ").strip()
image3 = input("Path for Image 3: ").strip()
image4 = input("Path for Image 4: ").strip()
output_format = input("Enter the output format (e.g., jpg, png): ").strip().lower()
output_path = f"collage.{output_format}"

# Call the function to create the collage
create_collage([image1, image2, image3, image4], output_path, output_format)
