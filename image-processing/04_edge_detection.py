import cv2

img=cv2.imread("image-processing/cat.jpg")
cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)

if img is None:
    print("error: could not load image")
    exit()

#sobel edge detection
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sobel_x=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
sobel_x=cv2.convertScaleAbs(sobel_x)
cv2.namedWindow("Sobel X",cv2.WINDOW_NORMAL)
cv2.imshow("Sobel X",sobel_x)
cv2.waitKey(3000)

sobel_y=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
sobel_y=cv2.convertScaleAbs(sobel_y)
cv2.namedWindow("Sobel Y",cv2.WINDOW_NORMAL)
cv2.imshow("Sobel Y",sobel_y)
cv2.waitKey(3000)

sobel_combined=cv2.addWeighted(sobel_x,0.5,sobel_y,0.5,0)
sobel_combined=cv2.convertScaleAbs(sobel_combined)
cv2.namedWindow("Sobel Combined",cv2.WINDOW_NORMAL)
cv2.imshow("Sobel Combined",sobel_combined)
cv2.waitKey(3000)


#laplacian edge detection
laplacian=cv2.Laplacian(gray,cv2.CV_64F)
laplacian=cv2.convertScaleAbs(laplacian)
cv2.namedWindow("Laplacian",cv2.WINDOW_NORMAL)
cv2.imshow("Laplacian",laplacian)
cv2.waitKey(3000)

#canny edge detection
canny=cv2.Canny(gray,100,200)
canny=cv2.convertScaleAbs(canny)
cv2.namedWindow("Canny",cv2.WINDOW_NORMAL)
cv2.imshow("Canny",canny)
cv2.waitKey(3000)

blur=cv2.GaussianBlur(gray,(5,5),0)
canny_blur=cv2.Canny(blur,100,200)
canny_blur=cv2.convertScaleAbs(canny_blur)
cv2.namedWindow("Canny Blurred",cv2.WINDOW_NORMAL)
cv2.imshow("Canny Blurred",canny_blur)
cv2.waitKey(3000)

