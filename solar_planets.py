import cv2
import numpy

img = cv2.imread("solar-system.jpg")



cv2.putText(img, "Mercury", (30, 350),fontFace= cv2.FONT_HERSHEY_SIMPLEX,   fontScale=1,color=(225,0,0))
cv2.putText(img, "Venus", (40, 500),fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,color=(0,115,0) )
cv2.putText(img, "Earth", (380, 430),fontFace= cv2.FONT_HERSHEY_SIMPLEX,  fontScale=1,color=(116,0,0) )
cv2.putText(img, "Mars", (580, 380),fontFace= cv2.FONT_HERSHEY_SIMPLEX,  fontScale=1,color=(0,0,255))
cv2.putText(img, "Jupiter", (700, 450),fontFace= cv2.FONT_HERSHEY_SIMPLEX,  fontScale=1,color=(0,0,255))
cv2.putText(img, "Saturn", (900, 420),fontFace= cv2.FONT_HERSHEY_SIMPLEX,  fontScale=1,color=(0,0,255) )
cv2.putText(img, "Uranus", (1100, 380),fontFace= cv2.FONT_HERSHEY_SIMPLEX,  fontScale=1,color=(0,0,255) )
cv2.putText(img, "Neptune", (1260, 400),fontFace= cv2.FONT_HERSHEY_SIMPLEX,  fontScale=1,color=(0,0,255))


cv2.imshow("output", img)
cv2.waitKey(0)


cv2.imwrite("solar-system.jpg", img)
