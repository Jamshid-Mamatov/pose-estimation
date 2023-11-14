import cv2
import numpy as np
import random
from pathlib import Path

# Load your image
directory_path = Path("pose_estimation")

# Use the glob method to find image files in the directory
image_files = directory_path.glob("*.jpg")

for input_image_path in image_files:
# Read the image using OpenCV
    image = cv2.imread(str(input_image_path))

    # top_padding = 500  # You can adjust these values
    # bottom_padding = 500
    # left_padding = 500
    # right_padding = 500

 

    # # Create the padded image with border replication
    # image = cv2.copyMakeBorder(image, top_padding, bottom_padding, left_padding, right_padding, cv2.BORDER_REFLECT)
    # # Save or display the padded image
    
    # output_image = f"border/{input_image_path.stem}.jpg"
    # # Save the rotated image
    # cv2.imwrite(output_image, image)
    # Generate a random angle between 0 and 180 degrees

    random_angle = random.randint(0, 180)
    back_image=cv2.imread("background.jpg")

    # Get the height and width of the image
    height, width = image.shape[:2]
    back_shape=max(height,width)
    # Define the rotation center as the center of the image
    
    back_image=cv2.resize(back_image,(back_shape,back_shape))

    center = (width // 2, height // 2)

    # Create a rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, random_angle, 1.0)

    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    output_image_path = f"data/{input_image_path.stem}{random_angle}.jpg"
    # Save the rotated image
    cv2.imwrite(output_image_path, rotated_image)

# print(f"Image rotated by {random_angle} degrees and saved as {output_image_path}")
