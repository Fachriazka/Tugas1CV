import cv2
  
cam = cv2.VideoCapture(0)
  
result, image = cam.read()
  
if result:
  
    cv2.imwrite("test.png", image)
  
else:
    print("error")