import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # or use dummy data

while True:
    frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
    cv2.imshow("Test Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
