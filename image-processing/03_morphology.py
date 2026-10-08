import cv2

img=cv2.imread("image-processing/cat.jpg")
cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)

if img is None:
    print("error: could not load image")
    exit()

#create a kernel/structuring element for morphologial operations
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#we can create ellipse and cross shaped kernels as well using cv2.MORPH_ELLIPSE and cv2.MORPH_CROSS

#erosion
erode=cv2.erode(img,kernel,iterations=1)
cv2.namedWindow("erosion",cv2.WINDOW_NORMAL)
cv2.imshow("erosion",erode)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#dilation
dilate=cv2.dilate(img,kernel,iterations=1)
cv2.namedWindow("dilation",cv2.WINDOW_NORMAL)
cv2.imshow("dilation",dilate)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#opening
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.namedWindow("opening",cv2.WINDOW_NORMAL)
cv2.imshow("opening",opening)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#closing
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.namedWindow("closing",cv2.WINDOW_NORMAL)
cv2.imshow("closing",closing)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#morphological gradient
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.namedWindow("morphological gradient",cv2.WINDOW_NORMAL)
cv2.imshow("morphological gradient",gradient)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#tophat
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.namedWindow("tophat",cv2.WINDOW_NORMAL)
cv2.imshow("tophat",tophat)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#blackhat
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.namedWindow("blackhat",cv2.WINDOW_NORMAL)
cv2.imshow("blackhat",blackhat)
cv2.waitKey(3000)
cv2.destroyAllWindows()
