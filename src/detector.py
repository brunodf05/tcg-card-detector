import cv2

def detect_cards(frame):
    output = frame.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # ignora coisas pequenas
        if area < 5000:
            continue

        # aproxima o contorno
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

        # queremos retângulos (4 lados)
        if len(approx) == 4:
            cv2.drawContours(output, [approx], -1, (0, 255, 0), 3)

    return output