from ultralytics import YOLO
import cv2
import pathlib

model = YOLO('best.pt')



test_img = 'test2'
image_path=pathlib.Path(test_img).glob("*.jpg")

# img=cv2.imread(str(next(image_path)))
# results = model(str(next(image_path)))[0]
# print(results.boxes)
# for i in results.keypoints.xy.tolist()[0]:
#     print(i)
for path in image_path:




    results = model(str(path))[0]
    img=cv2.imread(str(path))
    
    for result in results:
        # print((result.keypoints))
        x_min, y_min, x_max, y_max = map(int, result.boxes.xyxy.numpy()[0])
        img = cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (255,0,0), 5)

        for keypoint_indx, keypoint in enumerate(result.keypoints.xy.tolist()[0]):
            # print(result.keypoints.data.tolist())
            cv2.putText(img, str(keypoint_indx), (int(keypoint[0]), int(keypoint[1])),
                        cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 0), 5)

    output_image_path = f"result/{path.stem}.jpg"
    # Save the rotated image
    cv2.imwrite(output_image_path, img)