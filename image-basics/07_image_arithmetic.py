import cv2

img=cv2.imread("image-basics/cat.jpg")

#brightness
#bright
bright=cv2.add(img,(50,50,50))
cv2.namedWindow("bright cat",cv2.WINDOW_NORMAL)
cv2.imshow("bright cat",bright)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#dark
dark=cv2.subtract(img,(50,50,50))
cv2.namedWindow("dark cat",cv2.WINDOW_NORMAL)
cv2.imshow("dark cat",dark)
cv2.waitKey(5000)
cv2.destroyAllWindows()