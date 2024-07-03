from PIL import Image

def resize_image(input_path, output_path):
    # Open an image file
    with Image.open(input_path) as img:
        # Calculate the new size maintaining the aspect ratio
        original_width, original_height = img.size
        aspect_ratio = original_width / original_height
        if aspect_ratio > 1:  # Landscape
            new_width = 8192
            new_height = int(8192 / aspect_ratio)
        else:  # Portrait or square
            new_height = 8192
            new_width = int(8192 * aspect_ratio)

        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        # Save the resized image
        resized_img.save(output_path)
        print(f"Resized image saved to {output_path}")

# Usage
resize_image("vis/sprite.jpg", "vis/sprite.jpg")
