import cv2

img=cv2.imread("image-basics/cat.jpg")

#flip image(1-horizontal,0-vertical,-1-both)
flipped_img=cv2.flip(img,1)
cv2.namedWindow("flipped cat",cv2.WINDOW_NORMAL)
cv2.imshow("flipped cat",flipped_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
#cv2.imwrite("flipped_cat.jpg",flipped_img)

#rotate image
rotated_img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.namedWindow("rotated_cat",cv2.WINDOW_NORMAL)
cv2.imshow("rotated_cat",rotated_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
#cv2.imwrite("rotated_cat.jpg",rotated_img)