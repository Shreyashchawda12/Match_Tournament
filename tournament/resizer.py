from PIL import Image
from logger import logging
from exception import CustomException

import os
import sys

def resize_images(input_folder, output_folder, new_width, new_height):
    try:
        logging.info("Create the output folder if it doesn't exist")
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        logging.info("List all files in the input folder")
        files = os.listdir(input_folder)


        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
                input_path = os.path.join(input_folder, file)
                output_path = os.path.join(output_folder, file)

                logging.info("Open and resize the image")
                image = Image.open(input_path)
                resized_image = image.resize((new_width, new_height))

                logging.info("Save the resized image to the output folder")
                resized_image.save(output_path)

                logging.info("Close the image files")
                image.close()
                resized_image.close()

        logging.info("Image resizing complete.")
    
    except Exception as e:
            logging.info('Exception at resizing image')
            raise CustomException(e,sys)


input_folder = "test_data_raw"
output_folder = "test_data"
new_width = 1440
new_height = 900

resize_images(input_folder, output_folder, new_width, new_height)
