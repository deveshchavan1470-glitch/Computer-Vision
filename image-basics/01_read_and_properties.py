import cv2

#read image
img=cv2.imread("image-basics/cat.jpg")
print(img)
print(img.shape)
height,width,channels=img.shape
print("height:",height)
print("width:",width)
print("channels:",channels)
