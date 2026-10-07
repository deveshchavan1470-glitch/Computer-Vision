import cv2

img=cv2.imread("image-basics/cat.jpg")

#display image
cv2.namedWindow("cat",cv2.WINDOW_NORMAL)
cv2.imshow("cat",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#save image
cv2.imwrite("cat_copy.jpg",img)
