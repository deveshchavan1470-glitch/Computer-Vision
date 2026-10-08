import cv2

img=cv2.imread("image-processing/cat.jpg")
cv2.imshow("Original", img)

if img is None:
    print("error: could not load image")
    exit()

#grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#basic binary thresholding
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
print("binary threshold:",ret)
cv2.imshow("Binary", binary)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#binary inverse thresholding
ret,binary_inv=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Binary Inverse", binary_inv)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#truncated thresholding
ret,trunc=cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
cv2.imshow("Truncation", trunc)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#tozero thresholding
ret,tozero=cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
cv2.imshow("To Zero", tozero)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#tozero inverse thresholding
ret,tozero_inv=cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("To Zero Inverse", tozero_inv)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#Otsu's thresholding
otsu_value,otsu=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Otsu's threshold:",otsu_value)
cv2.imshow("Otsu", otsu)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#adaptive mean thresholding
adaptive_mean=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Adaptive Mean", adaptive_mean)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#adaptive gaussian thresholding
adaptive_gaussian=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Adaptive Gaussian", adaptive_gaussian)
cv2.waitKey(3000)
cv2.destroyAllWindows()


