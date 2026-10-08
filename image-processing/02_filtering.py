import cv2

img=cv2.imread("image-processing/cat.jpg")
cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)

if img is None:
    print("error: could not load image")
    exit()

#average blur filtering
average=cv2.blur(img,(15,15))
cv2.namedWindow("Average Blur",cv2.WINDOW_NORMAL)
cv2.imshow("Average Blur",average)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#gaussian blur filtering
gaussian=cv2.GaussianBlur(img,(15,15),0)
cv2.namedWindow("Gaussian Blur",cv2.WINDOW_NORMAL)
cv2.imshow("Gaussian Blur",gaussian)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#median blur filtering
median=cv2.medianBlur(img,15)
cv2.namedWindow("Median Blur",cv2.WINDOW_NORMAL)
cv2.imshow("Median Blur",median)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#bilateral filtering
bilateral=cv2.bilateralFilter(img,15,75,75)
cv2.namedWindow("Bilateral Filter",cv2.WINDOW_NORMAL)
cv2.imshow("Bilateral Filter",bilateral)
cv2.waitKey(3000)
cv2.destroyAllWindows()