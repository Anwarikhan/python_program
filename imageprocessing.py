import cv2
img=cv2.imread('B612_20190118_191530_945.jpg',0)
print(type(img))
print(img)
height =img.shape[0]
width=img.shape[1]
resized_height=int(height/2)
resized_Width=int(width/2)
resized_image=cv2.resize(img,(resized_Width,resized_height))
cv2.imwrite('new_B612_20190118_191530_945.jpg',resized_image)


# print(img.shape)
# cv2.imshow('B612_20190118_191530_945.jpg',resized_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()