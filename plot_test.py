import cv2

img=cv2.imread("test_img/test2/IMG_20231108_154628.jpg")

file=open("1.txt")

pose_coordinates=file.read()

# index=pose_coordinates[0]
# x1,y1=pose_coordinates[1:3]

# x2,y2=pose_coordinates[3:5]

# p1_x,p1_y=pose_coordinates[5:7]

# p2_x,p2_y=pose_coordinates[7:9]

# p3_x,p3_y=pose_coordinates[9:11]

# p4_x,p4_y=pose_coordinates[11:]
def convert_yolov8_labels_to_numbers_with_pose(labels, img):
    print(type(img))
    image_height, image_width = img.shape[:2]
    converted_labels = []

    
    parts = list(map(float, labels.split()))
    print(parts)
    class_id = int(parts[0])
    center_x, center_y, width, height = map(int, map(round, parts[1:5]))

    # Convert bounding box coordinates to absolute values
    absolute_center_x = center_x + int(parts[5] * image_width)
    absolute_center_y = center_y + int(parts[6] * image_height)
    absolute_width = int(width * image_width)
    absolute_height = int(height * image_height)

    # Extract and convert pose keypoint coordinates to absolute values
    keypoints = [(int(parts[i] * image_width), int(parts[i + 1] * image_height)) for i in range(7, len(parts), 2)]

    converted_labels.append({
        'class_id': class_id,
        'absolute_center_x': absolute_center_x,
        'absolute_center_y': absolute_center_y,
        'absolute_width': absolute_width,
        'absolute_height': absolute_height,
        'keypoints': keypoints
    })
     # Draw bounding box and keypoints on the image
    cv2.rectangle(img, (absolute_center_x - absolute_width // 2, absolute_center_y - absolute_height // 2),
                    (absolute_center_x + absolute_width // 2, absolute_center_y + absolute_height // 2),
                    (0, 255, 0), 5)

    for kp in keypoints:
        cv2.circle(img, kp, 20, (255, 0, 0), -1)

    converted_labels.append({
        'class_id': class_id,
        'absolute_center_x': absolute_center_x,
        'absolute_center_y': absolute_center_y,
        'absolute_width': absolute_width,
        'absolute_height': absolute_height,
        'keypoints': keypoints
    })

    # Save the image with keypoints drawn
    cv2.imwrite("res.jpg", img)
    return converted_labels
labels=convert_yolov8_labels_to_numbers_with_pose(pose_coordinates,img)

print(labels)