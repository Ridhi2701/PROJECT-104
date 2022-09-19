from msilib import PID_LASTPRINTED
import cv2
import os

img= cv2.imread('solar-system.jpg')

cv2.putText(img,  
           'Sun',
           (110, 50),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.putText(img,  
           'Mercury',
           (125, 245),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           'Venus',
           (195, 175),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           'Earth',
           (290, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           'Mars',
           (385, 180),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           'Jupiter',
           (470, 100),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           'Saturn',
           (730, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           'Uranus',
           (965, 140),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           'Neptune',
           (1120, 280),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )


cv2.imshow("output",img)

cv2.waitKey(0)