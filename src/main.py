import cv2
from detector import detect_cards

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output, warped_cards = detect_cards(frame)

    cv2.imshow("Card Detection", output)

    # 🔥 mostrar cartas corrigidas
    for i, card in enumerate(warped_cards):
        cv2.imshow(f"Card {i}", card)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()