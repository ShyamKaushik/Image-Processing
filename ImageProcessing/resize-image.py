import cv2
def resize(img_name,width,height):
    image = cv2.imread(img_name)
    cv2.imshow(image)
    cv2.waitKey(0)

resize('sample_img.jpg',1280,960)