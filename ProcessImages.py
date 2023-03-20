import cv2
import numpy as np


def BuscarColor(frame):
    
    # Rango de color amarillo en formato HSV
    lower = np.array([20, 100, 100])
    upper = np.array([30, 255, 255])
    elem = []
    # Convertir el fotograma a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Aplicar la máscara para filtrar el color amarillo
    mask = cv2.inRange(hsv, lower, upper)

    # Aplicar una operación de erosión y dilatación para eliminar el ruido
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Encontrar los contornos del objeto amarillo
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 2000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x + int(w / 12), y + int(h / 8)), (x + int(w * 11 / 12), y + int(h * 2 / 8)), (0, 255, 255), 2)
            elem.append((x, y, w, h))

    # Mostrar el fotograma
    #cv2.imshow('Frame', frame)
    return elem

def IntersectionMasks(frame, faces, ball):
    
    # Se definen las máscaras
    face_mask = np.zeros(frame.shape[:2], dtype='uint8')
    ball_mask = np.zeros(frame.shape[:2], dtype='uint8')

    # Si se detecta al menos un rostro se crean las máscaras 
    if len(faces) > 0:
        (x,y,w,h) = faces[0]
        
        #Ajustes de las coordenadas de las máscaras
        
        x1_fmask = x + int(w / 12)
        x2_fmask = x + int(w * 11 / 12)
        y1_fmask = y + int(h / 8)
        y2_fmask = y + int(h * 2 / 8)
        x_bmask = int(ball.x + ball.radius + 7)
        y_bmask = int(ball.y + ball.radius + 3)
        
        #cv2.rectangle(frame,(x1_fmask, y1_fmask),(x2_fmask, y2_fmask),(0, 255, 0),1)
        detectado = True
        
        # Se crean las máscaras
        cv2.circle(ball_mask,(x_bmask, y_bmask),ball.radius ,255 , -1)
        cv2.rectangle(face_mask, (x1_fmask, y1_fmask),(x2_fmask, y2_fmask),255,-1)
        face_mask = cv2.flip(face_mask, 1)
        
    else:
        detectado = False

    colision = cv2.bitwise_and(face_mask, face_mask, mask=ball_mask)
    
    if(colision.any()==1):
        #Mostrar el puntaje
        return True

    return False