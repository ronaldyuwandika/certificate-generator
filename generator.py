
import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv



def create_image(name, template_path, output_dir, text_y, font_path, font_size, output_format):
    try:
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)

        # Capitalize the name
        capitalized_name = name.upper()

        font = ImageFont.truetype(font_path, font_size)

        # Get the width and height of the image
        W, H = img.size

        # Get the width and height of the text
        w, h = draw.textsize(capitalized_name, font=font)

        # Calculate the X position (center of image minus half of text width)
        text_x = (W - w) / 2

        draw.text((text_x, text_y), capitalized_name, font=font, fill="black")

        # Save the image as a PDF, PNG, or JPEG
        output_path = f"{output_dir}{capitalized_name}.{output_format.lower()}"
        img.save(output_path, output_format.upper(), resolution=100.0)

        print(f"Created output image: {output_path}")

    except Exception as e:
        print(f"An error occurred while creating image for name {name}: {str(e)}")




def replace_name():
    try:
        # Load the variables from the .env file
        load_dotenv()
        template_path = os.getenv("TEMPLATE_PATH")
        name_list_path = os.getenv("NAME_LIST_PATH")
        output_dir = os.getenv("OUTPUT_DIR")
        text_y = int(os.getenv("TEXT_Y"))
        font_path = os.getenv("FONT_PATH")
        font_size = int(os.getenv("FONT_SIZE"))
        font_fill = os.getenv("FONT_FILL_COLOR")
        output_format = os.getenv("OUTPUT_FORMAT")  # Get the output format from .env file

        names_df = pd.read_csv(name_list_path)
        names = names_df["Full Name"].tolist()

        for name in names:
            create_image(name, template_path, output_dir, text_x, text_y, font_path, font_size, font_fill, output_format)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
       

if __name__ == "__main__":
    replace_name()