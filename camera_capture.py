""" 
Simple script to display and write frames from the selected camera using OpenCV.

You save frames by simply pressing "q" on your keyboard.
"""
import cv2

video_id = 6 # this is setup-dependent and would need to change. Ranges from 0-10+
cap = cv2.VideoCapture(video_id) 
i = 0

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) == ord('q'): # saves the current frame each time "q" is pressed
            print("Saving to frame.png")
            frame_str = 'calibration_imgs/calibration_img'+str(i)+'.png'
            # frame_str = 'aruco-board-cubes.png'
            cv2.imwrite(frame_str, frame)
            i+= 1

    else:
        print("Failed to capture frame")
        break

cap.release()