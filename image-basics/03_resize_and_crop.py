import cv2

img=cv2.imread("image-basics/cat.jpg")

#resize image
resized_image=cv2.resize(img,(300,300))
cv2.namedWindow("resized cat",cv2.WINDOW_NORMAL)
cv2.imshow("resized cat",resized_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()
#cv2.imwrite("cropped_cat.jpg",crop_img)

#crop image
crop_img=img[100:2000,100:800]
cv2.namedWindow("cropped cat",cv2.WINDOW_NORMAL)
cv2.imshow("cropped cat",crop_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
