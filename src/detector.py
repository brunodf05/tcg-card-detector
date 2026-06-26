import cv2
import numpy as np

def order_points(pts):
    pts = pts.reshape(4, 2)

    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # topo-esquerda
    rect[2] = pts[np.argmax(s)]  # baixo-direita

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # topo-direita
    rect[3] = pts[np.argmax(diff)]  # baixo-esquerda

    return rect


def warp_card(frame, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = int(max(widthA, widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = int(max(heightA, heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(frame, M, (maxWidth, maxHeight))

    return warp


def detect_cards(frame):
    output = frame.copy()
    warped_cards = []

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area < 5000:
            continue

        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

        if len(approx) == 4:
            cv2.drawContours(output, [approx], -1, (0, 255, 0), 3)

            # 🔥 NOVO: gerar carta corrigida
            warped = warp_card(frame, approx)
            warped_cards.append(warped)

    return output, warped_cards