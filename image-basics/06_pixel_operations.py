import cv2

img=cv2.imread("image-basics/cat.jpg")

#pixel access
px=img[100,100]
print(px)

blue=img[100,100,0]
green=img[100,100,1]
red=img[100,100,2]
print("blue:",blue)
print("green:",green)
print("red:",red)


#modify pixel
modified_img=img.copy()
modified_img[100,100]=[0,0,255]
cv2.namedWindow("modified cat",cv2.WINDOW_NORMAL)
cv2.imshow("modified cat",modified_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
