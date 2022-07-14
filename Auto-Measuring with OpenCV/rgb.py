# importing required libraries
import cv2
import numpy as np
 
# taking the input from webcam
vid = cv2.VideoCapture(2)

# running while loop just to make sure that
# our program keep running until we stop it
while True:
    # capturing the current frame
    _, frame = vid.read()

    # setting values for base colors
    b = frame[:, :, :1]
    g = frame[:, :, 1:2]
    r = frame[:, :, 2:]
 
    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)
    
    ratio = r_mean/g_mean
    r_ratio = round(ratio,2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, str(r_ratio), (200,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255),2)
 
    # displaying the current frame
    cv2.imshow("frame", frame)
    cv2.waitKey(1)

    print (ratio)