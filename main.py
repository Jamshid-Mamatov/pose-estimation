import cv2
import numpy as np
import random
from pathlib import Path







# Load your image
directory_path = Path("pose_estimation")

# Use the glob method to find image files in the directory
image_files = directory_path.glob("*.jpg")

for image_path in image_files:
    image=cv2.imread(str(image_path))
    alfa_degrees = random.randint(0, 180)

    background=cv2.imread("cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3B4Njc1MzQwLWltYWdlLWt3dnhocW43LmpwZw.webp")

    background=cv2.resize(background,(5050,5050))


    image_height,image_width=image.shape[:2]
    c_x = (5050 - 1) / 2
    c_y = (5050 - 1) / 2

    alfa_radians = np.radians(alfa_degrees)

    half_width = image_width * 0.5
    half_height = image_height * 0.5

    new_corners = []
    for dx, dy in [(-half_width, -half_height), (-half_width, half_height), (half_width, half_height), (half_width, -half_height)]:
        new_x = c_x + dx * np.cos(alfa_radians) - dy * np.sin(alfa_radians)
        new_y = c_y + dx * np.sin(alfa_radians) + dy * np.cos(alfa_radians)
        new_corners.append((new_x, new_y))

    print(new_corners)

    pts=np.array(new_corners,np.int32)

    isClosed = True

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 10

    # Using cv2.polylines() method
    # Draw a Blue polygon with 
    # thickness of 1 px
    back = cv2.polylines(background, [pts], 
                        isClosed, color, thickness)




    imgCorners = np.float32([[0, 0], [0, image_height- 1], [image_width - 1, image_height - 1], [image_width - 1, 0]])

    warpedCorners = np.float32(new_corners)

    T = cv2.getPerspectiveTransform(imgCorners,warpedCorners)


    warpedImg = cv2.warpPerspective(image, T, background.shape[:2])

    cv2.fillConvexPoly(background, warpedCorners.astype(int), (0, 0, 0), lineType=cv2.LINE_AA)

    result = cv2.bitwise_or(warpedImg, background, dst=warpedImg)

    output_image_path = f"data/{image_path.stem}{alfa_degrees}.jpg"
    # Save the rotated image
    cv2.imwrite(output_image_path, result)