import cv2
from detector import detect_cards

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output = detect_cards(frame)

    cv2.imshow("Card Detection", output)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
        break

cap.release()
cv2.destroyAllWindows()