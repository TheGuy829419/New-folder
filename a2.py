import cv2

image = cv2.imread('Blox Fruits.png')

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 400, 400)

cv2.imshow('Loaded Image', image)
cv2.waitkey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")
