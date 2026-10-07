import cv2

img=cv2.imread("image-basics/cat.jpg")

#grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)
cv2.namedWindow("grayscale cat",cv2.WINDOW_NORMAL)
cv2.imshow("grayscale cat",gray)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#bgr->rgb
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.namedWindow("rgb cat",cv2.WINDOW_NORMAL)
cv2.imshow("rgb cat",rgb)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#bgr->hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("hsv_cat",cv2.WINDOW_NORMAL)
cv2.imshow("hsv_cat",hsv)
cv2.waitKey(5000)
cv2.destroyAllWindows()